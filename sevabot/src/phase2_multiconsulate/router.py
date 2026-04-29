"""
Phase 2: Route user by zip to correct consulate KG
"""
import json

with open('data/consulates.json') as f:
    CONSULATES = json.load(f)

ZIP_TO_STATE = {"94404":"CA-N"}  # expand with real mapping

def get_consulate(zip_code):
    state = ZIP_TO_STATE.get(zip_code, "CA-N")
    for name, data in CONSULATES.items():
        if state in data["states"]:
            return name, data
    return "san_francisco", CONSULATES["san_francisco"]
