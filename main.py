import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

openpath = "C:\\"
fileName = 0
version = "0.1.0beta"
app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("ESP8266 Flasher")
ui.statusbar.showMessage("Version " + version)	


portList = []
ports = QSerialPortInfo().availablePorts()

for port in ports:
	portList.append(port.portName())

def openfile():
	global fileName
	fileName = QFileDialog.getOpenFileName(ui, "Open BIN File", openpath , "*.bin")
	if fileName[0] != '':
		ui.statusbar.showMessage("BIN file opened")
		print(fileName)
	else:
		ui.statusbar.showMessage("BIN file not opened. Please, try again.")
def flash():
	if fileName == 0:
		ui.statusbar.showMessage("Error! Please, first open a BIN file")
	else:
		COM = ui.comlist.currentText()
		command = "esptool.exe -p " + COM + " -b 115200" + " write_flash 0 " + fileName[0]
		code = os.system(command)
		print(code)
		if code == -1 or code == 2:
			ui.statusbar.showMessage("Flash not sucess. Maybe you choose wrong port or BIN file?")
		else:
			ui.statusbar.showMessage("Flash sucess. Thanks for using ESP8266 Flasher")	


ui.openF.clicked.connect(openfile)
ui.flashB.clicked.connect(flash)
ui.comlist.addItems(portList)

ui.show()
app.exec()