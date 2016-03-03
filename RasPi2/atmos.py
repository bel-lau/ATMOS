import picamera
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
arduino = 4
GPIO.setup(arduino,GPIO.IN)
camera = picamera.PiCamera()

start = 0
while start == 0:
        start = GPIO.input(arduino)
        if start == 1:
                break
        
# Capture video
camera.resolution = (640,480)
camera.start_recording('test.h264')
camera.wait_recording(5) #length of video
camera.stop_recording()
        
camera.resolution = (1024,768)
#second number is amount of pictures
for pic in range (0,3):
        camera.capture(str(pic) + '.jpg')
        time.sleep(10) #time between pictures
