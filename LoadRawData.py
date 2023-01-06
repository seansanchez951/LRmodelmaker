import os
import pandas as pd
from pathlib import Path

# module to load raw data
class LoadRawData:

    # global variable
    global raw_ds

    def __init__(self) -> None:
        # start with greeting
        print("Welcome to the Linear Regression Model Maker!\nWe'll start with loading in the raw data\nPlease load a csv, xml, json, or txt file only")
        # user input path to file
        file_path = input("Enter file path here: ")
        file_path = file_path.replace('"', '')
        # apply Path wrapper
        path_wrapped = Path(file_path)
        ext = path_wrapped.suffix
        print("file suffix is: ", ext)

        # validate and load file type to pandas df
        if ext == '.csv':
            print("loading csv file...")
            raw_ds = pd.read_csv(file_path)
        elif ext == '.xml':
            print("loading xml file...")
            raw_ds = pd.read_xml(file_path)
        elif ext == '.json':
            print('loading json file...')
            raw_ds = pd.read_json(file_path)
        elif ext == '.txt':
            print('loading txt file...')
            raw_ds = pd.read_csv(file_path)
        else:
            print("Invalid or file not supported!")

        print('sample of data set')
        print(raw_ds.head())

    

if __name__=="__main__":
    print("Calling main...")
    loadStart = LoadRawData()
    loadStart
    
    


