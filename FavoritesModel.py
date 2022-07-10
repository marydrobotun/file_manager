import re
import os
from PyQt5.QtCore import Qt, QByteArray, QAbstractListModel, QModelIndex, pyqtSlot
from RecordsModel import Favorites
from UserRecordsModel import Users

class FavoritesModel(QAbstractListModel):
	userName = Qt.UserRole + 1
	path = Qt.UserRole + 2
	date = Qt.UserRole + 3

	favorites = []

	def __init__(self, parent=None):
		self.base = parent
	
		super().__init__(parent)

	def rowCount(self, parent=QModelIndex()):
		return len(self.favorites)

	def data(self, index, role):
		if role == self.userName:
			return self.favorites[index.row()]['userName']
			
		if role == self.path:
			return self.favorites[index.row()]['path']

		if role == self.date:
			return self.favorites[index.row()]['date']			
		
	def roleNames(self):	
		default = super().roleNames()
		default[self.userName] = QByteArray(b"userName")
		default[self.path] = QByteArray(b"path")
		default[self.date] = QByteArray(b"date")
		return default

	#Загрузка с базы данных избранного
	@pyqtSlot()
	def loadFavorites(self):
		self.beginResetModel()

		query = Favorites.select(Users.name, Favorites.path, Favorites.date).join(Users, on=(Users.id == Favorites.user_id))
		
		self.favorites = []
		
		for favorite in query:
			self.favorites.append({'userName': favorite.users.name, 'path': favorite.path, 'date': str(favorite.date)})
		
		self.endResetModel()

	#Загрузка с базы данных избранного по id пользователя
	@pyqtSlot(int)
	def loadFavoritesByUserId(self, index):
		self.beginResetModel()

		query = Favorites.select(Users.name, Favorites.path, Favorites.date).join(Users, on=(Users.id == Favorites.user_id)).where(Favorites.user_id == self.base.users.users[index]['id'])
		
		self.favorites = []
		
		for favorite in query:
			self.favorites.append({'userName': favorite.users.name, 'path': favorite.path, 'date': str(favorite.date)})
		
		self.endResetModel()

	#Выбор избранного
	@pyqtSlot(int)
	def selectFavorite(self, index):
		self.base.folders.setFolder(self.favorites[index]['path'])