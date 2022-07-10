from BaseModel import BaseModel
from peewee import IntegerField, ForeignKeyField, CharField, DateTimeField
from UserRecordsModel import Users

class Favorites(BaseModel):
	user_id = IntegerField()
	path = CharField()
	date = DateTimeField()