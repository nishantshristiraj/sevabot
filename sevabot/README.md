# SevaBot – Indian Passport Renewal Assistant

**KG = Knowledge Graph**: versioned JSON of official rules (fees, docs, timelines) from CGI + VFS. The LLM never guesses – it reads the KG.

## Phases
- **Phase 1 – SF MVP** ✅: SF knowledge graph + WhatsApp 3-question flow
- **Phase 2 – All-US Coverage**: router for NY, Chicago, Houston, Atlanta, DC, SF
- **Phase 3 – Live Crawler**: daily scrape of cgisf.gov.in, vfsglobal, auto-diff alerts
- **Phase 4 – Personalizer**: auto-generate Annexure E/D, photo validator, checklist
- **Phase 5 – Web**: shareable checklist links, status tracker
- **Phase 6 – Proactive**: expiry reminders via WhatsApp

## Quick start (Phase 1)
```bash
pip install -r requirements.txt
export WHATSAPP_TOKEN=xxx PHONE_NUMBER_ID=xxx
python src/whatsapp_flow.py
```

See `docs/roadmap.md` for full plan.
