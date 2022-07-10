import Base
from peewee import Model

#Базовая модель
class BaseModel(Model):
	class Meta:
		database = Base.db