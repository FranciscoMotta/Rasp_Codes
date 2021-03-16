import RPi.GPIO as GPIO
import time 

#  CONFIGURACIONES GENERALES
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# GPIO PINES 
pinLed = 4
GPIO.setup(pinLed, GPIO.OUT)

pinBoton = 21
GPIO.setup(pinBoton, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
   while True:
        while GPIO.intput(pinBoton) == False:
              print("Boton presionado")
              GPIO.output(pinLed, GPIO.HIGH)
        GPIO.output(ledPin, GPIO.LOW)
except KeyboardInterrupt():
       GPIO.cleanp()
