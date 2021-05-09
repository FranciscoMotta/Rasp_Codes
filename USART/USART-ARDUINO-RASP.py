import serial # Importamos la librería de la comunicación serial
usart = serial.Serial("/dev/ttyACM0", 9600, timeout = 1) # Puerto = /dev/ttyACM0 escaneado -> python -m serial.tools.list_ports
# ls /dev/ttyACM*
# 9600 BAUDIOS = ARDUINO
# timeout = 1 -> tiempo de espera para la conexión

def enviar(): # Creamos una funcion
    dat = input("ingrese a o b: ") # Preguntamos por un dato
    usart.write(dat.encode()) # Enviamos el dato codificado para el Arduino
    
while True:
    enviar() # Llamamos a la funcion para enviar el dato