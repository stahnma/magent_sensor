#!/usr/bin/env python

 
import RPi.GPIO as GPIO 
import time


GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

LED1 = 18
LED2 = 23
door1 = 12
door2 = 16


GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(door1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(door2, GPIO.IN, GPIO.PUD_UP)

GPIO.output(LED1, 0)
GPIO.output(LED2, 0)

while True:
   if GPIO.input(door1) == False:
       print("Door 1 is closed.")
       time.sleep(2)
   else:
     if GPIO.input(door1) == True:
       print("Door 1 is open.")
       time.sleep(2)       
   if GPIO.input(door2) == False:
       print("Door 2 is closed.")
       time.sleep(2)
   else:
     if GPIO.input(door2) == True:
       print("Door 2 is open.")
       time.sleep(2)
GPIO.cleanup()

