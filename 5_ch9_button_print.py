#!/usr/bin/python

#import libraries
import Adafruit_BBIO.GPIO as GPIO
import time

button = "P8_11" # create a variable called button, which refers to the P8_11 pin
count = 0 # create a variable called count and initialize it with the value zero.

# This variable will count the number of times the button was pressed.
GPIO.setup(button, GPIO.IN) #initialize the pin as an INPUT
GPIO.add_event_detect(button, GPIO.RISING) #adds an event to detect. In this case, the rising edge of pin P8_11.

#loop forever
while True:
    if GPIO.event_detected(button) == True: # if a rising edge is detected, run the code below
        count = count + 1 #increment the variable count
        print("Button was pressed " + str(count) + " times!")
    time.sleep(0.01) # in order to not overburden the CPU
