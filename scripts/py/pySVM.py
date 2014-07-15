from PyML import *
from math import *

## Let's grab the data and put it into a list of lists for the SVM

#Initialize
X = []

#Now read the data
with open('/home/shawn/FreePizza/data/txt/numeric_field_data.txt','r') as f:

    #Keep a counter
    i = 0;

    #Now read in line per line
    for line in f:

        #Split the data inside of the brackets
        if i < 5670:
            temp = line[1:-2].split(", ");
        else:
            temp = line[1:-1].split(", ");

        #Replace a*^b to aeb to be read in scientific notation
        temp = [t.replace('*^','e') for t in temp];
        temp = map( lambda x: float(x), temp);

        #Now, append our vector X with the data
        X.append(temp)

        i = i + 1

## Now we load in the got_pizza dataset

#Initialize
y = []
with open('/home/shawn/FreePizza/data/txt/gotpizza.txt','r') as gp:

    for line in gp:
        # Turn string to boolean
        if line.rstrip() == 'True':
            temp = True
        else:
            temp = False

        y.append(temp)

## Now it's time to load our data into PyML's vector objects

#Load data (let's try 1/5th of it first)
fifth = int(floor(len(y)/5));
X2 = X[0:fifth];
y2 = y[0:fifth];

data = VectorDataSet(X2,L=y2)

#Create SVM object, then train our set
s = SVM()
s.train(data)
s.save("freePizza_test1")

## Yay!
