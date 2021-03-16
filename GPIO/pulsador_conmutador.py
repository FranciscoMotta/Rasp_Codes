import RPi.GPIO as GPIO
import time

# GENERAL CONFIG
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # PINES POR GPIO

# CONFIG PINES

# SALIDAS -> LEDS
leds = 20, 21  # TUPLA DE LEDS DE SALIDA
GPIO.setup(leds, GPIO.OUT)

# ENTRADA -> PULSADOR PULL UP
pulsador = 16 
GPIO.setup(pulsador, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
   while True:
       if GPIO.input(pulsador) == False:
          print("Boton Conmutador: Activo")
          GPIO.output(leds, (GPIO.HIGH, GPIO.LOW))
          time.sleep(1)
          GPIO.output(leds, (GPIO.LOW, GPIO.HIGH))
          time.sleep(1)
       elif GPIO.input(pulsador) == True:
          GPIO.output(leds, (GPIO.LOW, GPIO.LOW))
except KeyboardInterrupt():
     GPIO.cleanup()

