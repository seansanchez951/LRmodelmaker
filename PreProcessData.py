from LoadRawData import LoadRawData
import pandas as pd
import sklearn as sk
import sklearn.linear_model
from sklearn.preprocessing import OneHotEncoder


# module to preprocess raw data
class PreProcessData:

    def __init__(self, dataframe: pd.DataFrame, x, y, k, user_response_target):

        self.x = x
        self.y = y
        self.k = k
        self.user_response_target = user_response_target

        """Create a connection to a database."""
        self.dataframe = dataframe

        # pre-processing steps
        print('Preprocessing stage...')

        # quick info of dataframe
        print("General dataframe information")
        dataframe.info()

        print('Checking for missing values...')
        nan_count = dataframe.isna().sum().sum()

        if nan_count > 0:
            print('NaN values found in dataframe')
            print('Removing rows with NaN values...')
            dataframe = dataframe.dropna()
        else:
            print('No NaN values found')

        # checking for numerical and categorical data column
        print('Checking for numerical and categorical data types...')
        column_names = dataframe.columns
        column_dtypes = [dataframe[x].dtype for x in column_names]
        column_dictionary = dict(zip(column_names, column_dtypes))

        # possible data types in a pandas dataframe
        categorical = ['category', 'bool', 'object']
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

        # accumulators for categorical and numerical data types
        numerical_datatype_count = 0
        categorical_datatype_count = 0

        for i in column_dictionary:
            if column_dictionary.get(i) in categorical:
                categorical_datatype_count += 1
            elif column_dictionary.get(i) in numerics:
                numerical_datatype_count += 1

        print("Number of columns with numerical data types: ", numerical_datatype_count)
        print("Number of columns with categorical data types: ", categorical_datatype_count)

        user_flag = True
        while user_flag:
            # user has to decide the target variable y
            print("Please choose a target variable (y) from the list below.")
            print(column_names)
            user_response_target = input("Enter target variable here: ")

            # check to make sure user response is in the list
            if user_response_target not in column_names:
                print("response " + user_response_target + " is not in list! Please enter a valid column name.")
            else:
                print("response " + user_response_target + " is valid.")
                user_flag = False

        # target y has been chosen by user
        y = pd.DataFrame(dataframe[user_response_target].copy())
        print("Target Variable...")
        print(y.head())

        # the remaining columns will be put in the data matrix X
        X = dataframe.drop(user_response_target, axis=1)

        print("Data Matrix...")
        print(X.head())
        print(X.info())

        # now that we have our data matrix and target we need to split
        # the data into training and  sets
        X_train, X_val, y_train, y_val = sk.model_selection.train_test_split(X, y, test_size=0.33, random_state=42)

        # shapes for the split data
        print("Shape of X_train is: ", X_train.shape)
        print("Shape of y_train is: ", y_train.shape)
        print("Shape of X_val is: ", X_val.shape)
        print("Shape of y_val is: ", y_val.shape)

        # now that the target variable has been identified we need to encode any categorical data types in X
        # into a numerical data type for analysis and model training
        # extract out the categorical columns

        # x_cat selects categorical data from x dataframe
        x_cat = X.select_dtypes('object')

        # oneHotEncoder provided by scikit learn, ohe is a one hot encoder object
        ohe = OneHotEncoder()
        ohe.fit(x_cat)

        # apply feature names to categorical columns
        feature_names = ohe.get_feature_names_out(x_cat.columns)

        # this function does one hot encoding
        def encode_categorical_columns(x_matrix, ohe_object, feature_names_col):
            # x is a pandas dataframe
            # ohe is an sklearn OneHotEncoder object.

            # extract out the numeric columns
            x_numeric = x_matrix.select_dtypes(exclude='object')

            # extract out the categorical columns
            X_cat = x_matrix.select_dtypes('object')

            # asking the ohe object to do one hot encoding on the categorical columns
            encoded_columns = ohe_object.transform(X_cat).toarray()
            encoded_columns = pd.DataFrame(encoded_columns, columns=feature_names_col)

            # recombining the numeric columns with the ohe columns
            return pd.concat([x_numeric, encoded_columns], axis=1)

        X_train = encode_categorical_columns(X_train, ohe, feature_names)
        # X_test = encode_categorical_columns(X_test, ohe, feature_names)
