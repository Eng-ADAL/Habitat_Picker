# Habitat Picker transform.py

"""
Store Habitat_Picker transform code for extracted paid price csv files
"""

import pandas as pd
import numpy as np


# Normalising ID's (remove {} and capitalise)
def normalise_ids(df: pd.DataFrame) -> pd.DataFrame:
    df["transaction_id"] = (
            df["transaction_id"].str.strip("{}")
            .str.upper()
            )
    return df

# Normalise data types
def normalise_types(df: pd.DataFrame) -> pd.DataFrame:
    df["price"] = df["price"].astype("int64")
    df["date_of_transfer"] = pd.to_datetime(df["date_of_transfer"], errors="raise")
    return df

STRING_COLS = [
            "postcode", "paon", "saon", "street",
            "locality", "town_city", "district", "county"
            ]

# Normalise string (string cleaning)
def clean_strings(df: pd.DataFrame) -> pd.DataFrame:
    for col in STRING_COLS:
        df[col] = (
            df[col]
            .astype("string")
            .str.strip()
            .replace("", pd.NA)
        )
    return df

# Flag stndardisation (converting Y:Yes, N:No to boolean Y:True, N:False)
def standardise_flags(df: pd.DataFrame) -> pd.DataFrame:
    df["new_build_flag"] = df["new_build_flag"].map({"Y": True, "N": False})
    return df

# Enforce schema expected
EXPECTED_SCHEMA = {
    "transaction_id": "string",
    "price": "int64",
    "date_of_transfer": "datetime64[ns]",
    "postcode": "string",
    "property_type": "string",
    "new_build_flag": "boolean",
    "tenure_type": "string",
    "paon": "string",
    "saon": "string",
    "street": "string",
    "locality": "string",
    "town_city": "string",
    "district": "string",
    "county": "string",
    "ppd_category": "string",
    "record_status": "string",
}

def enforce_schema(df):
    for col, dtype in EXPECTED_SCHEMA.items():
        df[col] = df[col].astype(dtype)
    return df


# Collection of transform functions
def transform_ppd(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = normalise_ids(df)
    df = normalise_types(df)
    df = clean_strings(df)
    df = standardise_flags(df)
    df = enforce_schema(df)

    return df
