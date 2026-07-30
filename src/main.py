from src.extract import extract_data
from src.transform import transform_data
from src.load import save_csv
from src.database import create_database
from src.logger import log_info
from src.config import CSV_FILE_NAME


def main():
    log_info("Starting ETL")
    create_database()
    df = extract_data()
    if df is None:
        log_info("No data extracted")
        return
    df2 = transform_data(df)
    save_csv(df2, CSV_FILE_NAME)
    log_info("ETL finished")
