#!/usr/bin/env python

 
import RPi.GPIO as GPIO 
import time


GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

LED1 = 18
door1 = 12


GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(door1, GPIO.IN, GPIO.PUD_UP)

GPIO.output(LED1, 0)

while True:
   if GPIO.input(door1) == False:
       print("Door 1 is open.")
       time.sleep(2)
   else:
     if GPIO.input(door1) == True:
       print("Door 1 is touching.")
       time.sleep(2)       
GPIO.cleanup()
