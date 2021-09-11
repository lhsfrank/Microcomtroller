#!/usr/bin/python

#import libraries
import Adafruit_BBIO.GPIO as GPIO
import time

#create a variable called button, which refers to the P8_11 pin
button = "P8_11"

#initialize the pin as an INPUT
GPIO.setup(button, GPIO.IN)

#loop forever
while True:
  GPIO.wait_for_edge(button, GPIO.RISING) #blocks the program until a rising edge happens on pin P8_11.
  print("HIGH")
  GPIO.wait_for_edge(button, GPIO.FALLING) #blocks the program until a falling edge happens on pin P8_11.
  print("LOW")
