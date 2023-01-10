from LoadRawData import LoadRawData
import pandas as pd

# module to preprocess raw data
class PreProcessData:

    def __init__(self, dataframe: pd.DataFrame):
        """Create a connection to a database."""
        self.dataframe = dataframe
        print("testing display of dataframe")
        print(dataframe.tail())

        # pre-processing steps 
        print('Preprocessing stage...')

        

