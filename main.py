import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

openpath = "C:\\"
fileName = 0
speeds = ["9600", "115200"]
# \\index        0        1       2      3      4      5      6
flashsizes = ["256KB", "512KB", "1MB", "2MB", "4MB", "8MB", "16MB"]
flashmodes = ["qio", "qout", "dio", "dout"]
version = "0.2.0"
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
		speed = ui.speedlist.currentText()
		flash = ui.flashlist.currentText()
		flashmode = ui.modelist.currentText()
		command = "esptool.exe -p " + COM + " -b " + speed + " write_flash " + "--flash_mode " + flashmode + " --flash_size " + flash + " 0x0 " +fileName[0]
		print(command)
		code = os.system(command)
		if code == -1 or code == 2 or code == 1:
			ui.statusbar.showMessage("Flash not sucess. Maybe you choose wrong port or BIN file?")
		else:
			ui.statusbar.showMessage("Flash sucess. Thanks for using ESP8266 Flasher")
def erase_flash():
	COM = ui.comlist.currentText()
	ui.statusbar.showMessage("Start erasing")
	erase_command = "esptool.exe -p "+ COM + " erase_flash"
	print(erase_command)
	os.system(erase_command)

ui.openF.clicked.connect(openfile)
ui.flashB.clicked.connect(flash)
ui.comlist.addItems(portList)
ui.speedlist.addItems(speeds)
ui.speedlist.setCurrentIndex(1)
ui.flashlist.addItems(flashsizes)
ui.flashlist.setCurrentIndex(2)
ui.modelist.addItems(flashmodes)
ui.modelist.setCurrentIndex(2)
ui.erase.clicked.connect(erase_flash)

ui.show()
app.exec()