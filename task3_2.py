import pandas as pd 
import numpy as np
from task2_4_5 import splittedData
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def model():
    # import the split data sets from task 2
    x_train,x_test,y_train,y_test=splittedData()
    # get the predictor column
    
    val_x=x_train["TotalCharges"].astype(float)
    x_train=np.array(val_x)
    x_train=x_train.reshape(len(x_train),1)
    
    x_test_val=np.array(x_test["TotalCharges"])
    x_test_val=x_test_val.reshape(len(x_test_val),1)

    # instantiate the logistic regression object
    lr=LogisticRegression(random_state=1)

    # fit the data points to the model
    lr.fit(X=x_train,y=y_train)

    # predict the values
    predicted_values=lr.predict(x_test_val)

    # get the accuracy score
    score=accuracy_score(y_test,predicted_values)

    print(f"The use of Logistic regression model is {score*100} % accurate in this scenario")

    
    # find the probability and the odds
    def oddsProb(logR,x):
        odds=logR.coef_
        log_odd=np.exp(odds)
        print(f"With an increase in one dollar in total charges the customer is {log_odd} times likely to churn")
        # probability
        log_oddz=odds*x+logR.intercept_

        odd_prob=np.exp(log_oddz)
        probability=odd_prob/(1+odd_prob)
        print(probability)
    oddsProb(lr,x_train)



model()