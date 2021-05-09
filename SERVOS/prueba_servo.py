import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

servo1 = GPIO.PWM(21, 50)
servo1.start(7.5)

while True:
    dc = int(input("Ingrese un numero 5 - 10: "))
    servo1.ChangeDutyCycle(dc)
