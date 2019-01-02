# IR Blaster TV Control using Voice or GUI!
Control your tv with your voice or a GUI using Dialogflow + flask + LIRC with a Raspberry Pi & Google Assistant! See the the full project instructions at drewnay.com. Here is a quick video demonstrating what we'll be building:

VIDEO PLACEHOLDER

This project will be broken into 3 sections
1. Setting up LIRC, the 'Linux Infrared Remote Control' on the Raspberry Pi along with the wiring of the IR Emitter and Receiver. 
2. Creating the APIs and UI using Flask that will be used to control the various Remote Control commands that were setup in step 1
3. Setting up the Voice Skill using Google's Dialogflow and Actions. This tutorial will outline how to set the project up for Google Assistant to respond to various voice commands to hit the APIs you create in step 2. Alexa will be coming soon too!

Before you get started, here are the things you'll need for this project:
- [Raspberry Pi](https://www.raspberrypi.org/products/) 
- [IR Emitter LED and IR Receiver](https://www.amazon.ca/gp/product/B07FFQ9B9H/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)
- [Any Google Assistant Product](https://store.google.com/us/category/connected_home) 
- [Breadboard](https://www.amazon.com/BB400-Solderless-Plug-BreadBoard-tie-points/dp/B0040Z1ERO)
- [Jumper Cables](https://www.amazon.ca/Breadboard-Solderless-Prototype-Male-Female-Female-Female/dp/B0758CK1V4/ref=sr_1_1_sspa?ie=UTF8&qid=1546292926&sr=8-1-spons&keywords=arduino+jumper+cables&psc=1) 
- [BC547 Transistor](https://www.amazon.ca/Transistor-transistors-Assortment-2N2222-S9015-BC327-BC558/dp/B075TDNYJB/ref=sr_1_1?rps=1&ie=UTF8&qid=1546293038&sr=8-1&keywords=bc547&refinements=p_85%3A5690392011)
- [220 Ohm Resistor](https://www.amazon.ca/Haitronic-Resistor-Assortment-Education-Experiment/dp/B072Z72Y98/ref=sr_1_2_sspa?ie=UTF8&qid=1546293115&sr=8-2-spons&keywords=resistor+kit&psc=1)

Follow along in order to create your own Voice Controlled Remote! 
[Step 1](https://github.com/amcgaugh/ir-blaster/blob/master/LIRC/README.md)
[Step 2](https://github.com/amcgaugh/ir-blaster/blob/master/Flask%20APIs%20and%20UI/README.md)
[Step 3](https://github.com/amcgaugh/ir-blaster/blob/master/Dialogflow/README.md)
