import RPi.GPIO as GPIO
import time

# IMPORTAMOS LIBRERIA DEL MPU6050

from mpu6050 import mpu6050
import numpy as np

"""CONFIGURACIóN GENERALES"""
GPIO.setwarnings(False) # Deshabilitadas las advertencias
GPIO.setmode(GPIO.BCM) # Enumeración de pines por GPIO

"""CONFIGURACIÓN PERIFéRICOS"""
# Comando Linux deteción de I2C -> sudo i2cdectect -y 1
# SDA - SCL -> GPIO2 - GPIO3
# Resistencias PULL_UP integradas en el módulo MPU6050
# Envio de la dirección del esclavo necesitado
"""     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
"""
sensor = mpu6050(0x68) # Detectado por consola SLAVE ADRESS 
while True:
    accelerometer_data = sensor.get_accel_data()
    print(acelerometer_data)
    time.sleep(1)
