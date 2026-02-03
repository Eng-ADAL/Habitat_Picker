# Habitat Picker extract.py place holder

"""
Store Habitat_Picker extract code for csv file
"""

import pandas as pd
from pathlib    import Path

# pp-monthly.csv columns
PPD_COLUMNS = [
    "transaction_id",
    "price",
    "date_of_transfer",
    "postcode",
    "property_type",
    "new_build_flag",
    "tenure_type",
    "paon",
    "saon",
    "street",
    "locality",
    "town_city",
    "district",
    "county",
    "ppd_category",
    "record_status",
]


def extract_ppd_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        # log
        raise FileNotFoundError(f"PPD source file not found {path}")

    df = pd.read_csv(path, header=None)

    if df.shape[1] != len(PPD_COLUMNS):
        raise ValueError(f"Invalid column count! Expected: {len(PPD_COLUMNS)}, got: {df.shape[1]}")

    df.columns = PPD_COLUMNS
    return df

