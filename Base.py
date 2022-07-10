import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject
from peewee import SqliteDatabase

# Создание подключения к базе данных
db = SqliteDatabase("main.db")

from FavoritesModel import FavoritesModel
from UsersModel import UsersModel
from FoldersModel import FoldersModel
from FilesModel import FilesModel
from UserRecordsModel import Users
from RecordsModel import Favorites
import names

class Base(QObject):
	def __init__(self, parent=None):
		self.db = db
	
		super().__init__(parent)	
		
		#Созание базы данных
		self.initDataBase()

		#Создание окна
		app = QGuiApplication(sys.argv)
		engine = QQmlApplicationEngine()

		#Инициализация моделей
		self.favorites = FavoritesModel(self)
		self.users = UsersModel(self)
		self.files = FilesModel(self)
		self.folders = FoldersModel(self)

		engine.rootContext().setContextProperty('favoritesModel', self.favorites)
		engine.rootContext().setContextProperty('usersModel', self.users)
		engine.rootContext().setContextProperty('foldersModel', self.folders)
		engine.rootContext().setContextProperty('filesModel', self.files)

		#Загрузка базовой QML
		engine.load("main.qml")	

		#Загрузка списка папок
		self.folders.getFolders()

		engine.quit.connect(app.quit)
		sys.exit(app.exec_())
	
	def initDataBase(self):
		#Проверка на существование базы данных
		if not db.table_exists('users'):
			db.create_tables([Users, Favorites])
			
			#Генерация имён
			with db.atomic():
				for _ in range(10):
					user = Users.create(name=names.get_full_name(gender='male'))