import argparse
import os
import pandas as pd
from playwright.sync_api import sync_playwright

def extract_from_cards(page):
    shops = page.query_selector_all('div.Nv2PK')
    results = []

    for shop in shops:
        try:
            a_tag = shop.query_selector('a.hfpxzc')
            maps_link = a_tag.get_attribute("href") if a_tag else ""

            scrapio_card = shop.query_selector('.scrapio-card') or shop.query_selector('.scrapio-card__main')

            data = {
                "maps_link": maps_link,
                "email": "",
                "phone": "",
                "website": "",
                "contact_page": "",
                "facebook": "",
                "instagram": "",
            }

            if scrapio_card:
                icons = scrapio_card.query_selector_all('.scrapio-icon-detail')
                for icon in icons:
                    dtype = icon.get_attribute("data-type")
                    durl = icon.get_attribute("data-url")
                    if not dtype or not durl:
                        continue

                    if dtype == "emails":
                        data["email"] = durl.replace("mailto:", "")
                    elif dtype == "phone_international":
                        data["phone"] = durl.replace("tel:", "")
                    elif dtype == "website":
                        data["website"] = durl
                    elif dtype == "contact_pages":
                        data["contact_page"] = durl
                    elif dtype == "facebook":
                        data["facebook"] = durl
                    elif dtype == "instagram":
                        data["instagram"] = durl

                results.append(data)

        except Exception as e:
            print(f"⚠️ Error while processing a shop: {e}")

    return results

def clean_data(df):
    df = df.drop_duplicates(subset="maps_link")

    df = df[
        (df["email"].fillna("").str.strip() != "") |
        (df["phone"].fillna("").str.strip() != "")
    ]

    df = df.fillna("")

    df["has_email"] = df["email"].apply(lambda x: 1 if x.strip() != "" else 0)
    df = df.sort_values(by="has_email", ascending=False).drop(columns=["has_email"])

    return df

def run(extension_path, output_file, start_url):
    with sync_playwright() as p:
        user_data_dir = os.path.abspath("tmp-user-data-dir")
        context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            args=[
                f"--disable-extensions-except={extension_path}",
                f"--load-extension={extension_path}"
            ]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(start_url, timeout=60000)

        data = []
        while True:
            print("✅ Navigate to a page with a list of businesses, wait for Scrap.io icons to load.")
            text = input("Press Enter to scrape all visible businesses (or type STOP to finish)...").strip()
            if text.upper() == "STOP":
                break
            try:
                extracted = extract_from_cards(page)
                data.extend(extracted)
                print(f"→ Found {len(extracted)} business entries.")
            except Exception as e:
                print(f"⚠️ Error: {e}")

        if data:
            df = pd.DataFrame(data)
            df_cleaned = clean_data(df)
            df_cleaned.to_excel(output_file, index=False)
            print(f"\n✅ Cleaned data saved to {output_file}")
        else:
            print("\n No data scraped.")

        context.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape and clean business contact info from Google Maps with Scrap.io")
    parser.add_argument("--extension-path", type=str, required=True, help="Path to the Scrap.io Chrome extension")
    parser.add_argument("--output", type=str, default="output.xlsx", help="Output Excel file name")
    parser.add_argument("--url", type=str, default="https://www.google.com/maps", help="Initial URL to load in browser")

    args = parser.parse_args()
    run(args.extension_path, args.output, args.url)
