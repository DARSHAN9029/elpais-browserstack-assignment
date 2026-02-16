# El País Opinion Scraper – BrowserStack Assignment

## Overview

This project automates the following workflow:

- Navigate to El País Opinion section
- Scrape first 5 opinion articles
- Extract:
  - Article Title (Spanish)
  - Article Content (Spanish)
  - Cover Image (if available)
- Translate titles to English using Rapid Translate API
- Perform text frequency analysis on translated headers
- Execute cross-browser parallel testing on BrowserStack (5 environments)

---

## Tech Stack

- Python (base language)
- Selenium
- BeautifulSoup
- RapidAPI (Translation)
- BrowserStack Automate SDK

---

## How to Run Locally

```bash
pip install -r requirements.txt
python main.py
```
---

## Run on BrowserStack (Parallel Execution) 

```bash
browserstack-sdk python main.py
```