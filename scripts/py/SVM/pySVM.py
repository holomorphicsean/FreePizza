import pySVM_utils
from math import *
import sys
import os

## Check arguments
def die():
    print "Usage: python pySVM.py -a <Path to training data> <path to binary data> -c\nuse -a flag if the path is to ~/FreePizza/data/txt/";
    print "use -c flag if to cross validata data"
    exit()


#Die if not in python pySVM.py (flag1) (arg1) (arg2) (flag2) form
if len(sys.argv) < 2 or len(sys.argv) > 5:
    die()

mypath = os.getenv("HOME")

#If -a flag is used, prepend string with home data
if sys.argv[1] == "-a":
    path1 = mypath + "/FreePizza/data/txt/" + sys.argv[2]
    path2 = mypath + "/FreePizza/data/txt/" + sys.argv[3]
else:
    path1 = sys.argv[1]
    path2 = sys.argv[2]

## Let's grab the data and put it into a list of lists for the SVM

#Initialize
X = []

#Now read the data
with open(path1,'r') as f:

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
with open(path2,'r') as gp:

    for line in gp:
        # Turn string to boolean
        if line.rstrip() == 'True':
            temp = 'True'
        else:
            temp = 'False'

        y.append(temp)

## Now we feed the information into PyML

#If the -c flag was used at the end, then we're cross validating
if sys.argv[-1] == '-c':
    pySVM_utils.cross_validate(X,y)
else:
    pySVM_utils.train(X,y)

## Yay!
