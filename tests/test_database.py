import os
from src.database import create_database

def test_database_creation():
    create_database()

    assert os.path.exists("data/bank_market_cap.db")
