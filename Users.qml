import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.2
 
Dialog {
	id: usersWindow
	width: 500
	height: 500

	contentItem: Rectangle {
		anchors.fill: parent
		color: "#e1e1e2"
		RowLayout {
			anchors.fill: parent

			ScrollView {
				Layout.bottomMargin: 50
				Layout.fillWidth: true
				Layout.fillHeight: true
				ListView {
					Layout.fillWidth: true
					Layout.fillHeight: true
					focus: true
					id: users
					model: usersModel
					currentIndex: -1
					delegate: RowLayout{
						id: usersLayout
						width: users.width

						Label {
							text: userName
							width: parent.width
							Layout.bottomMargin: 5
							Layout.topMargin: 5
							Layout.leftMargin: 5
							Layout.rightMargin: 5

							MouseArea {
								anchors.fill: parent
								onClicked: selectUser(index)
								onDoubleClicked: selectFolder(index)
							}
						}

						MouseArea {
							Layout.fillWidth: true
							Layout.fillHeight: true
							onClicked: selectUser(index)
							onDoubleClicked: selectFolder(index)
						}

						function selectUser(index) {
							usersLayout.ListView.view.currentIndex = index
						}
						
						function selectFolder(index) {
							favoritesModel.loadFavoritesByUserId(index)

							usersWindow.close()
							
							favoritesWindow.open()
						}
					}
					highlight: Rectangle { color: "lightsteelblue" }
				}
			}
		}

		RowLayout {
			anchors.bottom: parent.bottom
			anchors.right: parent.right

			Button {
				text: "Add"
				Layout.rightMargin: 10
				Layout.bottomMargin: 10
				onClicked: {
					usersWindow.close()

					addUserWindow.open()
				}
			}

			Button {
				Layout.rightMargin: 10
				Layout.bottomMargin: 10
				text: "Delete"
				onClicked: {
					usersModel.deleteUser(users.currentIndex)
				}
			}
			
			Button {
				Layout.rightMargin: 10
				Layout.bottomMargin: 10
				text: "Close"
				onClicked: {
					usersWindow.close()
				}
			}
		}
	}
}