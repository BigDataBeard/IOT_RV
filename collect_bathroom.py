#!/usr/bin/python
import logging
import RPi.GPIO as GPIO
import time
import datetime

from logging.handlers import RotatingFileHandler

#GPIO SETUP
Number_1 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(Number_1, GPIO.IN)

Number_2  = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(Number_2, GPIO.IN)

Cleaning = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(Cleaning, GPIO.IN)

Dumped = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(Dumped, GPIO.IN)

#set path and name for log files
path = "/home/pi/Desktop/Bathroom/log/bathroom.log"

#create rotating log and set level
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

#specify the log size and log file count. 200 bytes will allow 3 logs per file
handler = RotatingFileHandler(path, maxBytes=200, backupCount=5)
logger.addHandler(handler)

#run by default

while 1:
    if GPIO.input(Number_1) == GPIO.LOW:
        #send output to log file
        logger.info("Time " + str(datetime.datetime.now()))
        logger.info ("Number 1 ")
        print ("Number 1")
        time.sleep(1)

        #send output to log file
    elif GPIO.input(Number_2) == GPIO.LOW:
        logger.info("Time " + str(datetime.datetime.now()))
        logger.info("Number 2 ")
        print ("Number 2")
        time.sleep(1)
        
    elif GPIO.input(Cleaning) == GPIO.LOW:
        logger.info("Time " + str(datetime.datetime.now()))
        logger.info("Cleaned ")
        print ("Cleaned")
        time.sleep (1)

    elif GPIO.input(Dumped) == GPIO.LOW:
        logger.info("Time " + str(datetime.datetime.now()))
        logger.info("Dumped ")
        print ("Dumped")
        time.sleep (1)
        

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)


