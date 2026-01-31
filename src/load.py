# Habitat Picker load.py

"""
Store Habitat_Picker load codes for csv/database
"""

from pathlib import Path
import pandas as pd


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

