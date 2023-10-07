from periphery import GPIO
import requests
import time

time.sleep(30)

buttonPin = 134  # GPIO pin 134 physical pin 38
LEDPin = 72  # GPIO pin 72 physical 5

buttonGPIO = GPIO(buttonPin, "in")
LEDGPIO = GPIO(LEDPin, "out")

url = 'http://gss.pad.iclr/api/ignition'
headers = {'Content-type': 'application/json'}
data = '{}'

while True:
    try:
        buttonValue = buttonGPIO.read()
        if buttonValue:
            print("Fire!")
            LEDGPIO.write(True)
            launchSignal = requests.post(url, headers=headers, data=data)
        else:
            print("Don't Fire!")
            LEDGPIO.write(False)
    except IOError:
        print(IOError)
