"""VERIFICAR SIEMPRE EL PUERTO"""

import serial as serialProtocol
import time

usart = serialProtocol.Serial("/dev/ttyACM0", 9600, timeout = 1)
while True:
    if usart.inWaiting() > 0:
        dato = usart.read()
        dato_c = dato.decode()
        if dato_c == '*':
            let = ""
            while True:
                if usart.inWaiting() > 0:
                    dato = usart.read()
                    dato_c = dato.decode()
                    if dato_c != "#":
                        let = let + dato_c
                else:
                    print(let)
                    time.sleep(1)


                    
    