# PART 2 - Flask APIs with a pretty Remote UI!

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

    $ python irblaster.py
    
Navigate to 0.0.0.0:5000 in your browser and you should see 'Hello there - Flask is working!'. Stop the server by running CTRL+C. 

Now we're going to add a new endpoint that will let us control the IR LED. If you look we've added a new route '/api/<remotecontrol>' where replacing '<remotecontrol>' with 'poweron' will send the system command "irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER". You can add a bunch of if-else or use switch-case statements to add any other irsend commands that you configured from STEP 1 of this tutorial. 

```python
from flask import Flask
import os

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

    $ python irblaster.py

Next test out your new API endpoint using the browser again. We'll switch the API to a POST request later on with a body (we'll need to for it to work with dialogflow / google assistant). Entering 0.0.0.0:5000/api/v1/poweron into a browser this time should actually envoke the POWER_ON command and turn on the tv! Switch 'poweron' to any other mapping you did to see your API now configured to work with any of your commands!

## Building the Remote Control GUI webpage

Great - now that we have the APIs working to control the IR LED we'll create a simple webpage that can be used to trigger the various remote control commands too!

Let's create a templates director with an index.html file inside:

    $ mkdir templates
    $ nano index.html

Add the following to the index.html. Add buttons for each of the different Remote Commands that you created for your Flask API and be sure to make each buttons' 'id' the same as the API endpoint (example 'poweron'):

```html
<html>
	<head>
		<title>MyRemote</title>
		<link rel="stylesheet" href='/static/style.css' />
	</head>
	<body>
		<h1>MY REMOTE!</h1>
		<div>
			<button id='poweron'>Power On</button>
			<button id='mute'>Mute</button>
		</div>
		<div>
			<button id='volumeup'>Volume Up</button>
			<button id='volumedown'>Volume Down</button>
		</div>
	</body>
</html>
```
Add some style to it by creating a style.css file in a 'static' directory by performing the following:

    $ cd ..
    $ mkdir static
    $ cd static
    $ nano style.css
    
Copy the following into the style sheet - or edit it to make it even better!

```python
body {
    background: white;
    color: grey;
    text-align: center;
}

button {
  color: white;
  background-color: #008CBA;  
  font-size: 12px;
  padding: 12px 28px;
  border-radius: 4px;
  width: 49%;
}
```

Navigate back to the root project folder and change the irblaster.py file to import render_template in order to use our newly created index.html page. This will allow the page to render when hitting the Flask server's root endpoint:

```python
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/api/v1/<remotecontrol>')
def controlremote(remotecontrol):
    if remotecontrol == "poweron":
    	os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
	return 'performing the following remote control action: ' + remotecontrol

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
```

Start the server again and if you navigate to the 0.0.0.0:5000 now in your browser you should see your remote! Next let's hook up the buttons to the API so that it can send the appropriate IR led command! Open up the index.html file again and make the following edits - adding a function to each button click and defining the appropriate api in the <script>:

```html
<html>
	<head>
		<title>MyRemote</title>
		<link rel="stylesheet" href='/static/style.css' />
	</head>
	<body>
		<h1>MY REMOTE!</h1>
		<div>
			<button id='poweron', onclick='remoteCommand(this.id)'>Power On</button>
			<button id='mute', onclick='remoteCommand(this.id)'>Mute</button>
		</div>
		<div>
			<button id='volumeup', onclick='remoteCommand(this.id)'>Volume Up</button>
			<button id='volumedown', onclick='remoteCommand(this.id)'>Volume Down</button>
		</div>
	</body>
	<script>
		function remoteCommand(value){
		  const url = '0.0.0.0:5000/api/v1/' + value		  
		  fetch(url, {
		  	method:"GET", 
		  	protocol:'http:',
		    	headers: {
            			"Content-Type": "text/plain"
        		}
		     })
          	  }
	</script>
</html>
```

Save the updated index.html document and then restart the irblaster.py server. Navigate to 0.0.0.0:5000 and you should see you remote. You should be able to click on any of the buttons and it should perform the corresponding command! Congratulations, you now have a working remote using the GUI webpage! 

We are going to make a final few modifications to the tvblaster.py APIs now so that they are ready to act as fulfillment for a dialogflow intent (this will make more sense when we get to that section - but trust me anyways!). 

```python
from flask import Flask, render_template, request, jsonify, make_response
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/api/v1/<remotecontrol>')
def controlremote(remotecontrol):
    if remotecontrol == "poweron":
    	os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
	return 'performing the following remote control action: ' + remotecontrol

@app.route('/api/v2/remote', methods = ['POST'])
def remote():
  data = request.get_json(silent = True, force = True);
	if request.method == 'POST':
		action = data.get("queryResult").get("parameters").get("control");
		if action == "power on": 
			os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
			reply = {
 			"fulfillmentText": "Sure " + action,
			}
			return make_response(jsonify(reply));
		elif action == 'power off':
  			os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
			reply = {
  			"fulfillmentText": "Sure " + action,
			}
			return make_response(jsonify(reply));
		elif action == 'volume up': 
			os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_VOLUMEUP")
			reply = {
  			"fulfillmentText": "Sure " + action,
			}
			return make_response(jsonify(reply));
		elif action == 'volume down': 
			os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_VOLUMEDOWN")
			reply = {
 			 "fulfillmentText": "Sure " + action,
			}
			return make_response(jsonify(reply));
		else :
  			errorreply = {
  		    "fulfillmentText": "it didn't work! try again.",
  			}
			return make_response(jsonify(errorreply));

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
```

As you can see we've added a few different actions along with their corresponding action. Modify and add any other remote commands that you've created as another elif action along with the corresponding irsend command. The above example has four - power on, power off, volume up and volume down. Save your changes and restart the irblaster flask server once more. 

Before we start on the final part - it will be important to expose your server to the outside world using port forwarding or a service like ngrok or serveo. I won't go over the details of that in this tutorial - but feel free to do a quick google search with 100s of easy solutions. It will be important that whatever service you use allows you to expose the server over https  - not http as a secure connection is needed for Dialogflow. 
