"""
Phase 5: Flask web for shareable checklists
"""
from flask import Flask, render_template_string
import json

app = Flask(__name__)
with open('data/sevabot_sf_kg_phase1.json') as f:
    KG = json.load(f)

@app.route('/checklist/<zip_code>')
def checklist(zip_code):
    html = f"<h1>SevaBot SF Checklist</h1><p>Fee: ${KG['fees_usd']['regular']['adult_10yr_36pg']['total']}</p>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
