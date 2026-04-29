"""
Simple crawler for CGI SF – updates fees & processing times
Run daily via GitHub Actions
"""
import requests, json, re
from datetime import datetime
from bs4 import BeautifulSoup

URLS = {
    "general": "https://www.cgisf.gov.in/page/general-passport-information/",
    "tatkal": "https://www.cgisf.gov.in/page/tatkaal-passport-services/",
    "faq": "https://www.cgisf.gov.in/page/faq-s-on-passport/"
}

def fetch():
    kg_path = "data/sevabot_sf_kg_phase1.json"
    with open(kg_path) as f:
        kg = json.load(f)
    
    # Example: scrape processing times
    try:
        r = requests.get(URLS["tatkal"], timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text()
        if "5 working days" in text:
            kg["processing_times"]["source_cgisf"]["tatkal"] = "5 working days from receipt at Consulate"
    except Exception as e:
        print("fetch error", e)
    
    kg["metadata"]["last_verified"] = datetime.utcnow().strftime("%Y-%m-%d")
    
    with open(kg_path, "w") as f:
        json.dump(kg, f, indent=2)
    
    print("KG updated")

if __name__ == "__main__":
    fetch()
