"""
Phase 6: Proactive expiry reminders
Store users in SQLite, send WhatsApp at T-9 months, T-6 months
"""
import sqlite3, datetime

def init_db():
    conn = sqlite3.connect('data/users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (phone TEXT, expiry DATE)')
    conn.commit()

def check_reminders():
    # TODO: query and send via WhatsApp API
    pass
