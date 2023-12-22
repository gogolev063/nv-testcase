import json

from sqlalchemy import create_engine, cast, UUID
from sqlalchemy.orm import sessionmaker, class_mapper
from sqlalchemy_utils import database_exists, create_database

from db_config import DB_PATH

from models.base import Base
from models.records import Record


# a class for interacting with a database
class DBDataSource:
	def __init__(self) -> None:
		# create a database engine
		self._engine = create_engine(DB_PATH)

		# create the database if it doesn't exist
		if not database_exists(DB_PATH):
			create_database(DB_PATH)
			Base.metadata.create_all(self._engine)

		# create a session factory
		self._Session = sessionmaker(bind=self._engine)

	def _to_dict(self, model: Record) -> dict:
		"""
		Saves the values of the fields of an object of the Record class 
		in the form of a dictionary, in which the key is the column name, 
		and the value is the corresponding value of the object
		:params model: An object of the Record class that needs to be saved 
		as a dictionary
		:return: Returns a dictionary, in which the key is the column name, 
		and the value is the corresponding value of the object
		"""
		columns = class_mapper(model.__class__).columns
		return dict((c.name, getattr(model, c.name)) for c in columns)

	def get_record_by_id(self, uuid: str) -> (bool, str):
		"""
		Returns an entry from database with specified uuid
		:param uuid: ID of entry for request from database
		:return: an entry with specified uuid
		"""
		with self._Session() as session:
			query = session.query(Record).where(Record.uuid == cast(uuid, UUID))
			results = query.all()
			found = len(results) > 0
			if found:
				data = self._to_dict(results[0])
			else:
				data = None

		return (found, json.dumps(data, default=str))

	def get_records(self, count: int | None = None):
		"""
		Returns the specified number of entries from database
		:param count: Optional. Limit the number of entries for request from database
		:return: List of entries
		"""
		with self._Session() as session:
			query = session.query(Record)
			if not count is None:
				query = query.limit(count)
			results = query.all()
			data = [self._to_dict(result) for result in results]

		return json.dumps(data, default=str)

	def add_records(self, records: str) -> bool:
		"""
		Adds entries to the database based on the passed list of values
		:param records: The list of records to insert into the database
		:return: Returns True if successful and False otherwise
		"""
		with self._Session() as session:
			try:
				for text in json.loads(records):
					session.add(Record(text=text))
			
			except Exception as e:
				session.rollback()
				return False
			
			else:
				session.commit()
				return True

	def delete_record(self, uuid: str) -> bool:
		"""
		Delete an entry from database with the specified ID
		:param uuid: The ID of record to delete from database
		:return: Number of deleted rows
		"""
		with self._Session() as session:
			try:
				record = session.query(Record).where(Record.uuid == cast(uuid, UUID)).one()
				session.delete(record)

			except Exception as e:
				session.rollback()
				return False
			
			else:
				session.commit()
		
		return True
