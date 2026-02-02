# Habitat Picker load.py

"""
Store Habitat_Picker load codes for csv/database
"""

import pandas as pd
import boto3

from pathlib import Path
from botocore.exceptions import ClientError

# save transformed ppd data to csv file
def write_monthly_csv(
    df: pd.DataFrame,
    output_dir: Path,
    year: int,
    month: int
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{year}-{month:02d}.csv"
    output_path = output_dir / filename

    df.to_csv(output_path, index=False)

    return output_path


# upload csv file to s3 bucket
def upload_to_s3(
    local_path: Path,
    bucket: str,
    s3_key: str
) -> None:
    s3 = boto3.client("s3")
    s3.upload_file(
        Filename=str(local_path),
        Bucket=bucket,
        Key=s3_key
    )
