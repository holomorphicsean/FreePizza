#json_to_csv_converter.py
# Hopefully the functionality is obvious, but converts JSON files into CSV files.

import json
import csv
import sys

from utilities import utils, indices

def convert_jsonfile_to_csvfile():
	if not utils.check_for_args(sys.argv):
		utils.die("Usage: json_to_csv_converter <json file name>")

	f = open(sys.argv[indices.FILE_INDEX])
	json_obj = ""

	for line in f:
		json_obj += line

	training_data = json.loads(json_obj)

	with open('data/csv/train.csv', 'wb') as f:
		fwriter = csv.writer(f, delimiter = ',')
		fwriter.writerow(indices.JSON_FIELD_NAMES)
		for record in training_data:
			row = list()
			for index in indices.JSON_FIELD_NAMES:
				if type(record[index]) is type(u''):
					row.append(record[index].encode('utf-8'))
				else:
					row.append(record[index])
			fwriter.writerow(row)

convert_jsonfile_to_csvfile()