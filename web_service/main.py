from fastapi import FastAPI, Response, status

from datasource import DBDataSource

# create datasource
data_source = DBDataSource()

# create FastAPI app
app = FastAPI()


def get_entry_by_id(uuid: str, response: Response):
	"""
	Returns an entry from database with specified uuid
	:param uuid: ID of entry for request from database
	:return: Returns a specific record by the requested uuid.
	If the record does not exist, it returns HTTP 404.
	"""
	found, data = data_source.get_record_by_id(uuid)
	if not found:
		response.status_code = status.HTTP_404_NOT_FOUND
	return data


def get_entries(count: int | None = None):
	"""
	Returns the specified number of entries from database
	:param count: Optional. Limit the number of entries for request from database
	:return: List of entries
	"""
	data = data_source.get_records(count)
	return data


@app.get("/")
def get_root(response: Response, count: int | None = None,
									 uuid: str | None = None) -> str:
	"""
	Handles root request.
	:param count: Optional. The number of requested entries
	:param uuid: Optional. ID of requested entry
	"""
	if not count is None:
		message = get_entries(count)
	elif not uuid is None:
		message = get_entry_by_id(uuid, response)
	else:
		message = 'NV-Testcase web-service'

	return message


@app.get("/all")
def get_all_entries():
	"""
	Returns all entries from database
	:return: List of entries
	"""
	return get_entries()


@app.post("/new", status_code=200)
def add_entries(records: str, response: Response):
	"""
	Adds entries to the database based on the passed list of values
	:param records: The string with list of records to insert into the database
	:return: 
	"""
	data_source.add_records(records)
	response.status_code = status.HTTP_201_CREATED


@app.delete("/", status_code=200)
def delete_entry(uuid: str, response: Response):
	"""
	Delete an entry from database with the specified ID
	:param uuid: The ID of record to delete from database
	:return: Returns HTTP 200 if successful. If the record does not exist,
	returns HTTP 404
	"""
	if not data_source.delete_record(uuid):
		response.status_code = status.HTTP_404_NOT_FOUND
