# SevaBot – Phase 1: San Francisco Passport Renewal

**KG = Knowledge Graph**: a structured JSON of facts (fees, rules, addresses) crawled from official sources, versioned daily. Think of it as your source of truth so the LLM doesn't hallucinate.

## What's here
- `data/sevabot_sf_kg_phase1.json` – live facts for CGI San Francisco (verified 2026-04-29)
- `src/whatsapp_flow.py` – Flask webhook for WhatsApp Cloud API
- `docs/checklist_template.md` – personalized checklist renderer

## Quick start
1. Set env vars: WHATSAPP_TOKEN, VERIFY_TOKEN, PHONE_NUMBER_ID
2. pip install flask requests
3. python src/whatsapp_flow.py
4. Test: send "passport" to your WhatsApp number

## Sources
- CGI SF General Passport Information
- CGI SF Tatkaal Services
- CGI SF FAQs
- VFS Global USA Passport Services
