# time_stat_report.py
# This script will generate a report that'll give stats about the success rates of requests based on time. 

from utilities import utils, indices, analytic_utils
import csv
import sys

def main():
	#0. Check to make sure we included the proper file args. We're going to use the .csv files:
	if not utils.check_for_args(sys.argv):
		utils.die("Usage: Not enough args -- python time_stat_report.py <csv filename here>")

	#Containers for data
	yes_monthly_data = dict()
	yes_time_data = dict()
	yes_days_data = dict()
	yes_date_data = dict()

	no_monthly_data = dict()
	no_time_data = dict()
	no_days_data = dict()
	no_date_data = dict()

	#0.5 Let's init the dicts
	for i in xrange(12):
		yes_monthly_data.setdefault(i+1, 0)
		no_monthly_data.setdefault(i+1, 0)

	for i in xrange(7):
		yes_days_data.setdefault(i, 0)
		no_days_data.setdefault(i, 0)

	for i in xrange(24):
		yes_time_data.setdefault(i, 0)
		no_time_data.setdefault(i, 0)


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
					yes_time_data[info["time"]] += 1
					yes_days_data[info["dow"]] += 1

				else:
					no_monthly_data[info["month"]] += 1
					no_time_data[info["time"]] += 1
					no_days_data[info["dow"]] += 1
			else:
				first = False

	#Generate monthly stats
	#todo: write a helper class for this
	total_records = 4040
	print "~~~~~~~~~~~~~~~~~~\nMONTHLY STATISTICS~~~~~~~~~~~~~~~~~~\n"
	for month in indices.MONTHS:
		print "Requests made in %s\n" % (indices.MONTHS[month])
		print "%d out of %d total people [%f %%] received pizza while" %(yes_monthly_data[month], total_records, yes_monthly_data[month] * 100.0 / total_records)
		print "%d out of %d total people [%f %%] received no pizza\n" %(no_monthly_data[month], total_records, no_monthly_data[month] * 100.0 / total_records)

	print "\n~~~~~~~~~~~~~~~~~~\nDAY OF THE WEEK STATS\n~~~~~~~~~~~~~~~~~~\n"
	for day in indices.DAYS_OF_THE_WEEK:
		print "Requests made on %s\n" % (indices.DAYS_OF_THE_WEEK[day])
		print "%d requests [%f %%] usually get pizza while" %(yes_days_data[day], yes_days_data[day]*100.0/total_records)
		print "%d requests [%f %%] usually get denied pizza.\n" %(no_days_data[day], no_days_data[day]*100.0/total_records)

	print "\n~~~~~~~~~~~~~~~~~~\nHOUR OF THE DAY STATS\n~~~~~~~~~~~~~~~~~~\n"
	for i in xrange(24):
		print "Requests made during the hour %d of the day:\n" %(i)
		print "%d requests [%f %%] usually get pizza while" %(yes_time_data[i], yes_time_data[i] * 100.0/total_records)
		print "%d requests [%f %%] usually don't get pizza. \n" %(no_time_data[i], no_time_data[i] * 100.0 / total_records)


if __name__ == "__main__":
	main()