import os

# CSV output path (default placed under data/ to keep repo root clean)
CSV_FILE_NAME = os.getenv("CSV_FILE_NAME", "data/bank_market_cap.csv")

# Source data URL - prefer setting BANK_DATA_URL in GitHub Actions secrets or repo secrets
URL = os.getenv("BANK_DATA_URL", "https://example.com/data-source.csv")
