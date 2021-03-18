from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton # Importamos la librería del Python Qt5
import sys

# Importamos la librería Serial

import serial 

usart = serial.Serial("/dev/ttyACM0", 9600, timeout = 1) # Nos conectamos por protocolo serial al Arduino


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
    
        # Label
        label1 = QLabel("¡hola mundo!", self)
        label1.move(50,50) # Coordenadas de impresión de texto
#         
#         label2 = QLabel("PUT HERE!", self)
#         label2.move(200,200)
#         
#                 
#         label2 = QLabel("PUT HERE!", self)
#         label2.move(350,350)
        # Boton
        
        button = QPushButton("Activar", self)
        button.move(100, 100)
        
        buttonOff = QPushButton("Desactivar", self)
        buttonOff.move(100, 200)
        
        button.clicked.connect(self.on)
        buttonOff.clicked.connect(self.off)
        
        
        self.show() # Mostramos la pantalla
    
    def off(self):
        print("BOTON DESACTIVAR")
        data = 'b'
        usart.write(data.encode()) # Enviamos el dato codificado para el Arduino
    
    def on(self):
        print("BOTON ACTIVAR")
        dat = 'a'
        usart.write(dat.encode()) # Enviamos el dato codificado para el Arduino
    
    
if __name__ == "__main__":
    
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_()) # Tiempo de presentación de la pantalla 


