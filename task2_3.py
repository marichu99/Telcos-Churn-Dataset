from task2_2 import dropNulls
import pandas as pd
import numpy as np


def binarizeDataset():
    df= pd.DataFrame(dropNulls())
    print(df.columns)
    
    for group in df.columns:
        # check which columns have categorical values yes or no
        binary_unique= int(df[group].nunique())
        if binary_unique == 2:
            
            print(f"the group is {group}")
            print(df[group].unique())
            # change the change the yes and no columns into 1 and Zero
            df[group].replace(["Yes","No"],[1,0],inplace=True)
            # binarize the multipleLines column as it is needed in task 3
            
            df["TotalCharges"].astype(float)
            print(df[group])
            print(df.head())
            output=df.to_csv("task2_3.csv")
            df.MultipleLines.replace(["Yes","No","No phone service"],[1,0,2],inplace=True)
            
    return df
        


binarizeDataset()