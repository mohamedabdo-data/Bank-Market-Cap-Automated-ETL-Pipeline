import requests
from io import StringIO
try:
    import pandas as pd
except Exception:
    pd = None

from config import URL


def extract_data():
    """
    Download CSV from URL and return a pandas.DataFrame (if pandas available),
    or a list of dicts / empty list on failure.
    """
    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        text = resp.text
        if pd is not None:
            df = pd.read_csv(StringIO(text))
            return df
        # fallback: parse CSV minimally into list of dicts
        lines = [l for l in text.splitlines() if l.strip()]
        if not lines:
            return []
        headers = [h.strip() for h in lines[0].split(",")]
        records = []
        for row in lines[1:]:
            values = [v.strip() for v in row.split(",")]
            records.append(dict(zip(headers, values)))
        return records
    except Exception:
        # On any error, return empty list (ETL will log "no data" rather than crash)
        return []
