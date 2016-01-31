#!/usr/bin/env python
 
import RPi.GPIO as GPIO 
import time
import datetime
import os
import sys

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

fridge = 12
log = open('/tmp/fridge.log', 'a')
laststate = 'closed'

GPIO.setup(fridge, GPIO.IN, GPIO.PUD_UP)

while True:
   sys.stdout.flush()
   if GPIO.input(fridge) == False:
       ts = time.time() 
       dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
       if laststate == "closed":
	 laststate = 'open'
	 log.write(str(dt) + "," + str(ts) + "," + "open\n")
         log.flush()
	 print(str(dt) + "," + str(ts) + "," + "fridge open")
       if os.environ.get('DEBUG'):
         print(str(dt) + "," + str(ts) + "," + "fridge open")
       time.sleep(2)
   else:
     if GPIO.input(fridge) == True:
       ts = time.time() 
       dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
       if laststate == "open":
	 laststate = 'closed'
	 log.write(str(dt) + "," + str(ts) + "," + "closed\n")
         log.flush()
	 print(str(dt) + "," + str(ts) + "," + "fridge closed")
       if os.environ.get('DEBUG'):
         print(str(dt) + "," + str(ts) + "," + "fridge closed")
       time.sleep(2)       
GPIO.cleanup()
