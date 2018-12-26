# ir-blaster (LIRC Setup)
Control your tv with your voice or a GUI using Dialogflow + flask + LIRC with a Raspberry Pi & Google Assistant! See the the full project instructions at drewnay.com. Here is a quick video demonstrating what we'll be building:

VIDEO PLACEHOLDER

Things you'll need:
- Raspberry Pi
- IR Led
- IR Receiver
- Google Home 
- Wires 
- Transistor
- Resistor

## PART 1 - Wiring and LIRC
First things first, let's get LIRC on the raspberry pi. Credit to [piddler](http://www.piddlerintheroot.com/ir-blaster-lirc/) for the best instructions I found to get this part of the project working.

## Installing LIRC and Setting Up Dependencies
First let's install LIRC:

    $ sudo apt-get install lirc

Edit the modules file:

    $ sudo nano /etc/modules

Add the following to the file:

    lirc_dev
    lirc_rpi gpio_in_pin=18 gpio_out_pin=22

Next we'll edit the hardware file:

    $ sudo nano /etc/lirc/hardware.conf

Make sure your variables are set to the following:

    LIRCD_ARGS="--uinput"
    LOAD_MODULES=true
    DRIVER="default"
    DEVICE="/dev/lirc0"
    MODULES="lirc_rpi"
    LIRCD_CONF=""
    LIRCMD_CONF=""

Edit the boot config file:

    $ sudo nano /boot/config.txt

Add the following to the file:

    dtoverlay=lirc-rpi,gpio_in_pin=18,gpio_out_pin=22

Create an ir-remote.conf file:

    $ sudo nano /etc/modprobe.d/ir-remote.conf

And add the following to this file:
    
    options lirc_rpi gpio_in_pin=18 gpio_out_pin=22


## Testing out the IR Receiver
Do a reboot of the pi and then it's time to test out the IR Receiver. 

    $ sudo modprobe lirc_rpi

Then:

    $ sudo kill $(pidof lircd)

Run this command:
  
    $ mode2 -d /dev/lirc0

You should now be able to point your remote at your IR Receiver, and when you press any buttons you should see some output in the console. 

Exit when you've confirmed that the IR Receiver is setup correctly by pressing 'CTRL + C'

## Recording the IR Inputs
First run this command: 
    
    $ sudo kill $(pidof lircd)

then:

    $ irrecord -d /dev/lirc0 ~/lircd.conf

Follow the instructions in the console - write the command (ie KEY_POWER) and then press the corresponding button on the remote. When you are done with all the button's you want recorded check to make sure that the recordings were captured by running:

    $ nano home/pi/lircd.conf

Then you will copy this file over to the /etc/lirc directory:

    $ sudo cp /home/pi/lircd.conf /etc/lirc/lircd.conf

Restart LIRC:

    $ sudo /etc/init.d/lirc restart 

Before you do start issuing commands, quickly run this command then you're ready to see the IR LED in action:

    $ sudo lircd --device /dev/lirc0

## Test it out!
To see one of your commands in action try the following command (replace KEY_POWER) with any of the other commands you mapped out to see them work too!):

    $ irsend SEND_ONCE /home/pi/lircd.conf KEY_POWER

And there you have it, you have a working raspberry pi IR Remote that can replay any of your commands. It's also worth noting that you don't need to map out all of the remote commands if your remote is listed [in here](http://lirc-remotes.sourceforge.net/remotes-table.html) (replace the lircd.conf file with the one from the site). 

## PART 2 - Flask APIs with a pretty Remote UI!

First thing we'll be creating are the APIs using Flask so that we can hit them from the Dialogflow events or through the GUI to send commands to the IR led.

First we will install Pip and Flask:

    $ sudo apt-get install python-pip
    $ sudo pip install flask

Next create a file called irblaster.py with the following code:

    $ nano irblaster.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello there - Flask is working!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
```

Test out the server to make sure it's working by going running it:

    python irblaster.py
    
Navigate to 0.0.0.0:5000 in your browser and you should see 'Hello there - Flask is working!'. Stop the server by running CTRL+C. 

Now we're going to add a new endpoint that will let us control the IR LED. If you look we've added a new route '/api/<remotecontrol>' where replacing '<remotecontrol>' with 'poweron' will send the system command "irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER". You can add a bunch of if-else or use switch-case statements to add any other irsend commands that you configured from STEP 1 of this tutorial. 

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello there - Flask is working!'

@app.route('/api/v1/<remotecontrol>')
def controlremote(remotecontrol):
    if remotecontrol == "poweron"
    	os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
	return 'performing the following remote control action: ' + remotecontrol

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
```
Save the file and run the server again with the following command: 

    python irblaster.py

Next test out your new API endpoint using the browser again. We'll switch the API to a POST request later on with a body (we'll need to for it to work with dialogflow / google assistant). Entering 0.0.0.0:5000/api/v1/poweron into a browser this time should actually envoke the POWER_ON command and turn on the tv! Switch 'poweron' to any other mapping you did to see your API now configured to work with any of your commands!

## Building the Remote Control GUI webpage

Great - now that we have the APIs working to control the IR LED we'll create a simple webpage that can be used to trigger the various remote control commands too!

Let's create an index.html

Next we'll do change our irblaster.py file to import render_template in order to use our newly created index.html page. This will allow the page to render when hitting the Flask server's root endpoint:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/api/v1/<remotecontrol>')
def controlremote(remotecontrol):
    if remotecontrol == "poweron"
    	os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
	return 'performing the following remote control action: ' + remotecontrol

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
```

Next thing we'll be building is the pretty front end remote control so that you can just as easily control you tv through a web page. 
