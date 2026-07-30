import sqlite3
import os

DB_PATH = "data/bank_market_cap.db"

def create_database():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS Largest_banks (
        Name TEXT,
        MC_USD_Billion REAL,
        MC_GBP_Billion REAL,
        MC_EUR_Billion REAL,
        MC_INR_Billion REAL
    )
    """)
    conn.commit()
    conn.close()


def insert_data(df):
    """Insert records into the Largest_banks table.

    Accepts a pandas.DataFrame, a list of dicts, a single dict, or an empty list.
    """
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    records = []
    try:
        import pandas as pd
    except Exception:
        pd = None

    if pd is not None and isinstance(df, pd.DataFrame):
        records = df.to_dict(orient="records")
    elif isinstance(df, list):
        records = df
    elif isinstance(df, dict):
        records = [df]
    else:
        # nothing to insert or unsupported type
        conn.close()
        return

    for r in records:
        cursor.execute(
            """
            INSERT INTO Largest_banks (Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                r.get("Name"),
                r.get("MC_USD_Billion"),
                r.get("MC_GBP_Billion"),
                r.get("MC_EUR_Billion"),
                r.get("MC_INR_Billion"),
            ),
        )

    conn.commit()
    conn.close()
