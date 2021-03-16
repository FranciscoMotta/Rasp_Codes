# MPU6050

from mpu6050 import *


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
try:
    sensor_mpu_6050 = mpu6050(0x68)
    print("MPU6050 OK")
    acele_data = sensor_mpu_6050.get_accel_data()
    print(acele_data)
    print(type(acele_data))
except:
    print("OPPS!!")

