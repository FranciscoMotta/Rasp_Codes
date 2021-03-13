import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pinLed = 4
pinPushBoton = 21

GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(pinPushBoton, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
	if GPIO.input(pinPushBoton) == False:
	   print("Boton presionado")
	   GPIO.output(pinLed, GPIO.HIGH)
	   time.sleep(0.1)


except KeyboardInterrupt():
	GPIO.cleanup()
