import pandas as pd
import os

from src.load import save_csv

def test_save_csv():
    df = pd.DataFrame({
        "Bank": ["ABC"],
        "MC_USD_Billion": [100]
    })

    save_csv(df, "test.csv")

    assert os.path.exists("test.csv")

    os.remove("test.csv")
