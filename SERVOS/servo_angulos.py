import RPi.GPIO as GPIO
import time 

# CONFIG GENERALES
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# CONFIG PINES 
pinServo = 21
GPIO.setup(pinServo, GPIO.OUT)

# PWM INIT

pinPwm = GPIO.PWM(pinServo, 50) # Pin del servo definido trabajando a 50hz
pinPwm.start(10) # 10% -> 2ms = 180°

while True:
    anguloDeGiro = int(input("Ingrese ángulo de giro 0 - 180: "))
    tiempo_ms = (anguloDeGiro*2)/180
    porcentajeActiv = (tiempo_ms*10)/2
    pinPwm.ChangeDutyCycle(porcentajeActiv)
    print("El porcentaje de giro es: ", porcentajeActiv)
