from task2_3 import binarizeDataset
import pandas as pd 
from sklearn.model_selection import train_test_split

def splittedData():
    # get the binarized dataset

    df= pd.DataFrame(binarizeDataset())
    # select all columns that are not "Churn" and set it as the independent variable
    independent=df.loc[:,df.columns!="Churn"]

    # select the churn and set it as dependent
    dependent=df["Churn"]
    # split the training and testing data from the dataset in a ratio of 2:1

    x_train,y_train,x_test,y_test=train_test_split(independent,dependent,train_size=0.6667,test_size=0.3333,random_state=0) 
    print(len(x_train))
    print(len(y_train))
    print(len(x_test))
    print(len(y_test))
    
    output=x_train.to_csv("task2_4_5_1.csv")
    y_train.to_csv("task2_4_5_2.csv")
    x_test.to_csv("task2_4_5_3.csv")
    y_test.to_csv("task2_4_5_4.csv")
    return x_train,y_train,x_test,y_test

    
splittedData() 