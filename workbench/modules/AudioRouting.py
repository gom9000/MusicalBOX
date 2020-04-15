#
# AudioRouting.py
#           ___ _            _     ___ _   _ ___ 
# __ ___ __/ __(_)_ __  _ __| |___| _ ) | | / __|
# \ \ / '_ \__ \ | '  \| '_ \ / -_) _ \ |_| \__ \
# /_\_\ .__/___/_|_|_|_| .__/_\___|___/\___/|___/
#     |_|              |_|                       
#
# Author.....: Alessandro Fraschetti (mail: gos95@gommagomma.net)
# Target.....: RaspberryPI
# Version....: 1.0 2020/04/09
# Description: python driver module for audio-routing
# URL........: 
# License....: Creative Commons ShareAlike 3.0 (http://creativecommons.org/licenses/by-sa/3.0/)
#


import RPi.GPIO as GPIO
import time
import math


# ============================================================================
# AudioRouting
# ============================================================================
class AudioRouting:
    DELAY = 0.001


    # ------------------------------------------------------------------------
    # Inits the AudioRouting and sets control GPIO pins
    # ------------------------------------------------------------------------
    def __init__(self, data_pin, clock_pin, latch_pin, reset_pin):
        self.data_pin = data_pin
        self.clock_pin = clock_pin
        self.latch_pin = latch_pin
        self.reset_pin = reset_pin
        self.__last_sh = 0
        self.__last_sl = 0
        self.__last_linein = 0
        self.__last_lineout = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.data_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.latch_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.reset_pin, GPIO.OUT, initial=GPIO.HIGH)

		# reset bistable relays
        self.route(1,2)
        self.route(2,3)
        self.route(3,4)
        self.route(1,1)
		self.route(0,0)


    # ------------------------------------------------------------------------
    # Clean GPIO
    # ------------------------------------------------------------------------
    def __del__(self):
        GPIO.cleanup()


    # ------------------------------------------------------------------------
    # Send Reset to Registers (low-to-high)
    # ------------------------------------------------------------------------
    def resetpulse(self):
        GPIO.output(self.reset_pin, GPIO.LOW)
        time.sleep(self.DELAY)
        GPIO.output(self.reset_pin, GPIO.HIGH)


    # ------------------------------------------------------------------------
    # Send Pulse to Registers (high-to-low)
    # ------------------------------------------------------------------------
    def pulse(self, pin):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(self.DELAY)
        GPIO.output(pin, GPIO.LOW)


    # ------------------------------------------------------------------------
    # Send Data (set and reset) to Registers
    # ------------------------------------------------------------------------
    def senddata(self, ds, dr):

        # send reset data
        for ii in range(8):
            databit = bool(dr&int(math.pow(2, ii)))
            #print ("%s"% (databit)) 
            GPIO.output(self.data_pin, databit)
            self.pulse(self.clock_pin)

        # send set data
        for ii in range(8):
            databit = bool(ds&int(math.pow(2, ii)))
            #print ("%s"% (databit)) 
            GPIO.output(self.data_pin, databit)
            self.pulse(self.clock_pin)



    # ------------------------------------------------------------------------
    # route linein (1-to-3) to lineout (1-to-4)
    # ------------------------------------------------------------------------
    def route(self, linein, lineout):
        print ("linein-%d to lineout-%d"% (linein, lineout))

        if linein > 0 and linein < 4:
            sh = int(math.pow(2, linein-1))
        else:
            sh = 0

        if lineout > 0 and lineout < 5:
            sl = int(math.pow(2, lineout+2))
        else:
            sl = 0

        rh = self.__last_sh
        rl = self.__last_sl

        self.__last_sh = sh 
        self.__last_sl = sl 

        if linein == self.__last_linein:
            sh = 0
            rh = 0
        if lineout == self.__last_lineout:
            sl = 0
            rl = 0

        sx = sh + sl
        rx = rh + rl

        self.__last_linein = linein 
        self.__last_lineout = lineout 

        self.senddata(sh, rh)
        self.pulse(self.latch_pin)
        time.sleep(self.DELAY)
        self.resetpulse()
        self.pulse(self.latch_pin)
        time.sleep(self.DELAY)

        self.senddata(sl, rl)
        self.pulse(self.latch_pin)
        time.sleep(self.DELAY)
        self.resetpulse()
        self.pulse(self.latch_pin)
        time.sleep(self.DELAY)
