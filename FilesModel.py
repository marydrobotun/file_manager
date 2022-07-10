import os
from PyQt5.QtCore import Qt, QByteArray, QAbstractListModel, QModelIndex, pyqtSlot, pyqtSignal

class FilesModel(QAbstractListModel):
	fileName = Qt.UserRole + 1
	
	fileResult = pyqtSignal(str, str, arguments=['file'])

	def __init__(self, parent=None):
		self.base = parent
	
		super().__init__(parent)

		self.files = []

	def rowCount(self, parent=QModelIndex()):
		return len(self.files)

	def data(self, index, role):
		return self.files[index.row()]['fileName']
		
	def roleNames(self):	
		default = super().roleNames()
		default[self.fileName] = QByteArray(b"fileName")
		return default
	
	def getFiles(self, directory):
		self.beginResetModel()

		self.files = [{'fileName': d} for d in sorted(os.listdir(directory)) if os.path.isfile(directory + os.sep + d)]
	
		self.endResetModel()

	#Выбор файла
	@pyqtSlot(int)
	def selectFile(self, index):
		filePath = self.base.folders.currentDirectoryPlain + self.files[index]['fileName']
	
		filename, fileExtension = os.path.splitext(filePath)

		text = ''

		#Проверка расширения
		if fileExtension[1:] in ['txt', 'py', 'qml']:
			#Получение текстовых файлов
			f = open(filePath, "r")
			text = f.read(500)
			f.close()

		#Отправка сообщения в Qt
		self.fileResult.emit(filePath, text)