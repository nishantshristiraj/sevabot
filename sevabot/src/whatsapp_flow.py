"""
SevaBot WhatsApp Flow – Phase 1 SF
3-question flow → personalized checklist
"""
import json, os
from flask import Flask, request
import requests

app = Flask(__name__)

# Load KG
with open('data/sevabot_sf_kg_phase1.json') as f:
    KG = json.load(f)

SESSIONS = {}

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "sevabot123")

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "error", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    try:
        msg = data['entry'][0]['changes'][0]['value']['messages'][0]
        from_id = msg['from']
        text = msg['text']['body'].strip().lower()
    except:
        return "ok"

    session = SESSIONS.get(from_id, {"step":0})
    
    if text in ["hi","passport","start"] or session["step"]==0:
        session = {"step":1}
        reply = "Namaste! SevaBot SF here. I'll build your passport renewal checklist.\nQ1: What's your US zip code?"
    elif session["step"]==1:
        session["zip"] = text
        # simple jurisdiction check
        session["step"]=2
        reply = "Q2: Normal or Tatkal? (tatkal = 5 days, $246)"
    elif session["step"]==2:
        session["tatkal"] = "tatkal" in text
        session["step"]=3
        reply = "Q3: Any name/DOB/place change? yes/no"
    elif session["step"]==3:
        session["change"] = "yes" in text
        session["step"]=4
        # generate checklist
        reply = build_checklist(session)
        session = {"step":0}  # reset
    else:
        reply = "Type 'passport' to start again."

    SESSIONS[from_id] = session
    send_whatsapp(from_id, reply)
    return "ok"

def build_checklist(s):
    kg = KG
    fee = kg['fees_usd']['tatkal' if s['tatkal'] else 'regular']['adult_10yr_36pg']['total']
    time = kg['processing_times']['source_cgisf']['tatkal' if s['tatkal'] else 'normal']
    addr = kg['jurisdiction']['vfs_center']['address']
    
    not_eligible = s['tatkal'] and s['change']
    
    checklist = f"""*SevaBot SF – Passport Renewal Checklist*
Verified: {kg['metadata']['last_verified']}

• Jurisdiction: CGI San Francisco
• Service: {'Tatkal' if s['tatkal'] else 'Normal'}
• Fee: ${fee} (pay by cashier check to 'VFS Services (USA) Inc')
• Processing: {time} (after PVR clear)
• Submit to: {addr}

*Documents (Adult)*
1. Printed govt application (embassy.passportindia.gov.in)
2. Printed VFS application
3. Original current passport
4. Copy of H1B/F1/GC/I-797
5. US address proof (DL/utility <3mo)
6. Annexure E (self-declaration)
7. 2x2" photo – white background

{'⚠️ NOT eligible for Tatkal with major changes per CGI SF. Use Normal.' if not_eligible else ''}

Next: https://visa.vfsglobal.com/usa/en/ind/apply-passport
"""
    return checklist

def send_whatsapp(to, text):
    token = os.getenv("WHATSAPP_TOKEN")
    phone_id = os.getenv("PHONE_NUMBER_ID")
    if not token: 
        print("Would send:", text)
        return
    url = f"https://graph.facebook.com/v19.0/{phone_id}/messages"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"messaging_product":"whatsapp","to":to,"text":{"body":text}}
    requests.post(url, json=payload, headers=headers)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
