from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,  QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1000, 200, 500, 500)
    win.setWindowTitle("Tech With Francisco")

    label = QtWidgets.QLabel(win)
    label.setText("Miguelon se la come")
    label.move(60, 60)

    win.show()
    sys.exit(app.exec_())

window() 