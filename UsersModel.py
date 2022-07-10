import os
from PyQt5.QtCore import Qt, QByteArray, QAbstractListModel, QModelIndex, pyqtSlot
from UserRecordsModel import Users
from RecordsModel import Favorites
from datetime import datetime

class UsersModel(QAbstractListModel):
	userName = Qt.UserRole + 1

	def __init__(self, parent=None):
		self.base = parent
		
		super().__init__(parent)
		
		self.users = []

	def rowCount(self, parent=QModelIndex()):
		return len(self.users)

	def data(self, index, role):
		return self.users[index.row()]['userName']
		
	def roleNames(self):	
		default = super().roleNames()
		default[self.userName] = QByteArray(b"userName")
		return default

	#Получение списка пользователей
	@pyqtSlot()
	def loadUsers(self):
		self.beginResetModel()

		self.users = []

		query = Users.select()
		
		for user in query:
			self.users.append({'userName': user.name, 'id': user.id})
		
		self.endResetModel()

	#Создание нового избранного
	@pyqtSlot(int)
	def saveFavorite(self, index):
		with self.base.db.atomic():
			Favorites.create(user_id=self.users[index]['id'], path=self.base.folders.currentDirectoryPlain, date=datetime.now())
			
	#Удаление пользователя и его записей избранного
	@pyqtSlot(int)
	def deleteUser(self, index):
		query = Users.delete().where(Users.id==self.users[index]['id'])
		query.execute()
		
		query = Favorites.delete().where(Favorites.user_id==self.users[index]['id'])
		query.execute()
		
		self.loadUsers()

	#Добавление пользователя
	@pyqtSlot(str)
	def addUser(self, userName):
		Users.create(name=userName)
		
		self.loadUsers()