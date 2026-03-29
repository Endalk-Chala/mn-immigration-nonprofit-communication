#!/usr/bin/env python3
"""
IAN Minnesota Immigration Legal Services Directory Scraper
Run this entire script in your terminal:

    python scrape_ian_mn.py

Requirements (installed automatically if missing):
    requests, beautifulsoup4, openpyxl, pandas
"""

import subprocess, sys

def install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

for pkg in ["requests", "beautifulsoup4", "openpyxl", "pandas"]:
    try:
        __import__(pkg if pkg != "beautifulsoup4" else "bs4")
    except ImportError:
        print(f"Installing {pkg}...")
        install(pkg)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import date

BASE_URL = "https://www.immigrationadvocates.org/nonprofit/legaldirectory/search"
PARAMS = {
    "state": "MN", "national": "0", "county": "", "legalArea": "",
    "legalService": "", "nonLegalService": "", "interestArea": "",
    "population": "", "legalNetwork": "", "language": "",
    "detentionFacility": "", "text": "", "zip": "", "interpreting": "0", "map": "0",
}
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def parse_page(soup):
    orgs = []
    for h4 in soup.find_all("h4"):
        org = {}
        a = h4.find("a")
        org["Name"] = a.get_text(strip=True) if a else h4.get_text(strip=True)
        org["Profile URL"] = (
            "https://www.immigrationadvocates.org" + a["href"]
            if a and a.get("href") else ""
        )
        sibling = h4.find_next_sibling()
        while sibling and sibling.name in ("table", "hr", "p", "br"):
            if sibling.name == "table":
                for row in sibling.find_all("tr"):
                    cells = row.find_all("td")
                    if len(cells) == 2:
                        key = cells[0].get_text(strip=True).rstrip(":")
                        val = cells[1].get_text(" ", strip=True)
                        org[key] = val
            sibling = sibling.find_next_sibling()
            if sibling and sibling.name == "h4":
                break
        orgs.append(org)
    return orgs

def scrape_all_pages():
    all_orgs = []
    page = 1
    while True:
        params = dict(PARAMS)
        if page > 1:
            params["page"] = page
        print(f"  Fetching page {page}...")
        try:
            resp = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=15)
            resp.raise_for_status()
        except Exception as e:
            print(f"  ERROR on page {page}: {e}")
            break
        soup = BeautifulSoup(resp.text, "html.parser")
        orgs = parse_page(soup)
        if not orgs:
            break
        all_orgs.extend(orgs)
        print(f"  -> {len(orgs)} organizations found on page {page}")
        next_link = soup.find("a", string=lambda t: t and "Next" in t)
        if not next_link:
            break
        page += 1
        time.sleep(1.5)
    return all_orgs

def save_outputs(orgs):
    df = pd.DataFrame(orgs)
    priority_cols = [
        "Name", "Location", "Contact",
        "Areas of legal assistance",
        "Types of legal assistance",
        "Profile URL",
    ]
    other_cols = [c for c in df.columns if c not in priority_cols]
    df = df[[c for c in priority_cols if c in df.columns] + other_cols]

    df.insert(0, "Source", "IAN National Legal Services Directory - MN")
    df.insert(1, "Date Retrieved", str(date.today()))
    df.insert(2, "Twin Cities Based (Y/N)", "")
    df.insert(3, "Active Digital Presence (Y/N)", "")
    df.insert(4, "Enforcement Responsive (Y/N)", "")
    df.insert(5, "IN STUDY SAMPLE", "")
    df.insert(6, "Exclusion Reason", "")

    csv_file = "ian_mn_organizations.csv"
    df.to_csv(csv_file, index=False)
    print(f"  Saved: {csv_file}")

    xlsx_file = "ian_mn_organizations.xlsx"
    with pd.ExcelWriter(xlsx_file, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="IAN MN Sampling Frame")
        ws = writer.sheets["IAN MN Sampling Frame"]
        ws.freeze_panes = "A2"
        for col in ws.columns:
            max_len = max((len(str(c.value or "")) for c in col), default=10)
            ws.column_dimensions[col[0].column_letter].width = min(max_len + 4, 60)
    print(f"  Saved: {xlsx_file}")

if __name__ == "__main__":
    print("\n" + "="*55)
    print("  IAN Minnesota Immigration Nonprofits Scraper")
    print("="*55)
    orgs = scrape_all_pages()
    print(f"\n  Total organizations found: {len(orgs)}")
    print("\n  Saving outputs...")
    save_outputs(orgs)
    print("\n  DONE.")
    print("  Open ian_mn_organizations.xlsx")
    print("  Fill in columns C-G to document your sampling decisions.")
    print("="*55 + "\n")
