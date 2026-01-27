# Habitat Picker app.py place holder

"""
Store Habitat_Picker main app structure
"""

from extract import extract_ppd_csv

def main():
    df = extract_ppd_csv()
    print(df.head())

if __name__ == "__main__":
    main()

