# ir-blaster
Control your tv through voice or a webpage using Dialogflow + flask + LIRC on a raspberry pi!

## Wiring and LIRC
The first step to get everything working is to setup LIRC on the raspberry pi and connect the IR LED and IR Receiver. First things first, let's get LIRC on the raspberry pi. Credit to [piddler](http://www.piddlerintheroot.com/ir-blaster-lirc/) for the best instructions I found to get this working. 
First let's install LIRC:
'sudo apt-get install lirc'
