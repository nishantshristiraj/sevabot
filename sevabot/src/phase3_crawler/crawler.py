"""
Phase 3: Daily crawler for CGI + VFS
Run via GitHub Actions at 6am PT
"""
import requests, json, datetime

URLS = {
  "sf_tatkal": "https://www.cgisf.gov.in/page/tatkaal-passport-services/",
  "sf_fees": "https://services.vfsglobal.com/one-pager/india/united-states-of-america/passport-services/"
}

def crawl():
    data = {"timestamp": datetime.datetime.utcnow().isoformat()}
    for key, url in URLS.items():
        r = requests.get(url, timeout=20)
        data[key] = {"status": r.status_code, "length": len(r.text)}
    with open('data/crawl_latest.json','w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    crawl()
