import RPi.GPIO as GPIO
import time 

# CONFIG GENERALES
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pin config
ledPinPwm = 21
GPIO.output(ledPinPwm, GPIO.OUT)

# PWM INIT

pinPwm = PWM.(ledPinPwm, 500) # PWM.(Canales (pin), Frecuencia (Hz)) 
led.start(100) # .start(%) porcentaje de activación del pulso en alto

while True:
    dutyCycle = int(input("Ingrese luminosidad 0 - 100 : "))
    led.ChanceDutyCycle(dutyCycle)
