import sys
import time
import RPi.GPIO as io
import subprocess
import Tkinter as tk
 
io.setmode(io.BCM)
SHUTOFF_DELAY = 6  # seconds
PIR_PIN = 7
root = tk.Tk()
 
def main():
    io.setup(PIR_PIN, io.IN)
    turned_off = False
    last_motion_time = time.time()
 
    while True:
        if io.input(PIR_PIN):
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
            if not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY):
                turned_off = True
                turn_off()
        time.sleep(.1)
 
def turn_on():
    subprocess.call("sh /home/pi/Documents/smart-mirror/screen_on.sh", shell=True)
    subprocess.call("sh /home/pi/Documents/smart-mirror/splash1.sh", shell=True)
    #subprocess.call("sh /home/pi/Documents/smart-mirror/smartmirror1.sh", shell=True)
    time.sleep(5)

def turn_off():
    subprocess.call("sh /home/pi/Documents/smart-mirror/screen_off.sh", shell=True)
 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()
