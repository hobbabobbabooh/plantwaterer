# External module imp
import RPi.GPIO as GPIO
import datetime
import time

init = False
pump_pin=8 # (GPIO14)
wsensor_pin=10 # (GPIO15)

GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme

def get_last_watered():
    try:
        f = open("last_watered.txt", "r")
        return f.readline()
    except:
        return "NEVER!"
      
def get_status(pin = wsensor_pin):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

def pump_switch(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
def auto_water(delay = 5):
    consecutive_water_count = 10
    pump_switch(pump_pin)
    print("Here we go! Press CTRL+C to exit")
    write_log("Pumped")
    try:
        while consecutive_water_count > 0:
#            time.sleep(delay)
#            wet = get_status(wsensor_pin) == 0
#            if not wet:
#                if consecutive_water_count < 5:
#                    pump_on(pump_pin, 1)
                consecutive_water_count -= 1
#            else:
#                consecutive_water_count = 0
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        write_log("Exit through input, GPIO cleanup started")
        GPIO.cleanup() # cleanup all GPI
        write_log("GPIO cleanup finished")
    except: #Catch addiutional exceptions.
        write_log("Error occured, GPIO cleanup started")
        GPIO.cleanup() # cleanup all GPI
        write_log("GPIO cleanup finished")        

def pump_on(delay = 1):
    pump_switch(pump_pin)
#    f = open("last_watered.txt", "w")
#    f.write("Last watered {}".format(datetime.datetime.now()))
#    f.close()
    write_log("Watering finished ")
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH)
    
def write_log (message)
    f = open("last_watered.txt", "a")
    f.write(message)
    f.write("{}".format(datetime.datetime.now()))
    f.close()
