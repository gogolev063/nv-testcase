import random
import string

import sys
from threading import Timer
import datetime

import json
import requests

import pandas as pd

from config import URL


TEXT_LENGTH = 16                 # length of the generated strings
GET_ENTRIES_COUNT = 10           # the number of requested entries
MIN_MESSAGE_ENTRIES_COUNT = 10   # the minimum number of entries that must be recorded at the same time
MAX_MESSAGE_ENTRIES_COUNT = 100  # the maximum number of entries that must be recorded at the same time
LOG_INTERVAL = 10                # the duration of the interval for logging the number of deleted entries


def generate_string(length: int) -> str:
	"""
	Generates a string of a given length using a specific alphabet
	:param length: The length of the generated string
	:return: The generated string of the specified length
	"""

	alphabet = string.ascii_letters + string.digits
	return ''.join(random.sample(alphabet, length))


def add_entries(entries: list) -> None:
	"""
	Getting a set number of entries from the application server
	:param entries:
	:return:
	"""
	query = json.dumps(entries)
	requests.post(URL + '/new?records=' + query)


def get_entries(count: int) -> str:
	"""
	Requests a specified number of entries from the application server
	:param count: The number of entries to request on the application server
	:return: JSON string with list of object dictionaries
	"""
	response = requests.get(URL + '/?count=' + str(count))
	return response.json()


def delete_entries(ids: list) -> int:
	"""
	Calls the delete entries with given IDs on the application server
	:param ids: List of IDs to delete
	:return: Returns count of deleted entries
	"""
	count = 0
	for id in ids:
		response = requests.delete(URL + '/?uuid=' + id)
		if response.status_code == 200:
			count =+ 1
		elif response.status_code == 404:
			print(f"An entry with a uuid = {id} was not found!")
	return count


def log_deleted_entries_count() -> None:
	"""
	Writing the number of deleted entries to the standard output stream every LOG_INTERVAL seconds
	:params message: Message to log into the standard output stream
	:return:
	"""
	sys.stdout.write(str(datetime.datetime.now()) + '   Deleted records: ' + str(deleted_count) + '\n')
	Timer(LOG_INTERVAL, log_deleted_entries_count).start()


# total count of deleted records
deleted_count = 0

# start logging of deleted entries count
log_deleted_entries_count()

while True:
	add_entries([generate_string(TEXT_LENGTH)
								for i in range(random.randint(MIN_MESSAGE_ENTRIES_COUNT,
																							MAX_MESSAGE_ENTRIES_COUNT))])
	try:
		records = pd.DataFrame(json.loads(get_entries(GET_ENTRIES_COUNT)))
		deleted_count += delete_entries(records.uuid.tolist())
	
	except Exception as e:
		print('ERROR', e)
