import RPi.GPIO as GPIO
import time 

# PINES 

GPIO.setwarnings(False) # Advertencias deshabilitadas
GPIO.setmode(GPIO.BCM) # Enumeración de acuerdo al GPIO

# Pines de control del lcd

control = 2,3 # RS-ENABLE
lcd_display = 4,5,6,7,8,9,10,11 # LCD0-LCD7

# CONFIGURACION DE PINES 

GPIO.setup(control, GPIO.OUT) # PINES DE CONTROL COMO SALIDA
GPIO.setup(lcd_display, GPIO.OUT) # PINES DE DATOS LCD0-LCD7

# LOOP 

try:
	"""MODO COMANDO -> CONFIG = 0X01, 0X38, 0X06 0X0C"""

	GPIO.output(control, (False, False))
	time.sleep(0.001)

	# ENVIO DE DATOS DE CONFIGURACION
	# 0X01 -> 0b0000 0001

	GPIO.output(lcd_display, (True, False, False, False, False, False, False, False))

	# TIEMPO DE ENABLE

	GPIO.output(control, (False, True))
	time.sleep(0.001)
	GPIO.output(control, (False, False))
	time.sleep(0.001)

	# 0X38 -> 0b0011 1000

	GPIO.output(lcd_display, (False, False, False, True, True, True, False, False))

	# TIEMPO DE ENABLE

	GPIO.output(control, (False, True))
	time.sleep(0.001)
	GPIO.output(control, (False, False))
	time.sleep(0.001)

	# 0X06 -> 0b0000 0110

	GPIO.output(lcd_display, (False, True, True, False, False, False, False, False))

	# TIEMPO DE ENABLE

	GPIO.output(control, (False, True))
	time.sleep(0.001)
	GPIO.output(control, (False, False))
	time.sleep(0.001)

	# 0X0C -> 0b0000 1100

	GPIO.output(lcd_display, (False, False, True, True, False, False, False, False))

	# TIEMPO DE ENABLE

	GPIO.output(control, (False, True))
	time.sleep(0.001)
	GPIO.output(control, (False, False))
	time.sleep(0.001)

	"""MODO CARACTER: MENSAJE -> HOLA""" 

	GPIO.output(control, (True, False))

	time.sleep(0.001)

	# LETRA H -> 0b0100 1000

	GPIO.output(lcd_display, (False, False, False, True, False, False, True, False))

	# TIEMPO DE ENABLE

	GPIO.output(control, (False, True))
	time.sleep(0.001)
	GPIO.output(control, (False, False))
	time.sleep(0.001)

except KeyboardInterrupt():
	GPIO.cleanup() 