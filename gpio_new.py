# Write your code here :-)

import RPi.GPIO as GPIO
import time

# Deshabilitamos advertencias
GPIO.setwarnings(False)

# Desfinimos tipo de enumeracion
GPIO.setmode(GPIO.BCM)

# Definimos el pin 21 como salida con estado inicial en 0
GPIO.setup(21, GPIO.OUT)

# LOOP
while True:
   # Elegimos un pin (21) y lo ponemos en estado 1
    GPIO.output(21,True)
    time.sleep(1) # Tiempo en segundos
    # Elegimos un pin (21) y lo ponemos en estado 0
    GPIO.output(21, False)
    time.sleep(0.5) # Tiempo en segundos