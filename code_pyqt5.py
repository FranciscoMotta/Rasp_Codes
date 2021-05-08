from PyQt5 import Qtwidgets
from PyQt5.Qtwidgets import QApplication, QMainWindow
import sys

def window():
	app = QApplication(sys.argv);
	win = QMainWindow()
	win.setGeometry(200, 200, 300, 300) # Xpos Ypos Width Height
	"""
	-----------------------------
	- 0,0                       -
	-                           - 
	-                           -
	-                           -
	-                           -
	-                           -
	-                           -
	-                 1980,1080 -
	-----------------------------
	"""
	win.setWindowTitle("Prueba GUI PYQT5")
	win.show()
	sys.exit(app.exec_())

window()