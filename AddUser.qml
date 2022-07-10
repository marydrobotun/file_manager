import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.2
 
Dialog {
	id: addUserWindow
	width: 480
	height: 80

	contentItem: Rectangle {
		anchors.fill: parent
		color: "transparent"
		RowLayout {
			Layout.fillWidth: true
			anchors.fill: parent

			TextField {
				id: newUser
				Layout.fillWidth: true
				Layout.rightMargin: 10
				Layout.leftMargin: 10
				Layout.topMargin: 10
				Layout.alignment: Qt.AlignTop
			}
		}

		RowLayout {
			anchors.bottom: parent.bottom
			anchors.right: parent.right

			Button {
				Layout.rightMargin: 10
				Layout.bottomMargin: 10
				text: "Add"
				onClicked: {
					usersModel.addUser(newUser.text)

					addUserWindow.close()
					
					usersWindow.open()
				}
			}
		}

	}
}