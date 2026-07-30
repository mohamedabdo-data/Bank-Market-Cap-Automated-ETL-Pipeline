import sqlite3

def create_database():
    conn = sqlite3.connect("data/bank_market_cap.db")
    conn.close()
