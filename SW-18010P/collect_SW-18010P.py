#!/usr/bin/python
import logging
import RPi.GPIO as GPIO
import time
import datetime

from logging.handlers import RotatingFileHandler

#GPIO SETUP
Vibration = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(Vibration, GPIO.IN)

#set path and name for log files
path = "/home/pi/Desktop/SW-18010P/log/vibration.log"

#create rotating log and set level
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

#specify the log size and log file count. 200 bytes will allow 3 logs per file
handler = RotatingFileHandler(path, maxBytes=220, backupCount=5)
logger.addHandler(handler)

#run by default

while 1:
    if GPIO.input(Vibration) == GPIO.LOW:
        #send output to log file
        logger.info("Time " + str(datetime.datetime.now()))
        logger.info ("Vibration Detected ")
        print ("Vibration Detected")
        time.sleep(1)

   # elif GPIO.input(Dumped) == GPIO.LOW:
        #logger.info("Time " + str(datetime.datetime.now()))
        #logger.info("Dumped ")
        #print ("Dumped")
        #time.sleep (1)
        

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)




