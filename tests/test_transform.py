import pandas as pd
from src.transform import transform_data

def test_transform_data():
    df = pd.DataFrame({
        "Bank": ["ABC"],
        "MC_USD_Billion": [100]
    })

    result = transform_data(df)

    assert "MC_GBP_Billion" in result.columns
