import RPi.GPIO as GPIO
import time

delay = 0.005
rig1 = 23
rig2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(rig1, GPIO.OUT)
GPIO.setup(rig2, GPIO.OUT)
GPIO.output(rig1, GPIO.HIGH)
GPIO.output(rig2, GPIO.HIGH)

def hardReboot(relay):
    hardOff(relay)
    powerOn(relay)

def powerOn(relay):
    toggle(relay,0.5)

def powerOff(relay):
    toggle(relay,0.5)

def hardOff(relay):
    toggle(relay,6.5)

def toggle(relay,delay):
    GPIO.output(relay, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(relay, GPIO.HIGH)

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
    try:
        while True:
            powerOn(rig1)
            powerOn(rig2)
            time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
