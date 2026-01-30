# Habitat Picker transform.py place holder

"""
Store Habitat_Picker transform code
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

# Collection of transform functions
def transform_ppd(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = normalise_ids(df)
    df = normalise_types(df)
    df = clean_strings(df)
    df = standardise_flags(df)

    return df
