# PART 1 - Wiring and LIRC

For wiring - follow the following schematic:

PLACEHOLDER FOR SCHEMATIC IMAGE

Next let's get LIRC on the raspberry pi. Credit to [piddler](http://www.piddlerintheroot.com/ir-blaster-lirc/) for the best instructions I found to get this part of the project working.

## Installing LIRC and Setting Up Dependencies
First let's install [LIRC](http://www.lirc.org):

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

Follow the instructions in the console - write a valid command (ie: KEY_POWER) and then press the corresponding button on the remote. When you are done with all the button's you want recorded check to make sure that the recordings were captured by running:

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
