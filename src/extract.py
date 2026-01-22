# Habitat Picker extract.py place holder

"""
Store Habitat_Picker extract code for csv file
"""
import pandas as pd

from config import DATA_RAW_DIR


ppd_dir = DATA_RAW_DIR / "sample_data.csv"
ppd_data = pd.read_csv(ppd_dir)


print(ppd_data.head())
