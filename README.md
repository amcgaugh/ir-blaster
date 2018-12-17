# ir-blaster
Control your tv through voice or a webpage using Dialogflow + flask + LIRC on a raspberry pi!

## Wiring and LIRC
First things first, let's get LIRC on the raspberry pi. Credit to [piddler](http://www.piddlerintheroot.com/ir-blaster-lirc/) for the best instructions I found to get this part of the project working.

###Installing LIRC and Setting Up Dependencies
First let's install LIRC:

    sudo apt-get install lirc

Edit the modules file:

    sudo nano /etc/modules

Add the following to the file:

    lirc_dev
    lirc_rpi gpio_in_pin=18 gpio_out_pin=22

Next we'll edit the hardware file:

    sudo nano /etc/lirc/hardware.conf

Make sure your variables are set to the following:

    LIRCD_ARGS="--uinput"
    LOAD_MODULES=true
    DRIVER="default"
    DEVICE="/dev/lirc0"
    MODULES="lirc_rpi"
    LIRCD_CONF=""
    LIRCMD_CONF=""

Edit the boot config file:

    sudo nano /boot/config.txt

Add the following to the file:

    dtoverlay=lirc-rpi,gpio_in_pin=18,gpio_out_pin=22

Create an ir-remote.conf file:

    sudo nano /etc/modprobe.d/ir-remote.conf

And add the following to this file:
    
    options lirc_rpi gpio_in_pin=18 gpio_out_pin=22


###Testing out the IR Receiver
Do a reboot of the pi and then it's time to test out the IR Receiver. 

    sudo modprobe lirc_rpi

Then:

    sudo kill $(pidof lircd)

Run this command:
  
    mode2 -d /dev/lirc0

You should now be able to point your remote at your IR Receiver, and when you press any buttons you should see some output in the console. 

Exit when you've confirmed that the IR Receiver is setup correctly by pressing 'CTRL + C'

###Recording the IR Inputs


