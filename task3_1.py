

from task2_4_5 import splittedData
import numpy as np


# import a logistic regression model as customer churn target is a classification problem
from sklearn.linear_model import LogisticRegression
# import some metrics to measure the accuracy of a logstic regression in this scenario
from sklearn.metrics import accuracy_score


def model():
    # import the split data sets from task 2
    x_train,x_test,y_train,y_test=splittedData()
    y_train=y_train.astype("float")
    y_test=y_test.astype("float")
    print("The x train data",x_train) 

    # fit the model using the MultipleLines column
    x_val=x_train["MultipleLines"]

    # transform the series into a 2D array to fit the model
    x_val=np.array(x_val)
    print(f"The values of x_val before reshaping {x_val}")
    x_val=x_val.reshape(len(x_val),1)
    print(f"The values of x_val after reshaping {x_val}")

    # transform the series into a 2D array to fit the model    
    x_test_val=x_test["MultipleLines"]
    x_test_val=np.array(x_test_val)
    x_test_val=x_test_val.reshape(len(x_test_val),1)

    # instantiate the Logistic Regression object
    lr=LogisticRegression(random_state=1)

    # fit the model using the training data
    lr.fit(X=x_val,y=y_train)

    # try predicting the value of the customer churn
    predicted_values=lr.predict(x_test_val)

    # confirm the accuracy of the model
    score=accuracy_score(y_test,predicted_values)

    """
    when the predicted results are 100%, the correlation is perfect
    when the predicted results is greater than 60% and less than 100%, the correlation is good
    when the predicted results is below 60%, the correlation is bad
    """
    print(f"The use of Logistic regression model is {score*100} % accurate in this scenario")


    

model()