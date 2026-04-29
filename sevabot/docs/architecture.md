# Architecture

User → WhatsApp → Flask webhook → KG lookup → Response
                                      ↓
                              Crawler (daily) → updates KG JSON → git commit

Data stays in JSON, no DB needed for Phase 1-3.
