"""ASEGURARSE DE QUE EL CÓDIGO ESTÉ EN LA MISMA CARPETA QUE LA LIBRERÍA DESCARGAR DEL MPU6050 PARA QUE FUNCIONE"""

import RPi.GPIO as GPIO
import time

#############################

from mpu6050 import mpu6050

#############################

# CONFIGURACIONES GENERALES

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# CONFIG PINES

servoPin = 21
GPIO.setup(servoPin, GPIO.OUT) # Pin 21 como salida

# PWM

angulo = GPIO.PWM(servoPin, 50) # Pin 21 PWM a 50 hz
angulo.start(5)

# SENSOR MPU6050

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
    sensor = mpu6050(0x68) # Conectamos con el sensor
    
    # Constantes
    
    angulo_inicial = 90 # Angulo inicial
    delta_t = 0.1 # Periodo de muestreo
    
    while True:
        print("%%%%%%%%%%%%%%%%%%%%%%%")
        aceleracion_data = sensor.get_accel_data() # Obtenemos la aceleración angular
        acel_z_axis = aceleracion_data['z'] # Obtenemos la aceleración en el eje Z
        print(acel_z_axis) # Presentamos la aceleracion en el eje z
        velocidad_data = sensor.get_gyro_data() # Obtenemos la velocidad angugar
        vloc_z_axis = velocidad_data['z']
        print(vloc_z_axis) # Presentamos la velocidad en el eje Z
        angulo_actual = angulo_inicial + vloc_z_axis*delta_t # Obtenemos la velocidad en el eje Z
        
        tiempo_ms = (angulo_actual*2)/180
        porcentajeActiv = (tiempo_ms*10)/2
        
        angulo_inicial = angulo_actual # Hacemos la retroalimentación del ángulo pasado y el actual
        print("Angulo : ", angulo_actual) # Presentamos el ángulo
        
        """
        PWM periodo = 20ms -> 50hz 
        GRADOS DE FUNCIONAMIENTO = 0 - 180° -> 1 - 2ms
        180 = 2 ms -> 10%
        grados = x ms -> x%
        tiempo_ms = grados*2/180 -> tiempo en ms
        2 = 10% de 20ms
        tiempo_ms = porcentaje   
        tiempo_ms = 2*porcentaje/10
        porcentaje = tiempo_ms*10/2

        """
        
        angulo.ChangeDutyCycle(porcentajeActiv)
        print("El porcentaje de giro es: ", porcentajeActiv)
        time.sleep(1)
        
except:
    print("OOPS!")

