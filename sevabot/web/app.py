from flask import Flask, request, render_template_string
import json

app = Flask(__name__)

with open('data/sevabot_sf_kg_phase1.json') as f:
    KG = json.load(f)

TEMPLATE = """
<!doctype html>
<html>
<head><title>SevaBot SF Checklist</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{font-family:system-ui;padding:24px;max-width:600px;margin:auto}h1{font-size:22px}li{margin:6px 0}.fee{font-size:28px;font-weight:700}</style>
</head>
<body>
<h1>Passport Renewal – San Francisco</h1>
<p>Verified: {{kg.metadata.last_verified}}</p>
<div class="fee">${{fee}} – {{service}}</div>
<p><b>Processing:</b> {{time}}</p>
<p><b>Submit to:</b> {{addr}}</p>
<h3>Documents</h3>
<ul>{% for d in docs %}<li>{{d}}</li>{% endfor %}</ul>
<p><a href="https://visa.vfsglobal.com/usa/en/ind/apply-passport">Start VFS application →</a></p>
</body></html>
"""

@app.route("/checklist")
def checklist():
    tatkal = request.args.get("tatkal","0")=="1"
    fee = KG['fees_usd']['tatkal' if tatkal else 'regular']['adult_10yr_36pg']['total']
    time = KG['processing_times']['source_cgisf']['tatkal' if tatkal else 'normal']
    return render_template_string(TEMPLATE,
        kg=KG, fee=fee, service="Tatkal" if tatkal else "Normal",
        time=time,
        addr=KG['jurisdiction']['vfs_center']['address'],
        docs=KG['document_checklist_adult_renewal']['mandatory']
    )

if __name__ == "__main__":
    app.run(port=8000)
