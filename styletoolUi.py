try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

IMAGE_DIR = 'C:/Users/Acer/OneDrive/เอกสาร/maya/2024/scripts/styletool'

class StyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('Style Tool')
		self.resize(300,100)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet(
			'''
					font-family: Papyrus;
					background-color:#7ecfc5
			'''
			)

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f'{IMAGE_DIR}/pibble.png')
		scaledPixmap = self.imagePixmap.scaled(
			QtCore.QSize(100,100),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.imageLabel.setPixmap(scaledPixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name:')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			'''
				QLineEdit{
					background-color: white;
					color: navy;
					border-radius: 8px;
					font-family: Arial;
					font-weight: bold;
				}
			'''
		)

		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.selectButton = QtWidgets.QPushButton('Select')
		self.selectButton.setStyleSheet(
			'''
				QPushButton {
					background-color: blue;
					border-radius: 12px;
					font-size: 16px;
					font-family: Papyrus;
					font-weight: bold;
					padding: 4px
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 blue, stop:1 yellow);
				}
				QPushButton:pressed {
					background-color: black;
				}
			'''
		)

		self.cancelButton = QtWidgets.QPushButton('Cencel')
		self.cancelButton.setStyleSheet(
			'''
				QPushButton {
					background-color: blue;
					border-radius: 12px;
					font-size: 16px;
					font-family: Papyrus;
					font-weight: bold;
					padding: 4px
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 blue, stop:1 yellow);
				}
				QPushButton:pressed {
					background-color: black;
				}
			'''
		)
		self.buttonLayout.addWidget(self.selectButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()

def run():
	global ui
	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = StyleToolDialog(parent=ptr)
	ui.show()        