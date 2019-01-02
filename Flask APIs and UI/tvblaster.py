from flask import Flask, render_template, request, jsonify, make_response
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/api/v1/<remotecontrol>')
def controlremote(remotecontrol):
    if remotecontrol == "poweron"
    	os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
	return 'performing the following remote control action: ' + remotecontrol

@app.route('/api/remote', methods=['POST'])
def remote():
        data = request.get_json(silent=True, force=True);
        if request.method == 'POST':
                 # os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
                 action = data.get("queryResult").get("parameters").get("control");
                 print action;
                 if action == "power on":
                         # os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
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
                 elif action == 'change input':
                         # os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
                         reply = {
                                "fulfillmentText": "Sure " + action,
                         }
                         return make_response(jsonify(reply));
                 elif action == 'weather.outfit':
                         # os.system("irsend SEND_ONCE /home/pi/lirc.conf KEY_POWER")
                         reply = {
                                "fulfillmentText": "Sure " + action,
                         }
                         return make_response(jsonify(reply));
                 else:
                         errorreply = {
                                "fulfillmentText": "it didn't work! try again.",
                         }
                         # print data
                         return make_response(jsonify(errorreply));

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')