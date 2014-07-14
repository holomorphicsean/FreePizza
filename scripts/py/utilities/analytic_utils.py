# analytic_utils.py 
# A set of analytic tools for our project

import utils
import indices

'''The DataHelper base class. Only includes a method to get the yes/no answer from a given record'''
class DataHelper:
	def __init__(self, record):
		self.record = record

	def did_receive_pizza(self):
		return self.record[indices.REQUESTER_RECEIVED_PIZZA]

'''The RetrievalDataHelper class is meant for getting data from our training set that deals with numbers obtained
when the data was retrieved.'''
class RetrievalDataHelper(DataHelper):
	def __init__(self, record):
		self.record = record

	def get_upvotes_and_downvotes(self):
		#stub
		upvotes = (self.record[indices.REQUESTER_UPVOTES_PLUS_DOWNVOTES_AT_RETRIEVAL] +
			self.record[indices.REQUESTER_UPVOTES_MINUS_DOWNVOTES_AT_RETRIEVAL]) / 2
		downvotes = record[indices.REQUESTER_UPVOTES_PLUS_DOWNVOTES_AT_RETRIEVAL] - upvotes
		return (upvotes, downvotes)



'''The RequestDataHelper class is meant for getting data from our training set when the request to get pizza was made.
This differents from the RetrievalDataHelper class.'''
class RequestDataHelper(DataHelper):
	def __init__(self, record):
		self.record = record

	def get_upvotes_and_downvotes(self):
		#stub
		upvotes = (self.record[indices.REQUESTER_UPVOTES_PLUS_DOWNVOTES_AT_REQUEST] +
			self.record[indices.REQUESTER_UPVOTES_MINUS_DOWNVOTES_AT_REQUEST]) / 2
		downvotes = record[REQUESTER_UPVOTES_MINUS_DOWNVOTES_AT_REQUEST] - upvotes
		return (upvotes, downvotes)

'''The TimeDataHelper is a class meant to help out with time related data analysis.'''
class TimeDataHelper(DataHelper):
	def __init__(self, record):
		self.record = record
		self.transformed_timestamp = None

	def transform_timestamp(self):
		self.transformed_timestamp = utils.timestamp_to_datetime(self.record[indices.UNIX_TIMESTAMP_OF_REQUEST])
		return self.transformed_timestamp

	def get_timestamp_info(self):
		if self.transformed_timestamp is not None:
			info = dict()
			info["month"] = self.transformed_timestamp.month
			info["time"] = self.transformed_timestamp.hour #will only provide hour for now
			info["dow"] = self.transformed_timestamp.weekday() #dow = day of week
			info["date"] = self.transformed_timestamp.day
			return info
			#stub
		else:
			utils.die("You did not transform the timestamp yet!")
			return