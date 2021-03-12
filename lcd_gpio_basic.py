import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # Desactivadas las advertencias
GPIO.setmode(GPIO.BCM) # Enumeración por GPIO

# PINES

pinRs = 2
pinEnable = 3

LCD0 = 4
LCD1 = 5
LCD2 = 6
LCD3 = 7
LCD4 = 8
LCD5 = 9
LCD6 = 10
LCD7 = 11

try:
    # CONFIG PINES SALIDA
    GPIO.setup(pinEnable, GPIO.OUT)
    GPIO.setup(pinRs, GPIO.OUT)

    GPIO.setup(LCD0, GPIO.OUT)
    GPIO.setup(LCD1, GPIO.OUT)
    GPIO.setup(LCD2, GPIO.OUT)
    GPIO.setup(LCD3, GPIO.OUT)
    GPIO.setup(LCD4, GPIO.OUT)
    GPIO.setup(LCD5, GPIO.OUT)
    GPIO.setup(LCD6, GPIO.OUT)
    GPIO.setup(LCD7, GPIO.OUT)

    # Modo comando

    GPIO.output(pinRs, GPIO.LOW)
    GPIO.output(pinEnable, GPIO.LOW)
    time.sleep(0.001)
    # Datos de configuracion

    """PRIMER DATO 0X01"""
    GPIO.output(LCD0,GPIO.HIGH)
    GPIO.output(LCD1,GPIO.LOW)
    GPIO.output(LCD2,GPIO.LOW)
    GPIO.output(LCD3,GPIO.LOW)
    GPIO.output(LCD4,GPIO.LOW)
    GPIO.output(LCD5,GPIO.LOW)
    GPIO.output(LCD6,GPIO.LOW)
    GPIO.output(LCD7,GPIO.LOW)

    GPIO.output(pinEnable, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(pinEnable, GPIO.LOW)
    time.sleep(0.001)
    """SEGUNDO DATO 0X38"""
    GPIO.output(LCD0,GPIO.LOW)
    GPIO.output(LCD1,GPIO.LOW)
    GPIO.output(LCD2,GPIO.LOW)
    GPIO.output(LCD3,GPIO.HIGH)
    GPIO.output(LCD4,GPIO.HIGH)
    GPIO.output(LCD5,GPIO.HIGH)
    GPIO.output(LCD6,GPIO.LOW)
    GPIO.output(LCD7,GPIO.LOW)

    GPIO.output(pinEnable, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(pinEnable, GPIO.LOW)
    time.sleep(0.001)

    """TERCER DATO 0X06"""
    GPIO.output(LCD0,GPIO.LOW)
    GPIO.output(LCD1,GPIO.HIGH)
    GPIO.output(LCD2,GPIO.HIGH)
    GPIO.output(LCD3,GPIO.LOW)
    GPIO.output(LCD4,GPIO.LOW)
    GPIO.output(LCD5,GPIO.LOW)
    GPIO.output(LCD6,GPIO.LOW)
    GPIO.output(LCD7,GPIO.LOW)

    GPIO.output(pinEnable, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(pinEnable, GPIO.LOW)
    time.sleep(0.001)

    """CUARTO DATO 0X0C"""
    GPIO.output(LCD0,GPIO.LOW)
    GPIO.output(LCD1,GPIO.LOW)
    GPIO.output(LCD2,GPIO.HIGH)
    GPIO.output(LCD3,GPIO.HIGH)
    GPIO.output(LCD4,GPIO.LOW)
    GPIO.output(LCD5,GPIO.LOW)
    GPIO.output(LCD6,GPIO.LOW)
    GPIO.output(LCD7,GPIO.LOW)

    GPIO.output(pinEnable, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(pinEnable, GPIO.LOW)
    time.sleep(0.001)

    # MODO CARACTER


    GPIO.output(pinRs, GPIO.HIGH)
    time.sleep(0.001)

    """FRASE -> HOLA
    PASAMOS LAS LETRAS A HEXADECIMAL ASCII
    H -> 01001000
    O -> 01001111
    L -> 01001100
    A -> 01000001
    """

    """PRIMER DATO H"""
    GPIO.output(LCD0,GPIO.LOW)
    GPIO.output(LCD1,GPIO.LOW)
    GPIO.output(LCD2,GPIO.LOW)
    GPIO.output(LCD3,GPIO.LOW)
    GPIO.output(LCD4,GPIO.LOW)
    GPIO.output(LCD5,GPIO.HIGH)
    GPIO.output(LCD6,GPIO.HIGH)
    GPIO.output(LCD7,GPIO.LOW)

    GPIO.output(pinEnable, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(pinEnable, GPIO.LOW)
    time.sleep(0.001)

    """SEGUNDO DATO O"""
    GPIO.output(LCD0,GPIO.HIGH)
    GPIO.output(LCD1,GPIO.HIGH)
    GPIO.output(LCD2,GPIO.HIGH)
    GPIO.output(LCD3,GPIO.HIGH)
    GPIO.output(LCD4,GPIO.LOW)
    GPIO.output(LCD5,GPIO.LOW)
    GPIO.output(LCD6,GPIO.HIGH)
    GPIO.output(LCD7,GPIO.LOW)

    GPIO.output(pinEnable, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(pinEnable, GPIO.LOW)
    time.sleep(0.001)

    """TERCER DATO L"""
    GPIO.output(LCD0,GPIO.LOW)
    GPIO.output(LCD1,GPIO.LOW)
    GPIO.output(LCD2,GPIO.LOW)
    GPIO.output(LCD3,GPIO.HIGH)
    GPIO.output(LCD4,GPIO.LOW)
    GPIO.output(LCD5,GPIO.LOW)
    GPIO.output(LCD6,GPIO.HIGH)
    GPIO.output(LCD7,GPIO.LOW)

    GPIO.output(pinEnable, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(pinEnable, GPIO.LOW)
    time.sleep(0.001)

    """CUARTO DATO A"""
    GPIO.output(LCD0,GPIO.HIGH)
    GPIO.output(LCD1,GPIO.LOW)
    GPIO.output(LCD2,GPIO.LOW)
    GPIO.output(LCD3,GPIO.LOW)
    GPIO.output(LCD4,GPIO.LOW)
    GPIO.output(LCD5,GPIO.LOW)
    GPIO.output(LCD6,GPIO.HIGH)
    GPIO.output(LCD7,GPIO.LOW)

    GPIO.output(pinEnable, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(pinEnable, GPIO.LOW)
    time.sleep(0.001)
except KeyboardInterrupt:
        GPIO.cleanup() # Limpiamos el GPIO
