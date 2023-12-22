from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID
import uuid

from models.base import Base

# define a record model class
class Record(Base):
	__tablename__ = "records"
	uuid = Column(UUID, primary_key=True, default=uuid.uuid4, unique=True)
	text = Column(String, nullable=False)
