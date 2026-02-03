# Habitat Picker app.py place holder

"""
Store Habitat_Picker main app structure
"""

from pathlib    import Path

from extract    import extract_ppd_csv
from config     import DATA_RAW_DIR

def main(input_path: Path):
    df = extract_ppd_csv(input_path)
    # df = transform...
    print(df.head())

if __name__ == "__main__":
    main(DATA_RAW_DIR / "sample_data.csv")

