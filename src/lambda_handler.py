# Habitat Picker lambda_handler.py

"""
Store Habitat_Picker lambda codes for AWS cloud integration
"""

from pathlib import Path
import tempfile
import boto3

from extract import extract_ppd_csv
from transform import transform_ppd
from load import upload_to_s3


def handler(event, context):
    """
    AWS Lambda entry point
    event example:
    {
        "bucket": "habitat-picker-s3",
        "key": "raw/ppd-2021.csv"
    }
    """

    bucket = event["bucket"]
    key = event["key"]

    # safety check: only process raw inputs
    if not key.startswith("raw/"):
        raise ValueError("Lambda should only process raw inputs")


    s3 = boto3.client("s3")

    # Lambda only allows writing to /tmp
    tmp_dir = Path(tempfile.gettempdir())
    local_input = tmp_dir / "input.csv"
    local_output = tmp_dir / "output.csv"

    # Download raw file
    s3.download_file(bucket, key, str(local_input))

    # Run your existing ETL logic
    df_ext = extract_ppd_csv(local_input)
    df_tra = transform_ppd(df_ext)

    year = df_tra["date_of_transfer"].dt.year.iloc[0]
    month = df_tra["date_of_transfer"].dt.month.iloc[0]

    df_tra.to_csv(local_output, index=False)

    # Upload curated output
    output_key = f"curated/year={year}/month={month:02d}/data.csv"
    upload_to_s3(local_output, bucket, output_key)

    return {"status": "ok", "output": output_key}

