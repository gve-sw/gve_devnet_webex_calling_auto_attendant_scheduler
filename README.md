# Auto Attendant Scheduler Bot
This prototype defines a Webex bot that a user can use to schedule their site's Webex Calling Auto Attendant. The bot uses the Webex APIs and the webex_bot Python library to accept commands from the user through Webex messages and then execute those commands.

## Contacts
* Danielle Stacy

## Solution Components
* Python 3.9
* Webex Calling
* Webex Teams

## Prerequisites
- **Webex API Personal Token**:
1. To use the Webex REST API, you need a Webex account backed by Cisco Webex Common Identity (CI). If you already have a Webex account, you're all set. Otherwise, go ahead and [sign up for a Webex account](https://cart.webex.com/sign-up).
2. When making request to the Webex REST API, the request must contain a header that includes the access token. A personal access token can be obtained [here](https://developer.webex.com/docs/getting-started).

> Note: This token has a short lifetime - only 12 hours after logging into this site - so it shouldn't be used outside of app development.

- **Webex Bot**:  
This prototype requires a bot. To create a Webex bot, you need a token from Webex for Developers.
1. Log in to `developer.webex.com`
2. Click on your avatar and select `My Webex Apps`
3. Click `Create a New App`
4. Click `Create a Bot` to start the wizard
5. Following the instructions of the wizard, provide your bot's name, username, and icon
6. Once the form is filled out, click `Add Bot` and you will be given an access token
7. Copy the access token and store it safely. Please note that the API key will be shown only once for security purposes. In case you lose the key, then you have to revoke the key and generate a new key

> For more information about Webex Bots, please see the [documentation](https://developer.webex.com/docs/bots)

> [This blog](https://developer.webex.com/blog/from-zero-to-webex-teams-chatbot-in-15-minutes) gives more step by step instructions.


## Installation/Configuration
1. Clone this repository with `git clone https://github.com/gve-sw/gve_devnet_webex_calling_auto_attendant_scheduler` 
2. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).
3. Install the requirements with `pip3 install -r requirements.txt`
4. Add the tokens that you found in the Prerequisites section as environmental variables to the .env file.
```python
WEBEX_KEY='personal webex token goes here'
BOT_TOKEN='bot token goes here'
```
5. Launch the bot with this command:
```
$ python3 bot.py
```

## Usage
To start scheduling the Auto Attendant with the bot, start a conversation in Webex to the bot that you created in the Prerequisites section. 

Then send the string `attendant` as a message to the bot. Once the bot processes this message, it will reply with a Webex card that prompts you to select the location of the Auto Attendant that you would like to schedule from a dropdown list.

Once you have selected the location and submitted the response, the bot will delete that message and process the location of the Auto Attendant. Then it will reply with another Webex card that prompts you to select the name of the Auto Attendant and the schedule you would like to assign to it from separate dropdown lists.

After you submit your selections, the bot will again delete the message and then reassign the Auto Attendant schedule to your specifications. If the assignment is successful, the bot will send a message that lets you know it was successful. If there was an issue, the bot will send a message to let you know what kind of error occurred while trying to reassign the Auto Attendant schedule.

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

After sending the message `attendant`  
![/IMAGES/first-response.png](/IMAGES/first-response.png)

After submitting the location  
![/IMAGES/second-response.png](/IMAGES/second-response.png)

The bot successfully changed the Auto Attendant schedule  
![/IMAGES/successful-response.png](/IMAGES/successful-response.png)

Changes in Webex Control Hub  
![/IMAGES/control-hub.png](/IMAGES/control-hub.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
