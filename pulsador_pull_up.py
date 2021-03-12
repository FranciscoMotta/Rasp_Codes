import RPi.GPIO as GPIO
import time

# Advertencias

GPIO.setwarnings(False)

# Enumeracion mediante GPIO

GPIO.setmode(GPIO.BCM) 

# Configuracion de PINES 

pushBotton = 21
led = 2 

# Configuramos el pulsador como entrada pull up

GPIO.setup(pushBotton, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Led

GPIO.setup(led, GPIO.OUT)

try:

	if GPIO.input(pushBotton) == False:
		print("pulsador presionado")
		GPIO.output(led, GPIO.HIGH)
		time.sleep(0.1)
	else:
		GPIO.output(led, GPIO.sLOW)

except KeyboardInterrupt:
    GPIO.cleanup()