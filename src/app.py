# Habitat Picker app.py place holder

"""
Store Habitat_Picker main app structure
"""

from pathlib    import Path

from extract    import extract_ppd_csv
from transform  import transform_ppd
from config     import DATA_RAW_DIR

def main(input_path: Path):
    df_ext = extract_ppd_csv(input_path)
    df_tra = transform_ppd(df_ext)

    print("\nDTYPES\n--- --- ---")
    print(df_tra.dtypes)

    print("\nSAMPLE ROWS\n--- --- ---")
    print(df_tra.head())

if __name__ == "__main__":
    main(DATA_RAW_DIR / "sample_data.csv")

