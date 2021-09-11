#!/usr/bin/python
import Adafruit_BBIO.PWM as PWM
import time

RGB = ["P9_14", "P9_16", "P8_13"]
#RGB[0] controls red, RGB[1] controls green, RGB[2]controls blue

for i in range(0, 3): #runs the indented code below 3 times
    PWM.start(RGB[i], 0) #initialize PWM with all leads OFF

#set initial conditions
c_initial = RGB[0]
c_next = RGB[1]
c_off = RGB[2]

while True:
    PWM.set_duty_cycle(c_off, 0)
    for i in range(0, 100):
        PWM.set_duty_cycle(c_initial, 100-i)
        PWM.set_duty_cycle(c_next, i)
        time.sleep(0.05) #change this line for faster/slower fading speed
    #swap the colors in the following order: R->G->B->Repeat
    aux = c_initial
    c_initial = c_next
    c_next = c_off
    c_off = aux
