# Configuration file for Habitat_Picker ../src/config.py
"""
This file contains habitat picker configurations
"""


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_RAW_DIR = BASE_DIR / "data_raw"
DATA_EXT_DIR = BASE_DIR / "data_extracted"
DATA_TRA_DIR = BASE_DIR / "data_transformed"
