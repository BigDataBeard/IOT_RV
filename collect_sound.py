import logging
import time
import RPi.GPIO as GPIO
import sound
import datetime

from logging.handlers import RotatingFileHandler

## initalize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

#read data using pin 10
instance = sound.SOUND(pin=10)

#set path and name for log files
path = "/home/pi/Desktop/Sound/log/sound.log"

#create rotating log and set level
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

#specify the log size and log file count.200 bytes will allow 3 logs per file
handler = RotatingFileHandler(path, maxBytes=500, backupCount=5)
logger.addHandler(handler)

#run by default

try:
        while True:
            result = instance.read()
            if result.is_valid():
                #send output to log file
                logger.info("Sound Detected!" + str(Sound.Detected))
                        #send output to shell
                print("Sound Detected! " + str(Sound.Detected))

            time.sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

