#indices.py
# Has the indices of all dictionaries here.

FILE_INDEX = 1 #index that starts the files of sys.argv

JSON_FIELD_NAMES = [u'requester_number_of_posts_on_raop_at_request', u'requester_subreddits_at_request', u'requester_number_of_posts_on_raop_at_retrieval', u'requester_number_of_comments_at_request', u'request_title', u'requester_days_since_first_post_on_raop_at_retrieval', u'giver_username_if_known', u'requester_days_since_first_post_on_raop_at_request', u'post_was_edited', u'requester_account_age_in_days_at_request', u'requester_upvotes_minus_downvotes_at_retrieval', u'requester_number_of_posts_at_retrieval', u'requester_user_flair', u'requester_upvotes_minus_downvotes_at_request', u'requester_username', u'unix_timestamp_of_request', u'requester_upvotes_plus_downvotes_at_request', u'unix_timestamp_of_request_utc', u'number_of_upvotes_of_request_at_retrieval', u'number_of_downvotes_of_request_at_retrieval', u'requester_number_of_comments_in_raop_at_retrieval', u'request_number_of_comments_at_retrieval', u'requester_number_of_posts_at_request', u'requester_received_pizza', u'requester_number_of_comments_at_retrieval', u'request_text', u'requester_account_age_in_days_at_retrieval', u'requester_upvotes_plus_downvotes_at_retrieval', u'request_text_edit_aware', u'request_id', u'requester_number_of_comments_in_raop_at_request', u'requester_number_of_subreddits_at_request']

#INDICES OF FIELD NAMES
REQUESTER_NUMBER_OF_POSTS_ON_RAOP_AT_REQUEST = 0
REQUESTER_SUBREDDITS_AT_REQUEST = 1
REQUESTER_NUMBER_OF_POSTS_ON_RAOP_AT_RETRIEVAL = 2
REQUESTER_NUMBER_OF_COMMENTS_AT_REQUEST = 3
REQUEST_TITLE = 4
REQUESTER_DAYS_SINCE_FIRST_POST_ON_RAOP_AT_RETRIEVAL = 5
GIVER_USERNAME_IF_KNOWN = 6
REQUESTER_DAYS_SINCE_FIRST_POST_ON_RAOP_AT_REQUEST = 7
POST_WAS_EDITED = 8
REQUESTER_ACCOUNT_AGE_IN_DAYS_AT_REQUEST = 9
REQUESTER_UPVOTES_MINUS_DOWNVOTES_AT_RETRIEVAL = 10
REQUESTER_NUMBER_OF_POSTS_AT_RETRIEVAL = 11
REQUESTER_USER_FLAIR = 12
REQUESTER_UPVOTES_MINUS_DOWNVOTES_AT_REQUEST = 13
REQUESTER_USERNAME = 14
UNIX_TIMESTAMP_OF_REQUEST = 15
REQUESTER_UPVOTES_PLUS_DOWNVOTES_AT_REQUEST = 16
UNIX_TIMESTAMP_OF_REQUEST_UTC = 17
NUMBER_OF_UPVOTES_OF_REQUEST_AT_RETRIEVAL = 18
NUMBER_OF_DOWNVOTES_OF_REQUEST_AT_RETRIEVAL = 19
REQUESTER_NUMBER_OF_COMMENTS_IN_RAOP_AT_RETRIEVAL = 20
REQUEST_NUMBER_OF_COMMENTS_AT_RETRIEVAL = 21
REQUESTER_NUMBER_OF_POSTS_AT_RETRIEVAL = 22
REQUESTER_RECEIVED_PIZZA = 23
REQUESTER_NUMBER_OF_COMMENTS_IN_RAOP_AT_RETRIEVAL = 24
REQUEST_TEXT = 25
REQUESTER_ACCOUNT_AGE_IN_DAYS_AT_RETRIEVAL = 26
REQUESTER_UPVOTES_PLUS_DOWNVOTES_AT_RETRIEVAL = 27
REQUESTER_TEXT_EDIT_AWARE = 28
REQUEST_ID = 29
REQUESTER_NUMBER_OF_COMMENTS_IN_RAOP_AT_REQUEST = 30
REQUESTER_NUMBER_OF_SUBREDDITS_AT_REQUEST = 31

#TIME RELATED THINGS
MONTHS = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
DAYS_OF_THE_WEEK = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}