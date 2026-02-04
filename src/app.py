# Habitat Picker app.py

"""
Store Habitat_Picker main app structure
"""

from pathlib    import Path
from datetime   import datetime

from extract    import extract_ppd_csv
from transform  import transform_ppd
from load       import write_monthly_csv, upload_to_s3

from config     import DATA_RAW_DIR, DATA_TRA_DIR


def main(input_path: Path):
    df_ext = extract_ppd_csv(input_path)
    df_tra = transform_ppd(df_ext)

    year = df_tra["date_of_transfer"].dt.year.iloc[0]
    month = df_tra["date_of_transfer"].dt.month.iloc[0]


    output_path = write_monthly_csv(df_tra, DATA_TRA_DIR, year, month)


    print(f"\nWritten file: {output_path}")

    print("\nDTYPES\n--- --- ---")
    print(df_tra.dtypes)

    print("\nSAMPLE ROWS\n--- --- ---")
    print(df_tra.head())

    bucket = "habitat-picker-s3"
    s3_key = f"ppd/year={year}/month={month:02d}/{output_path.name}"

    upload_to_s3(
        local_path=output_path,
        bucket=bucket,
        s3_key=s3_key
    )

    print(f"Uploaded to s3://{bucket}/{s3_key}")


if __name__ == "__main__":
    main(DATA_RAW_DIR / "ppd-2021.csv")

