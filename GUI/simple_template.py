from PyQt5.QtWidgets import QWidget, QApplication # Importamos la librería del Python Qt5
import sys

class App(QWidget):
    def __init__(self):
        
        super().__init__()
        
        self.tittle = "Curso RPI4"
        self.m = 200 # X
        self.n = 200 # Y
        self.alto = 600
        self.ancho = 1000
        
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle(self.tittle) # Ponemos título a la ventana
        self.setGeometry(self.m, self.n, self.ancho, self.alto) # Definimos las dimenciones de la ventana
        self.show() # Mostramos la pantalla
        
if __name__ == "__main__":
    
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_()) # Tiempo de presentación de la pantalla 



