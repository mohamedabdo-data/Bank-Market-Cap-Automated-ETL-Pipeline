import os
try:
    import pandas as pd
except Exception:
    pd = None

from config import CSV_FILE_NAME
from database import insert_data


def save_csv(df):
    """Save DataFrame or list/dict to CSV_FILE_NAME."""
    dirpath = os.path.dirname(CSV_FILE_NAME)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    if pd is not None and isinstance(df, pd.DataFrame):
        df.to_csv(CSV_FILE_NAME, index=False)
        return

    # Convert list/dict to CSV via pandas if available
    if pd is not None:
        df2 = pd.DataFrame(df)
        df2.to_csv(CSV_FILE_NAME, index=False)
        return

    # Fallback: write an empty CSV file to ensure file exists
    with open(CSV_FILE_NAME, "w", encoding="utf-8") as f:
        f.write("")
