import os
try:
    import pandas as pd
except Exception:
    pd = None

from src.config import CSV_FILE_NAME
from src.database import insert_data


def save_csv(df, file_path=None):
    """Save DataFrame or list/dict to CSV file.

    If file_path is provided it will be used, otherwise CSV_FILE_NAME from
    config is used. Returns the path written.
    """
    path = file_path or CSV_FILE_NAME
    dirpath = os.path.dirname(path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    if pd is not None and isinstance(df, pd.DataFrame):
        df.to_csv(path, index=False)
        return path

    # Convert list/dict to CSV via pandas if available
    if pd is not None:
        df2 = pd.DataFrame(df)
        df2.to_csv(path, index=False)
        return path

    # Fallback: write an empty CSV file to ensure file exists
    with open(path, "w", encoding="utf-8") as f:
        f.write("")
    return path
