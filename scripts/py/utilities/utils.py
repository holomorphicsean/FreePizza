# utils.py
# This file will contain random utility functions. If you add a function, try and provide
# a small description of what it does above the funcitond definition. 

import sys
import datetime

'''Error functions'''
def die(msg=""):
	print "[ERROR] -- " + msg
	sys.exit(1)

def check_for_args(args, numOfArgs=1):
	if len(args) - 1 != numOfArgs:
		return False
	else:
		return True

def timestamp_to_datetime(timestamp):
	return datetime.datetime.fromtimestamp(timestamp).strfttime('%Y-%m-%d %H:%M:%S')

