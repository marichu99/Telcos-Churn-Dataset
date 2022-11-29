from task2_1 import newDataSet
import pandas as pd
import numpy as np


def dropNulls():
    df=pd.DataFrame(newDataSet())
    print(df)
    df.replace(" ",np.nan, inplace=True)
    
    # print(df["InternetService"].isna() == False)
    # check which columns have null values
    for group in df.columns:    
        print(f"The {group} column has {df[group].isna().sum()} null values")
    # drop the columns with null values
    
    df.dropna(axis=0,inplace=True)
    output=df.to_csv("task2_2.csv")
    

    return df
dropNulls()