#!/usr/bin/env python

 
import RPi.GPIO as GPIO 
import time
import datetime

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

fridge = 12

log = open('fridge.log', 'a')

GPIO.setup(fridge, GPIO.IN, GPIO.PUD_UP)

while True:
   if GPIO.input(fridge) == False:
       ts = time.time() 
       dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
       log.write(ts + "," + dt + "," + "closed\n")
       print(dt + " - Refridgerator 1 is open.")
       time.sleep(2)
   else:
     if GPIO.input(fridge) == True:
       ts = time.time() 
       dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
       log.write(str(dt) + "," + str(ts) + "," + "closed.\n")
       print(dt + " - Door is now closed.")
       time.sleep(2)       
GPIO.cleanup()
