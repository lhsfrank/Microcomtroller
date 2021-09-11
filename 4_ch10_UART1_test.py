#!/usr/bin/python

import Adafruit_BBIO.UART as UART
import serial
import time

UART.setup("UART1")

ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)

ser1.close()

ser1.open()

while True:
    if ser1.isOpen():
        ser1.write("This is a message from UART1!\n")
        rxbuf = ser1.readline()
        print(rxbuf)
        time.sleep(0.05)
