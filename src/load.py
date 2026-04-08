# Habitat Picker load.py

"""
Store Habitat_Picker load codes for csv/database
"""

import pandas as pd
import boto3

import pyarrow as pa
import pyarrow.parquet as pq

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


# Upload transformed file S3 bucket as parquet file
def write_parquet_partitioned(df, base_dir: Path, year: int, month: int) -> Path:
    partition_dir = base_dir / f"year={year}" / f"month={month:02d}"
    partition_dir.mkdir(parents=True, exist_ok=True)

    table = pa.Table.from_pandas(df, preserve_index=False)
    output_path = partition_dir / "data.parquet"

    pq.write_table(table, output_path, compression="snappy")

    return output_path

def upload_to_s3(local_path: Path, bucket: str, s3_key: str) -> None:
    s3 = boto3.client("s3")
    s3.upload_file(
        Filename=str(local_path),
        Bucket=bucket,
        Key=s3_key
    )
