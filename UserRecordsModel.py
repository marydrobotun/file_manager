from BaseModel import BaseModel
from peewee import CharField

class Users(BaseModel):
	name = CharField()
	