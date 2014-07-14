# time_stat_report.py
# This script will generate a report that'll give stats about the success rates of requests based on time. 

from utilities import utils, indices, analytic_utils
import csv
import sys

def main():
	#0. Check to make sure we included the proper file args. We're going to use the .csv files:
	if not utils.check_for_args(sys.argv):
		utils.die("Usage: Not enough args -- python time_stat_report.py <csv filename here>")

	yes_monthly_data = dict()
	no_monthly_data = dict()

	#0.5 Let's init the dicts
	for i in xrange(12):
		yes_monthly_data.setdefault(i+1, 0)
		no_monthly_data.setdefault(i+1, 0)


	#1. Let's import the CSV file and gather data
	with open(sys.argv[1], 'rb') as f:
		freader = csv.reader(f, delimiter=",")
		first = True
		for row in freader:
			if not first:
				helper = analytic_utils.TimeDataHelper(row)
				helper.transform_timestamp()
				info = helper.get_timestamp_info()

				if helper.did_receive_pizza() == "True":
					yes_monthly_data[info["month"]] += 1
				else:
					no_monthly_data[info["month"]] += 1
			else:
				first = False

	#2. Analysis yay!
	total_yes = sum(yes_monthly_data.values())
	for k,v in yes_monthly_data.iteritems():
		print "For month %d, there are %d out of %d [%f percent].\n" % (k, v, total_yes, (float(v) / total_yes) * 100)

	total_no = sum(no_monthly_data.values())
	for k,v in no_monthly_data.iteritems():
		print "For month %d, there are %d out of %d [%f percent].\n" % (k, v, total_no, (float(v) / total_no) * 100 )

if __name__ == "__main__":
	main()