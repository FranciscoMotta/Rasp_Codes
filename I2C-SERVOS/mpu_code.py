from mpu6050 import mpu6050

try:
    # Sensor
    sensor =mpu6050(0x68)
    # Mensaje
    print("MPU OK")
except:
    print("MPU NOT OK")