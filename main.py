from LoadRawData import LoadRawData
from PreProcessData import PreProcessData
import pandas as pd

if __name__ == "__main__":
    print("Calling main.py...")
    # starting program
    LoadRawData()
    # send raw data to preprocess class
    PreProcessData(LoadRawData.raw_ds, x=None, y=None, k=None, user_response_target=None)
