import RPi.GPIO as GPIO
import time 

# CONFIG GENERALES
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pin config
ledPinPwm = 21
GPIO.setup(ledPinPwm, GPIO.OUT)

# PWM INIT

pinPwm = GPIO.PWM(ledPinPwm, 500) # PWM.(Canales (pin), Frecuencia (Hz)) 
pinPwm.start(100) # start(%) porcentaje de activación del pulso en alto

while True:
    dutyCycle = int(input("Ingrese luminosidad 0 - 100 : "))
    pinPwm.ChangeDutyCycle(dutyCycle)
