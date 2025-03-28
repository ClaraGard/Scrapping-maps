# 🗺️ Scrap Google Maps Business Info with Scrap.io

This guide helps you collect business contact details (emails, phones, websites, etc.) from Google Maps using the **Scrap.io** browser extension and this Python script — no coding skills required!

---

## ✅ What You'll Get

- A spreadsheet (`.xlsx`) with contact info like:
  - Business website
  - Email address
  - Phone number
  - Social links (Facebook, Instagram)
  - Google Maps link

---

## 🔧 What You Need

1. **A computer (Windows, macOS, or Linux)**
2. **Python 3 installed**
3. **Google Chrome or Chromium**
4. **The Scrap.io extension (free)**

---

## 🚀 Step-by-Step Setup

### 1. ✅ Install Python

Go to the official Python website and download the latest version:

🔗 https://www.python.org/downloads/

- During installation, **check the box that says**:  
  `Add Python to PATH`
- Then click **Install Now**

To confirm Python is installed:
- Open your terminal or command prompt
- Type: `python --version`  
  You should see something like `Python 3.11.7`

---

### 2. ✅ Install Required Python Packages

Open your terminal or command prompt and run:

```bash
pip install pandas playwright openpyxl
playwright install
```

This installs the necessary tools for the script to run.

---

### 3. ✅ Install the Scrap.io Extension

Go to the Scrap.io Chrome Web Store page:

🔗 https://chrome.google.com/webstore/detail/scrapio-google-maps-scrap/lhdoppojpmngadmnindnejefpokejbdd

Once installed, you’ll need to find the extension's local path to allow the script to load it.

---

## 🔍 How to Find the Extension Path

1. Open Chrome and go to `chrome://extensions`
2. Enable **Developer Mode** (top right corner)
3. Find **Scrap.io** and click **Details**
4. Copy the **ID** — it looks like:  
   `lhdoppojpmngadmnindnejefpokejbdd`
5. On your computer, go to:

   - **Windows:**
     ```
     C:\Users\<YourName>\AppData\Local\Google\Chrome\User Data\Default\Extensions
     ```
   - **macOS:**
     ```
     ~/Library/Application Support/Google/Chrome/Default/Extensions
     ```
   - **Linux:**
     ```
     ~/.config/google-chrome/Default/Extensions
     ```

6. Open the folder matching the extension ID.
7. Inside, open the most recent version folder (like `1.6.4_0`)
8. Copy the full path — this is your `--extension-path`.

---

## 🏃 How to Run the Script

1. Download or copy the script and save it as `scrape_maps.py`

2. In a terminal or command prompt, navigate to the folder where the script is saved.

3. Run the script using:

```bash
python scrape_maps.py --extension-path "FULL_PATH_TO_SCRAPIO" --output "my_data.xlsx"
```

Example (on Windows):

```bash
python scrape_maps.py --extension-path "C:\Users\Clara\AppData\Local\Google\Chrome\User Data\Default\Extensions\lhdoppojpmngadmnindnejefpokejbdd\1.6.4_0" --output "paris_restaurants.xlsx"
```

---

## 🔍 Scraping Instructions

Once the script runs:

1. A Chrome browser will open with Google Maps
2. Search for a type of business, like **“Florists in Marseille”**
3. Wait for the Scrap.io icons to appear
4. Go back to the terminal and press **Enter**  
   → This scrapes all visible businesses
5. Scroll down in Maps to load more businesses
6. Press **Enter** again to scrape the new ones
7. Repeat as needed
8. Type `STOP` and press **Enter** to finish

The script will clean the data and save it to your Excel file.

---

## 📂 Output Example

| maps_link | email             | phone       | website           | contact_page       | facebook             | instagram             |
|-----------|------------------|-------------|-------------------|--------------------|----------------------|-----------------------|
| https://... | info@domain.com | +33612345678 | www.example.com   | /contact           | fb.com/yourbiz       | instagram.com/yourbiz |

---

## ❓ Troubleshooting

- **Nothing scraped?**  
  → Make sure Scrap.io icons are loaded on the map page before pressing Enter

- **Extension not working?**  
  → Double-check the extension path — it must include the version folder

- **Playwright errors?**  
  → Run `playwright install` again

- **"Permission denied"?**  
  → Try running the terminal as Administrator

---

## 💡 Tips

- Use more specific search terms for better targeting  
  (e.g., `"photographers in Lyon"` instead of just `"photographers"`)

- Zoom in/out on the map if results aren’t loading

- Wait a few seconds after scrolling before scraping again

---

## 🧼 What the Script Does

- Opens Chrome with the Scrap.io extension
- Lets you manually browse Google Maps
- Collects contact info from visible business listings
- Cleans the data (removes duplicates, keeps only useful lines)
- Saves it to Excel

---

## 🛠 Want to Customize?

If you’re more technical, you can:
- Add more social links or business fields
- Save to `.csv` instead of `.xlsx`
- Combine this with email campaigns or CRMs

---

## 📞 Need Help?

Open an issue or contact the author if you’re stuck or want to contribute to the project.

---
