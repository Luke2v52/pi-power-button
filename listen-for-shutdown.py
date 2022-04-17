#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess

#Use BCM numbers (GPIO #'s)
GPIO.setmode(GPIO.BCM)

#Initial GPIO values on boot
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)

#New GPIO values after shutdown
GPIO.wait_for_edge(3, GPIO.FALLING)
GPIO.output(4, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

#Pi Shutdown
subprocess.call(['shutdown', '-h', 'now'], shell=False)
