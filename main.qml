import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

ApplicationWindow {
	visible: true
	width: 640
	height: 240
	title: qsTr("Files Viewer")

	Connections {
		target: foldersModel

		function onFolderResult(folder) {
			currentPath.text = folder
		}
	}
	
	Connections {
		target: filesModel

		function onFileResult(file, text) {
			if (text)
			{
				textPreview.text = text
				imagePreview.visible = false
				textPreview.visible = true
			}
			else if (file.match(".png|.jpg$"))
			{
				imagePreview.source = file
				imagePreview.visible = true
				textPreview.visible = false
			}
			else
			{
				imagePreview.visible = false
				textPreview.visible = false
			}
		}
	}

	menuBar: MenuBar {
		Menu {
			title: qsTr("File")
			MenuItem {
				text: "Close"
				onTriggered:{
					Qt.quit();
				}
			}
		}

		Menu {
			title: qsTr("Favorites")
			MenuItem {
				text: "Add folder"
				onTriggered:{
					usersModel.loadUsers()
					
					addFavoriteWindow.open()
				}
			}

			MenuItem {
				text: "Favorites"
				onTriggered:{
					favoritesModel.loadFavorites()
				
					favoritesWindow.open()
				}
			}
		}
	}

	GridLayout {
		
		Layout.fillWidth: true
		anchors.fill: parent
		columns: 1
		
		RowLayout {
			Layout.fillWidth: true
			Layout.rightMargin: 10
			Label {
				width: 200
				text: "Folder:"
				padding: 10
			}
			
			TextField {
				id: currentPath
				Layout.fillWidth: true
			}
			
		}

		SplitView {
			Layout.fillHeight: true
			Layout.fillWidth: true

			ScrollView {
				ListView {
					width: 180
					
					focus: true
					id: folders
					model: foldersModel
					currentIndex: -1
					delegate: RowLayout{
						id: foldersLayout
						width: folders.width

						Image {
							source: "images/folder.png"
							
							MouseArea {
								anchors.fill: parent
								onClicked: foldersLayout.ListView.view.currentIndex = index
								onDoubleClicked: selectFolder(index)
							}
						}

						Label {
							text: folderName
							width: parent.width

							MouseArea {
								anchors.fill: parent
								onClicked: foldersLayout.ListView.view.currentIndex = index
								onDoubleClicked: selectFolder(index)
							}
						}

						MouseArea {
							Layout.fillWidth: true
							Layout.fillHeight: true
							onClicked: foldersLayout.ListView.view.currentIndex = index
							onDoubleClicked: selectFolder(index)
						}

						function selectFolder(index){
							foldersLayout.ListView.view.currentIndex = index;
							
							foldersModel.selectFolder(index)
						}
					}
					highlight: Rectangle { color: "lightsteelblue" }
				}
			}

			ScrollView {
				ListView {
					width: 180; height: 200
					focus: true
					id: files
					model: filesModel
					currentIndex: -1
					delegate: RowLayout{
						id: filesLayout
						width: files.width

						Label {
							text: fileName
							width: parent.width

							MouseArea {
								anchors.fill: parent
								onClicked: selectFile(index)
							}
						}

						MouseArea {
							Layout.fillWidth: true
							Layout.fillHeight: true
							onClicked: selectFile(index)
						}

						function selectFile(index){
							filesLayout.ListView.view.currentIndex = index
							
							filesModel.selectFile(index)
						}
					}
					highlight: Rectangle { color: "lightsteelblue" }
				}
			}
			RowLayout {
				Rectangle {
					Layout.preferredWidth: 150
					Layout.preferredHeight: 150
					clip: true
					color: "transparent"
					border.color: "black"
					border.width: 1

					Image {
						id: imagePreview
						anchors.fill: parent
						visible: false
						fillMode: Image.PreserveAspectFit
					}

					Text {
						id: textPreview
						visible: false
						anchors.fill: parent
					}
				}
			}
		}	
	}

	AddFavorite {
		id: addFavoriteWindow
		title: qsTr("Add Favorite")
	}

	Favorites {
		id: favoritesWindow
		title: qsTr("Favorites")
	}
	
	Users {
		id: usersWindow
		title: qsTr("User List")
	}

	AddUser {
		id: addUserWindow
		title: qsTr("Add User")
	}
}