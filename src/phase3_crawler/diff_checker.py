"""
Compare new crawl vs last KG, alert on fee/time changes
"""
import json

def diff():
    with open('data/sevabot_sf_kg_phase1.json') as f:
        old = json.load(f)
    # placeholder: in production parse HTML and compare old['fees_usd']
    print("No changes detected – implement HTML parsing next")
