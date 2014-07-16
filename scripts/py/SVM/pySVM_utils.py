from PyML import *
from PyML.classifiers.svm import loadSVM
from math import *
import os

## This is a function to either train data or cross-validate data

def train(X,y):

    #Ask to name data
    name = raw_input("Enter name for data: ")

    #Load data into PyML's vector objects, then train our set
    data = VectorDataSet(X,L=y)

    s = SVM()
    s.train(data)
    s.save(name)

def cross_validate(X,y):

    # Ask what percentage of the data should be trained
    p = 0
    while p < 50 or p > 100:
        p = raw_input("Enter percentage of data to train (between 50 and 75): ")
        p = float(p);

    K = int(floor(float(p)*len(X)/100))

    X1 = X[0:K]
    y1 = y[0:K]

    #Load data into PyML's vector objects, then train set
    data = VectorDataSet(X1,L=y1)

    s = SVM()
    s.train(data)
    s.save("cross_validating")

    #Now check the other data
    X2 = X[K+1:-1]
    y2 = y[K+1:-1]

    #Load our training data
    loadedSVM = loadSVM("cross_validating",data)

    testData = VectorDataSet(X2,L=y2)
    r = loadedSVM.test(testData)
    print r

    #Delete the data now that we're done with it
    os.system("rm cross_validating")
