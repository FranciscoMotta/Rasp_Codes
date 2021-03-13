import RPi.GPIO as GPIO 
import time 

# CONFIG GENERAL 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# PINES LEDS
pinesConfig = 4, 5, 6, 7, 8, 9
GPIO.setup(pinesConfig, GPIO.OUT)

# PINES PULSADORES
pinesBotonConf = 20 , 21
GPIO.setup(pinesBotonConf, GPIO.IN, pull_up_down = GPIO.PUD_UP)

botonIncremento = 20
botonDecremento = 21

cuentaBase = 3
ledPrendidos = 0

# LOOP

try:
    while True:
    if GPIO.input(botonIncremento) == False:
       ledPrendidos = cuentaBase + 1
       print("Boton de incremento presionado")
       time.sleep(1)
       if ledPrendidos > 9:
          ledPrendidos = 9
       else: 
           GPIO.output(ledPrendidos, GPIO.HIGH)

    elif GPIO.input(botonDecremeto) == False:
        GPIO.output(ledPrendidos, GPIO.LOW)
	print("Boton de decremento presionado")
        if ledPrendidos < 4:
            ledPrendidos = 4
        else:
            ledPresionado -= 1
    else:
        pass 

except KeyboardInterrupt():
       GPIO.cleanup()
