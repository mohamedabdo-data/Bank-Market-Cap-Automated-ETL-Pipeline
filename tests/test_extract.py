import pandas as pd
from src.extract import extract_data


def test_extract_data():
    df = extract_data()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
