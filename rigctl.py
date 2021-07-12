import RPi.GPIO as GPIO
from flask import Flask, render_template, request, redirect
import time

#rig name, description, GPIO pin
rigs = [['Rig1', 'AMD', 23], ['Rig2', 'NVIDIA', 24]]
ip = '192.168.201.187'
port = '44332'

app = Flask(__name__, template_folder='template')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ambientTemp = None

# Define relay pins as output
for rig in rigs:
	GPIO.setup(rig[2], GPIO.OUT)
	GPIO.setup(rig[2], GPIO.OUT)

# set gpio to HIGH (relays off)
for rig in rigs:
	GPIO.output(rig[2], GPIO.HIGH)
	GPIO.output(rig[2], GPIO.HIGH)

def initRigs ():
	for rig in rigs:
		rig.append('off')

def hardReboot(gpio):
    hardOff(gpio)
    time.sleep(1)
    powerOn(gpio)

def powerOn(gpio):
    toggle(gpio,0.5)

def shutdown(gpio):
    toggle(gpio,0.5)

def hardOff(gpio):
    toggle(gpio,6.5)

def toggle(gpio,delay):
    GPIO.output(gpio, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(gpio, GPIO.HIGH)
	
def update():
	ambientTemp = 0
	for rig in rigs:
		pass

@app.route("/")
def index():
	# Read GPIO Status
	templateData = {
		'rigs' : rigs,
		'ambientTemp' : ambientTemp,
    }
	return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	for rig in rigs:
		if not rig[0] == deviceName:
			continue
		else:
			gpio = rig[2]

			if action == "hardReboot":
				hardReboot(gpio)
				rig[3] = 'on'
			elif action == "powerOn":
				powerOn(gpio)
				rig[3] = 'on'
			elif action == "shutdown":
				shutdown(gpio)
				rig[3] = 'off'
			elif action == "hardOff":
				hardOff(gpio)
				rig[3] = 'off'
	templateData = {
		'rigs' : rigs,
		'ambientTemp' : ambientTemp,
    }
	return redirect('/')

if __name__ == "__main__":
	try:
		initRigs()
		app.run(host=ip, port=port, debug=True)

	except KeyboardInterrupt:
		GPIO.cleanup()
