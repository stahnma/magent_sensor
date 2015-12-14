#!/usr/bin/env python
 
import RPi.GPIO as GPIO 
import time
import datetime

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

fridge = 12
log = open('fridge.log', 'a')
laststate = 'closed'

GPIO.setup(fridge, GPIO.IN, GPIO.PUD_UP)

while True:
   if GPIO.input(fridge) == False:
       if laststate == "closed":
	 laststate = 'open'
	 ts = time.time() 
	 dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	 log.write(str(dt) + "," + str(ts) + "," + "open\n")
	 print(dt + " Refridgerator door is open.")
       time.sleep(2)
   else:
     if GPIO.input(fridge) == True:
       if laststate == "open":
	 laststate = 'closed'
	 ts = time.time() 
	 dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	 log.write(str(dt) + "," + str(ts) + "," + "closed\n")
	 print(dt + " Refridgerator door is closed.")
       time.sleep(2)       
GPIO.cleanup()
