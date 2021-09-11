#!/usr/bin/python

"""
    Blink
    Turns an onboard LED on and off continuously,
    with intervals of 1 second.
"""

#import libraries
import Adafruit_BBIO.GPIO as GPIO
import time

#create a variable called led, which refers to the P9_14 pin
led = "P9_14"

#initialize the pin as an OUTPUT
GPIO.setup(led, GPIO.OUT)

#loop forever
while True:
    GPIO.output(led, GPIO.HIGH) #set P9_14 high - turn it on
    time.sleep(1) #stay idle for 1 second
    GPIO.output(led, GPIO.LOW) #set P9_14 low - turn it off
    time.sleep(1) #stay idle for 1 second
