# Habitat Picker extract.py place holder

"""
Store Habitat_Picker extract code for csv file
"""

import pandas as pd
from config import DATA_RAW_DIR

def extract_ppd_csv(filename: str = "sample_data.csv") -> pd.DataFrame:
    path = DATA_RAW_DIR / filename
    return pd.read_csv(path)

