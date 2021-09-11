#!/usr/bin/python

import Adafruit_BBIO.UART as UART
import serial
import time

UART.setup("UART2")

ser2 = serial.Serial(port = "/dev/ttyO2", baudrate=9600)

ser2.close()

ser2.open()

while True:
    if ser2.isOpen():
        ser2.write("This is a message from UART2!\n")
        rxbuf = ser2.readline()
        print(rxbuf)
        time.sleep(0.05)
