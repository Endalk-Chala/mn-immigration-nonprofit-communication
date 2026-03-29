#!/usr/bin/env python3
"""
Study 2 — Media Relations Audit
Twin Cities Immigration Nonprofit Coverage Scraper
Outlets: MPR News, Sahan Journal, MinnPost, Axios Twin Cities, Bring Me The News

Usage:
    cd C:\\Users\\endal\\OneDrive\\Desktop\\PR
    python study2_media_audit\\scrapers\\media_scraper.py

Output:
    study2_media_audit/data/raw/media_coverage_raw.xlsx
    study2_media_audit/data/raw/media_coverage_raw.csv

Requirements (auto-installed): requests beautifulsoup4 openpyxl pandas
"""

# ── Auto-install ──────────────────────────────────────────────────────────────
import subprocess, sys
for pkg in ["requests", "beautifulsoup4", "openpyxl", "pandas"]:
    try:
        __import__(pkg if pkg != "beautifulsoup4" else "bs4")
    except ImportError:
        print(f"Installing {pkg}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re, time, json
from datetime import date, datetime
from urllib.parse import urljoin, quote_plus
import os

# ── Output paths ──────────────────────────────────────────────────────────────
OUT_DIR  = os.path.join("study2_media_audit", "data", "raw")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_XLSX = os.path.join(OUT_DIR, "media_coverage_raw.xlsx")
OUT_CSV  = os.path.join(OUT_DIR, "media_coverage_raw.csv")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# ── Study parameters ──────────────────────────────────────────────────────────
STUDY_START = datetime(2025, 10, 1)
STUDY_END   = datetime(2026, 3, 26)

ORGANIZATIONS = [
    "Immigrant Law Center of Minnesota",
    "ILCM",
    "International Institute of Minnesota",
    "IIMN",
    "Advocates for Human Rights",
    "The Advocates for Human Rights",
    "Arrive Ministries",
    "Karen Organization of Minnesota",
    "KOM",
    "MN Interfaith Coalition on Immigration",
    "ICOM",
    "Unidos MN",
    "Monarca",
]

# Search terms combining org names with enforcement context
SEARCH_QUERIES = [
    "immigration enforcement Minnesota nonprofit",
    "Operation Metro Surge nonprofit",
    "Operation PARRIS refugee Minnesota",
    "ICE Minnesota immigrant organization",
    "Immigrant Law Center Minnesota",
    "International Institute Minnesota",
    "Advocates Human Rights Minnesota immigration",
    "Arrive Ministries refugee",
    "Karen Organization Minnesota ICE",
    "Unidos MN immigration",
    "ICOM immigration Minnesota",
]

# ── Appearance type classifier ────────────────────────────────────────────────
QUOTE_SIGNALS = [
    "said,", "says,", "said.", "says.", "according to",
    "told", "stated", "commented", "noted", "explained",
    "remarked", "added", "argued", "wrote",
]
OPEDS = ["opinion", "op-ed", "commentary", "perspective", "editorial", "column"]
PRESS_RELEASE_SIGNALS = [
    "press release", "for immediate release", "media contact",
    "contact:", "###", "– end –",
]

def classify_appearance(title, text, url):
    title_l = title.lower()
    url_l   = url.lower()
    text_l  = text.lower()[:3000]  # check first 3000 chars

    if any(kw in title_l or kw in url_l for kw in OPEDS):
        return "Op-ed / Column"
    if any(kw in text_l for kw in PRESS_RELEASE_SIGNALS):
        return "Press Release Pickup"
    if any(kw in text_l for kw in QUOTE_SIGNALS):
        return "Quoted as Source"
    if any(org.lower() in text_l for org in ORGANIZATIONS):
        return "Organization Named/Referenced"
    return "Mentioned"

def org_mentions(text):
    """Return list of which orgs appear in the text."""
    found = []
    text_l = text.lower()
    pairs = [
        ("ILCM", ["immigrant law center of minnesota", "ilcm"]),
        ("IIMN", ["international institute of minnesota", "iimn"]),
        ("The Advocates", ["advocates for human rights"]),
        ("Arrive Ministries", ["arrive ministries"]),
        ("KOM", ["karen organization of minnesota", " kom "]),
        ("ICOM", ["interfaith coalition on immigration", "icom"]),
        ("Unidos MN", ["unidos mn", "unidos minnesota", "monarca"]),
    ]
    for label, keywords in pairs:
        if any(kw in text_l for kw in keywords):
            found.append(label)
    return "; ".join(found) if found else ""

def in_study_window(date_str):
    """Return True if date_str falls within Oct 2025 – Mar 26 2026."""
    if not date_str:
        return True  # include if undated, flag for manual review
    for fmt in ["%Y-%m-%d", "%B %d, %Y", "%b %d, %Y", "%m/%d/%Y", "%Y/%m/%d"]:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return STUDY_START <= dt <= STUDY_END
        except:
            continue
    return True  # include and flag

def safe_fetch(url, timeout=12):
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        r.raise_for_status()
        return r.text
    except Exception as e:
        return None

# ═════════════════════════════════════════════════════════════════════════════
# OUTLET SCRAPERS
# ═════════════════════════════════════════════════════════════════════════════

# ── 1. MPR News ───────────────────────────────────────────────────────────────
def scrape_mpr(query):
    results = []
    page = 1
    while page <= 5:
        url = f"https://www.mprnews.org/search?q={quote_plus(query)}&page={page}"
        html = safe_fetch(url)
        if not html:
            break
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.select("article, .search-result, .result-item, h3 a, h2 a")
        if not articles:
            break
        found_any = False
        for item in soup.select("article"):
            title_el = item.select_one("h2, h3, h4, .title")
            link_el  = item.select_one("a[href]")
            date_el  = item.select_one("time, .date, .pub-date")
            if not title_el or not link_el:
                continue
            title    = title_el.get_text(strip=True)
            art_url  = urljoin("https://www.mprnews.org", link_el["href"])
            pub_date = date_el.get("datetime", date_el.get_text(strip=True)) if date_el else ""
            if not in_study_window(pub_date):
                continue
            # Fetch article for full text
            time.sleep(0.8)
            art_html = safe_fetch(art_url)
            body_text = ""
            if art_html:
                art_soup  = BeautifulSoup(art_html, "html.parser")
                body_text = art_soup.get_text(" ", strip=True)
            orgs = org_mentions(title + " " + body_text)
            if not orgs:
                continue
            results.append({
                "Outlet":         "MPR News",
                "Title":          title,
                "URL":            art_url,
                "Date":           pub_date,
                "Orgs_Mentioned": orgs,
                "Appearance_Type":classify_appearance(title, body_text, art_url),
                "Query_Used":     query,
                "Full_Text_Excerpt": body_text[:1000],
            })
            found_any = True
        if not found_any:
            break
        page += 1
        time.sleep(1.5)
    return results

# ── 2. Sahan Journal ──────────────────────────────────────────────────────────
def scrape_sahan(query):
    results = []
    url = f"https://sahanjournal.com/?s={quote_plus(query)}"
    html = safe_fetch(url)
    if not html:
        return results
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.select("article, .post, .entry"):
        title_el = item.select_one("h2, h3, .entry-title")
        link_el  = item.select_one("a[href]")
        date_el  = item.select_one("time, .entry-date, .published")
        if not title_el or not link_el:
            continue
        title    = title_el.get_text(strip=True)
        art_url  = urljoin("https://sahanjournal.com", link_el["href"])
        pub_date = date_el.get("datetime", date_el.get_text(strip=True)) if date_el else ""
        if not in_study_window(pub_date):
            continue
        time.sleep(0.8)
        art_html  = safe_fetch(art_url)
        body_text = ""
        if art_html:
            art_soup  = BeautifulSoup(art_html, "html.parser")
            body_text = art_soup.get_text(" ", strip=True)
        orgs = org_mentions(title + " " + body_text)
        if not orgs:
            continue
        results.append({
            "Outlet":         "Sahan Journal",
            "Title":          title,
            "URL":            art_url,
            "Date":           pub_date,
            "Orgs_Mentioned": orgs,
            "Appearance_Type":classify_appearance(title, body_text, art_url),
            "Query_Used":     query,
            "Full_Text_Excerpt": body_text[:1000],
        })
        time.sleep(1.0)
    return results

# ── 3. MinnPost ───────────────────────────────────────────────────────────────
def scrape_minnpost(query):
    results = []
    url = f"https://www.minnpost.com/?s={quote_plus(query)}"
    html = safe_fetch(url)
    if not html:
        return results
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.select("article, .search-result, .post"):
        title_el = item.select_one("h2, h3, .entry-title, .post-title")
        link_el  = item.select_one("a[href]")
        date_el  = item.select_one("time, .entry-date, .post-date")
        if not title_el or not link_el:
            continue
        title    = title_el.get_text(strip=True)
        art_url  = urljoin("https://www.minnpost.com", link_el["href"])
        pub_date = date_el.get("datetime", date_el.get_text(strip=True)) if date_el else ""
        if not in_study_window(pub_date):
            continue
        time.sleep(0.8)
        art_html  = safe_fetch(art_url)
        body_text = ""
        if art_html:
            art_soup  = BeautifulSoup(art_html, "html.parser")
            body_text = art_soup.get_text(" ", strip=True)
        orgs = org_mentions(title + " " + body_text)
        if not orgs:
            continue
        results.append({
            "Outlet":         "MinnPost",
            "Title":          title,
            "URL":            art_url,
            "Date":           pub_date,
            "Orgs_Mentioned": orgs,
            "Appearance_Type":classify_appearance(title, body_text, art_url),
            "Query_Used":     query,
            "Full_Text_Excerpt": body_text[:1000],
        })
        time.sleep(1.0)
    return results

# ── 4. Axios Twin Cities ──────────────────────────────────────────────────────
def scrape_axios(query):
    results = []
    # Axios uses a JS-rendered frontend but their search returns some accessible results
    url = f"https://www.axios.com/local/twin-cities?q={quote_plus(query)}"
    html = safe_fetch(url)
    if not html:
        return results
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.select("article, [data-testid='story'], .story-card"):
        title_el = item.select_one("h2, h3, [data-testid='headline']")
        link_el  = item.select_one("a[href]")
        date_el  = item.select_one("time, [data-testid='timestamp']")
        if not title_el or not link_el:
            continue
        title    = title_el.get_text(strip=True)
        art_url  = urljoin("https://www.axios.com", link_el["href"])
        pub_date = date_el.get("datetime", date_el.get_text(strip=True)) if date_el else ""
        if not in_study_window(pub_date):
            continue
        time.sleep(0.8)
        art_html  = safe_fetch(art_url)
        body_text = ""
        if art_html:
            art_soup  = BeautifulSoup(art_html, "html.parser")
            body_text = art_soup.get_text(" ", strip=True)
        orgs = org_mentions(title + " " + body_text)
        if not orgs:
            continue
        results.append({
            "Outlet":         "Axios Twin Cities",
            "Title":          title,
            "URL":            art_url,
            "Date":           pub_date,
            "Orgs_Mentioned": orgs,
            "Appearance_Type":classify_appearance(title, body_text, art_url),
            "Query_Used":     query,
            "Full_Text_Excerpt": body_text[:1000],
        })
        time.sleep(1.0)
    return results

# ── 5. Bring Me The News ──────────────────────────────────────────────────────
def scrape_bmtn(query):
    results = []
    url = f"https://bringmethenews.com/?s={quote_plus(query)}"
    html = safe_fetch(url)
    if not html:
        return results
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.select("article, .post, .search-result"):
        title_el = item.select_one("h2, h3, .entry-title")
        link_el  = item.select_one("a[href]")
        date_el  = item.select_one("time, .entry-date, .post-date")
        if not title_el or not link_el:
            continue
        title    = title_el.get_text(strip=True)
        art_url  = urljoin("https://bringmethenews.com", link_el["href"])
        pub_date = date_el.get("datetime", date_el.get_text(strip=True)) if date_el else ""
        if not in_study_window(pub_date):
            continue
        time.sleep(0.8)
        art_html  = safe_fetch(art_url)
        body_text = ""
        if art_html:
            art_soup  = BeautifulSoup(art_html, "html.parser")
            body_text = art_soup.get_text(" ", strip=True)
        orgs = org_mentions(title + " " + body_text)
        if not orgs:
            continue
        results.append({
            "Outlet":         "Bring Me The News",
            "Title":          title,
            "URL":            art_url,
            "Date":           pub_date,
            "Orgs_Mentioned": orgs,
            "Appearance_Type":classify_appearance(title, body_text, art_url),
            "Query_Used":     query,
            "Full_Text_Excerpt": body_text[:1000],
        })
        time.sleep(1.0)
    return results

# ═════════════════════════════════════════════════════════════════════════════
# SAVE OUTPUT
# ═════════════════════════════════════════════════════════════════════════════
def save_outputs(all_results):
    df = pd.DataFrame(all_results)

    if df.empty:
        print("\n  WARNING: No results collected. Check outlet connectivity.")
        return

    # Deduplicate by URL
    df = df.drop_duplicates(subset=["URL"])
    df = df.sort_values(["Outlet", "Date"], ascending=[True, False])

    # Add coding columns
    df["Paid_or_Unpaid"]        = ""   # manual: Paid / Unpaid
    df["Frame_Match_Study1"]    = ""   # manual: does media frame match org frame?
    df["Quote_Org_Verified"]    = ""   # manual: Y/N
    df["Spokesperson_Named"]    = ""   # manual: name
    df["Notes"]                 = ""

    # CSV
    df.to_csv(OUT_CSV, index=False)
    print(f"  Saved: {OUT_CSV}")

    # Excel with formatting
    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Media Coverage Raw")

        # Summary pivot by outlet + appearance type
        pivot = df.groupby(["Outlet", "Appearance_Type"]).size().reset_index(name="Count")
        pivot.to_excel(writer, index=False, sheet_name="Summary by Outlet")

        # Summary pivot by org
        org_rows = []
        for org in ["ILCM","IIMN","The Advocates","Arrive Ministries","KOM","ICOM","Unidos MN"]:
            count = df["Orgs_Mentioned"].str.contains(org, na=False).sum()
            org_rows.append({"Organization": org, "Total_Mentions": count})
        pd.DataFrame(org_rows).to_excel(writer, index=False, sheet_name="Summary by Org")

        # Format main sheet
        ws = writer.sheets["Media Coverage Raw"]
        ws.freeze_panes = "A2"
        for col in ws.columns:
            max_len = max((len(str(c.value or "")) for c in col), default=10)
            ws.column_dimensions[col[0].column_letter].width = min(max_len + 3, 60)

    print(f"  Saved: {OUT_XLSX}")
    print(f"\n  Total unique articles: {len(df)}")
    print("\n  Articles by outlet:")
    for outlet, count in df["Outlet"].value_counts().items():
        print(f"    {outlet}: {count}")
    print("\n  Mentions by organization:")
    for org in ["ILCM","IIMN","The Advocates","Arrive Ministries","KOM","ICOM","Unidos MN"]:
        count = df["Orgs_Mentioned"].str.contains(org, na=False).sum()
        print(f"    {org}: {count}")

# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
SCRAPERS = [
    ("MPR News",          scrape_mpr),
    ("Sahan Journal",     scrape_sahan),
    ("MinnPost",          scrape_minnpost),
    ("Axios Twin Cities", scrape_axios),
    ("Bring Me The News", scrape_bmtn),
]

if __name__ == "__main__":
    print("\n" + "="*60)
    print("  Study 2 — Media Relations Audit Scraper")
    print("  Twin Cities Immigration Nonprofit Coverage")
    print(f"  Window: Oct 1 2025 – Mar 26 2026")
    print("="*60)

    all_results = []

    for outlet_name, scraper_fn in SCRAPERS:
        print(f"\n── {outlet_name} ──────────────────────────────")
        outlet_results = []
        for query in SEARCH_QUERIES:
            print(f"  Query: {query[:50]}...")
            try:
                results = scraper_fn(query)
                outlet_results.extend(results)
                print(f"  → {len(results)} articles found")
            except Exception as e:
                print(f"  ERROR: {e}")
            time.sleep(1.5)
        print(f"  Subtotal {outlet_name}: {len(outlet_results)} articles")
        all_results.extend(outlet_results)

    print(f"\n{'='*60}")
    print(f"  Total articles collected (before dedup): {len(all_results)}")
    print("\n  Saving outputs...")
    save_outputs(all_results)

    print("\n  NEXT STEPS:")
    print("  1. Open media_coverage_raw.xlsx")
    print("  2. Review each article and fill in:")
    print("     - Paid_or_Unpaid (most will be Unpaid)")
    print("     - Quote_Org_Verified (Y/N)")
    print("     - Spokesperson_Named (who was quoted)")
    print("     - Frame_Match_Study1 (does media frame = org frame?)")
    print("  3. Add Star Tribune / Pioneer Press results manually")
    print("     from LexisNexis or ProQuest")
    print("="*60 + "\n")
