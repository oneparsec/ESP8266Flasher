import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from os.path import expanduser
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtGui import QIcon
from design import Ui_MainWindow

if sys.platform == "win32":
	esptoolName = "esptool.exe"
else:
	esptoolName = "./esptool"
home = expanduser("~")
openpath = home
fileName = 0
speeds = ["9600", "19200", "38400", "57600", "74880", "115200"]
#   index        0        1       2      3      4      5      6
flashsizes = ["256KB", "512KB", "1MB", "2MB", "4MB", "8MB", "16MB"]
flashmodes = ["qio", "qout", "dio", "dout"]
version = "0.2.1"

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.statusbar.showMessage("Version " + version)
		self.ui.openF.clicked.connect(self.openfile)
		self.ui.flashB.clicked.connect(self.flash)
		self.ui.comlist.addItems(portList)
		self.ui.speedlist.addItems(speeds)
		self.ui.speedlist.setCurrentIndex(5)
		self.ui.flashlist.addItems(flashsizes)
		self.ui.flashlist.setCurrentIndex(2)
		self.ui.modelist.addItems(flashmodes)
		self.ui.modelist.setCurrentIndex(2)
		self.ui.erase.clicked.connect(self.erase_flash)	
	def openfile(self):
		global fileName
		fileName = QFileDialog.getOpenFileName(self, "Open BIN File", openpath , "*.bin")
		if fileName[0] != '':
			self.ui.statusbar.showMessage("BIN file opened")
			print(fileName)
		else:
			self.ui.statusbar.showMessage("BIN file not opened. Please, try again.")
	def flash(self):
		if fileName == 0:
			self.ui.statusbar.showMessage("Error! Please, first open a BIN file")
		else:
			COM = self.ui.comlist.currentText()
			speed = self.ui.speedlist.currentText()
			flash = self.ui.flashlist.currentText()
			flashmode = self.ui.modelist.currentText()
			command = esptoolName + " -p " + COM + " -b " + speed + " write_flash " + "--flash_mode " + flashmode + " --flash_size " + flash + " 0x0 " +fileName[0]
			print(command)
			code = os.system(command)
			if code == -1 or code == 2 or code == 1:
				self.ui.statusbar.showMessage("Flash not sucess. Maybe you choose wrong port or BIN file?")
			else:
				self.ui.statusbar.showMessage("Flash sucess. Thanks for using ESP8266 Flasher")
	def erase_flash(self):
		COM = self.ui.comlist.currentText()
		self.ui.statusbar.showMessage("Start erasing")
		erase_command = "esptool.exe -p "+ COM + " erase_flash"
		print(erase_command)
		os.system(erase_command)
	def refresh(self):
		ports = QSerialPortInfo().availablePorts()
		for port in ports:
			portList.append(port.portName())



if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	portList = []
	ports = QSerialPortInfo().availablePorts()

	for port in ports:
		portList.append(port.portName())

	application = MainWindow()

	application.show()
	application.setWindowTitle("ESP8266 Flasher")
	app.exec()