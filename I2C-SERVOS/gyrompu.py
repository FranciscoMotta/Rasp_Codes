from mpu6050 import mpu6050

try: 
    sensor = mpu6050(0x68)
    print("MPU OK")
except:
    print("OOPS!")
