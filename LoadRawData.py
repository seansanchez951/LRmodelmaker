import os
import pandas as pd
from pathlib import Path


# module to load raw data
class LoadRawData:

    raw_ds = None

    def __init__(self) -> None:
        # start with greeting
        print(
            "Welcome to the Linear Regression Model Maker!\nWe'll start with loading in the raw data\nPlease load a "
            "csv, xml, json, or txt file only")

        user_flag = True
        while user_flag:
            # user input path to file
            file_path = input("Enter file path here: ")
            # remove double quotes from path
            file_path = file_path.replace('"', '')
            # apply Path wrapper
            path_wrapped = Path(file_path)
            ext = path_wrapped.suffix
            print("file suffix is: ", ext)

            # validate and load file type to pandas df
            # note: need to cover when input has valid suffix but is an invalid path or file name
            if ext == '.csv':
                print("loading csv file...")
                LoadRawData.raw_ds = pd.read_csv(file_path)
                print('sample of raw data set...')
                print(LoadRawData.raw_ds.head())
                user_flag = False
            elif ext == '.xml':
                print("loading xml file...")
                LoadRawData.raw_ds = pd.read_xml(file_path)
                print('sample of raw data set...')
                print(LoadRawData.raw_ds.head())
                user_flag = False
            elif ext == '.json':
                print('loading json file...')
                LoadRawData.raw_ds = pd.read_json(file_path)
                print('sample of raw data set...')
                print(LoadRawData.raw_ds.head())
                user_flag = False
            elif ext == '.txt':
                print('loading txt file...')
                LoadRawData.raw_ds = pd.read_csv(file_path)
                print('sample of raw data set...')
                print(LoadRawData.raw_ds.head())
                user_flag = False
            else:
                print("Invalid or file not supported!")

# if __name__=="__main__":
#   print("Calling LoadRawData.py main...")
#   loadStart = LoadRawData()
#   loadStart
