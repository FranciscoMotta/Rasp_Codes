import RPi.GPIO as GPIO
import time

# CONFIG GENERAL
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# PINES
leds = 20, 21
GPIO.setup(leds, GPIO.OUT)

try:
   while True:
       print("led conmutados retardo: 1 seg")
       GPIO.output(leds, (True, False))
       time.sleep(1)
       GPIO.output(leds, (False, True))
       time.sleep(1)
except KeyboardInterrupt():
     GPIO.cleanup()
