## Part 3 - Dialogflow and Actions. Control the remote with your voice!

This section will teach you how to create a dialogflow event and a google action to respond to a users voice to create the API request to your Flask server. 

First you will create a new 'Agent'. Call it whatever you like, mine will be called 'IRVoiceRemote' and create a new Google Project. 
![alt text](https://ibb.co/mzq3sCq)

Next you will need to create a new 'Intent'. Name the intent something simple, we'll call ours 'voiceremote'. 
![alt text](https://ibb.co/mzq3sCq)

Next we'll create a new 'Entity'. Again call it something simple, we'll call ours 'remote_options'. Fill the entities with all of your recorded remote commands - you can see the ones I added below. If you want to use synonyms ('turn off' instead of 'power off') feel free to add in the synonyms. Save it and go back to your voiceremote Intent. 

In the 'Actions and Parameters' section, add 'remote_request' to the 'entity' column and make sure to click the box that says the entity is mandatory. 

Add some training phrases to add some variations on how you would invoke some of your entities. These can be various phrases that you would use that might contain the entities you listed in the last step. 

In the 'Responses' section, toggle on the 'Set this intent as the end of the conversation'. This ensures that when you invoke the intent it does not continue to ask for further requests or information. 

In 'Fulfillment' section within 'Intents', toggle on the 'Enable webhook call for this intent'. 

You will then need to go to the 'Fulfillment' page and enable the webhook section. You will then enter the https url of the endpoint that you created using portforwarding or one of the services (ngrok or serveo). Be sure to append '/api/v2/remote' to the end of the request to hit the API that you created. 
