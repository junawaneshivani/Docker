#####################################
# Linear Regression in one variable #
#####################################

# Normal Equation          --> directly gives theta values no need for alpha
####################
# ( X'*X )-1 *X'*y #
####################

# Input for the algorithm --> data.csv, no of hours spent studying VS grade


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import sys



def plot_graph(plt, X, y) -> None:
    """
    Input:  X, y
    Output: points on graph
    """
    plt.scatter(X, y, color="green")


def plot_line(plt, X, h, color, label) -> None:
    """
    Input:  X, h
    Output: line on graph
    """
    plt.plot(X, h, color=color, label=label)


if __name__ == "__main__":

    data = pd.read_csv("data.csv") # read input from file
    X = np.array(data.iloc[:, 0:-1]) # values converts it into a numpy array
    y = np.array(data.iloc[:, -1])   # just the last column

    plt.title("Linear Regression")
    plot_graph(plt, X, y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Normal Equation Model 
    X_train = np.c_[np.ones(len(X_train)), X_train] # converting X to (n + 1) dimension
    X_train_transpose = np.transpose(X_train) # getting X transpose
    theta = np.linalg.inv(X_train_transpose.dot(X_train)).dot(X_train_transpose).dot(y_train)

    h = theta[0] + theta[1] * X_train[:, 1]
    plot_line(plt, X_train[:, 1], h, color="blue", label="Normal Equation")

    h = theta[0] + theta[1] * X_test                                                      
    accuracy = mean_squared_error(y_test, h) # Calculating accuracy on test data
    print("Normal Equation, theta0: {:.2f}, theta1: {:.2f}, accuracy {:.2f}".format(theta[0], theta[1], accuracy))

    plt.legend()
    plt.show()
