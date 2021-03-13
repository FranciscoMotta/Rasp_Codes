import RPi.GPIO as GPIO
import time

# Configuración de advertencias
GPIO.setwarnings(False)
# Enumeracion de pines por GPIO
GPIO.setmode(GPIO.BCM)
# Config pines
GPIO.setup(21, GPIO.OUT)
try:
    while True:
        GPIO.output(21, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(21, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt():
    GPIO.cleanup()
