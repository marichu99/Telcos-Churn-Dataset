import pandas as pd
import numpy as np

def newDataSet():
    # import the data set
    df=pd.read_csv("Customer_Churn.csv")
    # print out the first five records to see what the data looks like
    print(df.head())
    # check out the different types of columns in the dataset
    print(df.columns)
    # drop the columns not related to the churn 
    df=df.drop(columns=["customerID","gender","SeniorCitizen","Dependents","tenure"],axis=1)
    print(f"The new columns are {df.columns}")
    output=df.to_csv("task2_1.csv")
    return df

newDataSet()