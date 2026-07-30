import requests
from io import StringIO
import os
try:
    import pandas as pd
except Exception:
    pd = None

from src.config import URL


def extract_data():
    """
    Download CSV from URL and return a pandas.DataFrame (if pandas available),
    or a list of dicts / empty list on failure. If the network fetch fails,
    fall back to a bundled sample CSV (data/sample.csv) so CI/tests don't rely
    on external network resources.
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
            raise RuntimeError("no CSV content")
        headers = [h.strip() for h in lines[0].split(",")]
        records = []
        for row in lines[1:]:
            values = [v.strip() for v in row.split(",")]
            records.append(dict(zip(headers, values)))
        return records
    except Exception:
        # Try bundled sample CSV next (use repo working dir 'data/sample.csv')
        sample_path = os.path.join(os.getcwd(), "data", "sample.csv")
        if pd is not None and os.path.exists(sample_path):
            try:
                return pd.read_csv(sample_path)
            except Exception:
                pass
        # Final fallback: return empty list or None-like structure
        if pd is not None:
            # return an empty DataFrame so callers expecting DataFrame won't crash
            return pd.DataFrame()
        return []
