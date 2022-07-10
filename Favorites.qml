import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.2
 
Dialog {
	id: favoritesWindow
	width: 500
	height: 500
	standardButtons: Dialog.Close
	Rectangle {
		anchors.fill: parent
		color: "transparent"
		TableView {
			id: favorites
			model: favoritesModel
			anchors.fill: parent
			TableViewColumn{
				role: "userName"
				title: "UserName"
			}
			
			TableViewColumn{
				role: "path"
				title: "Path"
			}
			
			TableViewColumn{
				role: "date"
				title: "Date"
			}
			onDoubleClicked: {
				favoritesModel.selectFavorite(favorites.currentRow)
				
				favoritesWindow.close()
			}
		}
	}
}