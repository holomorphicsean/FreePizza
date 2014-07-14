from PyML import *


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

#Load data
data = VectorDataSet(X,L=y)

#Create SVM object, then train our set
s = SVM()
s.train(data)
s.save("freePizza")

## Yay!
