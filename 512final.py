#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:28:38 2020

@author: jameshuang
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 
import time
import random
from matplotlib import animation

N=23; #-1 means all
df = pd.read_csv("pex23.txt",sep=' ',header=0)
col_name=[];
for i in range(1,24):
    col_name.append('X'+str(i));
    if i ==23:
        col_name.append('Y');
df.columns=col_name;


def sigmoid(x):
    # Activation function used to map any real value between 0 and 1
    return 1 / (1 + np.exp(-x))

def net_input(theta, x):
    # Computes the weighted sum of inputs
    return np.dot(x, theta)

def probability(theta, x):
    # Returns the probability after passing through sigmoid
    return sigmoid(net_input(theta, x))

def cost_function(theta, x, y):
    # Computes the cost function for all the training samples
    m = x.shape[0]
    total_cost = -(1 / m) * np.sum(
        y * np.log(probability(theta, x)) + (1 - y) * np.log(
            1 - probability(theta, x)))
    return total_cost

def gradient(theta, x, y):
    # Computes the gradient of the cost function at the point theta
    m = x.shape[0]
    return (1 / m) * np.dot(x.T, sigmoid(net_input(theta,   x)) - y)

def fit(x, y, theta):
    start_time = time.time()
    opt_weights = optimize.fmin_tnc(func=cost_function, x0=theta,
                  fprime=gradient,args=(x, y.flatten()))
    exe_time = time.time() - start_time;
    print('exe time:',exe_time);
    print(opt_weights[1]);
    
    #N=3, [-4.81570985 66.75146026 11.27840838 33.06238058]
    #N=2, [-3.8657184  46.23553302 14.16926244] iter=45
    
    return opt_weights[0]

def predict(x):
    theta = parameters[:, np.newaxis]
    return probability(theta, x)

def accuracy(x, actual_classes, probab_threshold=0.5):
    predicted_classes = (predict(x) >= probab_threshold).astype(int)
    predicted_classes = predicted_classes.flatten()
    accuracy = np.mean(predicted_classes == actual_classes)
    return accuracy * 100


if __name__ == '__main__':

    
    #split train/test 
    random.seed(2020);
    train = random.sample(range(0,df.shape[0]), 1500);
    test=list(range(0,df.shape[0]));
    for temp in train:
        test.remove(temp);
    
    df_train=df.iloc[train, :]
    df_test=df.iloc[test, :]
    
    X = df_train.iloc[:, :N];
    y = df_train.iloc[:, -1];
    admitted = X.loc[y == 1];
    not_admitted = X.loc[y == 0]; 
    X = np.c_[np.ones((X.shape[0], 1)), X];
    y = y[:, np.newaxis];
    theta = np.zeros((X.shape[1], 1));
    
    X_test = df_test.iloc[:, :N];
    y_test = df_test.iloc[:, -1];
    admitted_test = X_test.loc[y_test == 1];
    not_admitted_test = X_test.loc[y_test == 0];
    X_test = np.c_[np.ones((X_test.shape[0], 1)), X_test];
    y_test = y_test[:, np.newaxis];
    
    #skl package
    #model = LogisticRegression();
    #model.fit(X, y.ravel());
    #y_values_skl = model.predict(X_test);
    #accuracy_skl = accuracy_score(y_test.flatten(),y_values_skl)*100;
    
    #model
    parameters = fit(X, y.ravel(), theta);
    accuracy = accuracy(X_test, y_test);
    
    
    # visualize if N=2
    if N==2:
        
        x_values = [np.min(X_test[:, 1] - 0.01), np.max(X_test[:, 2] + 0.01)];
        y_values = - (parameters[0] + np.dot(parameters[1], x_values)) / parameters[2];    
        plt.scatter(admitted_test.iloc[:, 0], admitted_test.iloc[:, 1], s=10, label='explosive1')
        plt.scatter(not_admitted_test.iloc[:, 0], not_admitted_test.iloc[:, 1], s=1, label='not explosive2')
        plt.plot(x_values, y_values, label='logistic line')
        plt.xlabel('variable1')
        plt.ylabel('variable2')
        plt.legend()
        plt.show()


