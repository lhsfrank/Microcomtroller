#!/usr/bin/python

#import libraries
import Adafruit_BBIO.GPIO as GPIO
import time

#create a variable called button, which refers to the P8_11 pin
button = "P8_11"

#initialize the pin as an INPUT
GPIO.setup(button, GPIO.IN) # Initialize P8_11 as an input

#loop forever
while True:
  if GPIO.input(button) == True: # Checks if the pin is HIGH
    print("HIGH")
  time.sleep(0.01) # In order to not overburden the CPU
