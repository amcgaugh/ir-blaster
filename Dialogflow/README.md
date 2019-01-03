# Part 3 - Dialogflow and Actions. Control the remote with your voice!

This section will teach you how to create a dialogflow event and a google action to respond to a users voice to create the API request to your Flask server. 

1. First you will create a new 'Agent'. Call it whatever you like, mine will be called 'IRVoiceRemote' and create a new Google Project. 

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/Step%201.png)

2. Next you will need to create a new 'Intent'. Name the intent something simple, we'll call ours 'voiceremote'.

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/DF%20Intent.png)

3. Next we'll create a new 'Entity'. Again call it something simple, we'll call ours 'remote_options'. Fill the entities with all of your recorded remote commands - you can see the ones I added below. If you want to use synonyms ('turn off' instead of 'power off') feel free to add in the synonyms. Save it and go back to your voiceremote Intent. 

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/Step%202.png)

4. Back in the voiceremote Intent go to the 'Actions and Parameters' section, add 'remote_options' to the 'entity' column and click the box that says the entity is mandatory. 

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/Step%203.png)

5. Add some training phrases to add some variations on how you would invoke some of your entities. These can be various phrases that you would use that might contain the entities you listed in the last step. 

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/Step%204.png)

6. In the 'Responses' section, add 'Google Assistant' and then toggle on the 'Set this intent as the end of the conversation'. This ensures that when you invoke the intent it does not continue to ask for further requests or information. 

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/Step%205.png)

7. In 'Fulfillment' section within 'Intents', toggle on the 'Enable webhook call for this intent'. 

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/Step%206.png)

8. You will then need to go to the 'Fulfillment' page and enable the webhook section. You will then enter the https url of the endpoint that you created using portforwarding or one of the services (ngrok or serveo). Be sure to append '/api/v2/remote' to the end of the request to hit the API that you created. 

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/Step%207.png)

9. Next go to 'Integrations' and select the Google Assistant. 

10. A window will popup - add 'voiceremote' to the explicit intent. For the implic intent you can add the 'Default Welcome Intent' and then click 'Manage Assistant App'

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/Popupwindow.png)

11. Click on the 'Decide how you action will be invoked'. For Display Name, call you action whatever you want to be asking the Google Assistant to request your skill, I have it as 'Andrew's Remote'. This will mean you will be invoking the skill by saying, "Hey Google, Ask Andrew's Remote to Power On". 

![alt text](https://raw.githubusercontent.com/amcgaugh/ir-blaster/master/docs/HowInvoked.png)

12. From there you should be able to go to the 'Simulator' and give it a go. Or better yet - as long as you created this Action with the gmail account associated with your Google Assistants, you can now try it out live. Try saying "Hey Google, Ask Andrew's Remote to Power On" (or whatever you called your remote / whatever remote command you want to send). It should now be htiting your Flask API and invoking the Remote Command. Congrats you did it!
