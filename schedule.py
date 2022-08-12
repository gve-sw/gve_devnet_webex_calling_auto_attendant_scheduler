""" Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
import os, requests, json
from dotenv import load_dotenv

from webex_bot.models.command import Command
from webex_bot.models.response import Response
from adaptivecardbuilder import *
from webex_card import *


# Get environmental variables
load_dotenv()
WEBEX_KEY = os.getenv("WEBEX_KEY")
BASE_URL = "https://webexapis.com/v1"

headers = {
    "Authorization": "Bearer " + WEBEX_KEY,
    "Content-Type": "application/json; charset=utf-8"
}

# Make API call to get the possible locations that the Auto Attendant might be at
location_endpoint = "/locations"
location_response = requests.get(BASE_URL+location_endpoint, headers=headers)
location_response_json = json.loads(location_response.text)["items"]
locations = []
location_to_id = {}
# Format the locations into a dictionary that the Adaptive card will understand
for location in location_response_json:
    location_format = {
        "title": location["name"],
        "value": location["name"]
    }
    locations.append(location_format)

    location_to_id[location["name"]] = location["id"]

# Get the JSON representation of the Adaptive card
location_card = getLocationCard(locations)

attendant_to_location = {}
attendant_id_to_name = {}


# The locationAutoAttendant class defines the bot's behavior once the command `attendant` is issued
class locationAutoAttendant(Command):
    def __init__(self):
        super().__init__(
            command_keyword="attendant",
            help_message="Create new schedule for Webex Calling Auto Attendant",
            card=location_card,
            delete_previous_message=True
        )

    # This function shouldn't execute
    def execute(self, message, attachment_actions, activity):

        # Build card response
        response = Response()
        # Fallback text
        response.text = "Something has gone wrong"

        return response

# The scheduleAutoAttendant class defines the bot's behavior after the user input for the location card has been submitted
class scheduleAutoAttendant(Command):
    def __init__(self):
        super().__init__(
            command_keyword="schedule",
            help_message="Create new schedule for Webex Calling Auto Attendant, enter the keyword attendant to start",
            card=location_card,
            delete_previous_message=True
        )

    def execute(self, message, attachment_actions, activity):
        location = attachment_actions.inputs["location"] # the location selected
        location_id = location_to_id[location] # the location id associated with that location

        # Make an API call to retrieve the available attendants at the specified location
        attendant_endpoint = "/telephony/config/autoAttendants?locationId={}".format(location_id)
        attendants_response = requests.get(BASE_URL+attendant_endpoint, headers=headers)
        attendants_response_json = json.loads(attendants_response.text)["autoAttendants"]
        attendants = []
        # Format the attendants into a dictionary that the Adaptive card will understand
        for attendant in attendants_response_json:
            attendant_format = {
                "title": attendant["name"],
                "value": attendant["id"]
            }
            attendants.append(attendant_format)

            attendant_to_location[attendant["id"]] = attendant["locationId"]
            attendant_id_to_name[attendant["id"]] = attendant["name"]

        # Make an API call to retrieve the available schedules for these attendants
        schedule_endpoint = "/telephony/config/locations/{}/schedules".format(location_id)
        schedule_response = requests.get(BASE_URL+schedule_endpoint, headers=headers)
        schedule_response_json = json.loads(schedule_response.text)["schedules"]
        schedules = []
        # Format the schedules into a dictionary that the Adaptive card will understand
        for schedule in schedule_response_json:
            schedule_format = {
                "title": schedule["name"],
                "value": schedule["name"]
            }
            schedules.append(schedule_format)


        # Get the JSON representation of the Adaptive card this step will send
        attendant_card = getScheduleCard(attendants, schedules)
        card_data=attendant_card["content"]
        card_payload = {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": card_data
        }

        # Build card response
        response = Response()
        # Fallback text
        response.text = "Attendant Schedule Card"
        # Attach the Adaptive card
        response.attachments = card_payload

        return response


# This class defines the behavior of the bot after the attendant and schedule choices have been submitted
class makeChanges(Command):
    def __init__(self):
        super().__init__(
            command_keyword="makechanges",
            help_message="Create new schedule for Webex Calling Auto Attendant",
            card=None,
            delete_previous_message=True
        )

    def execute(self, message, attachment_actions, activity):
        attendant = attachment_actions.inputs["autoAttendant"] # the attendant selected
        schedule = attachment_actions.inputs["schedule"] # the schedule selected
        location = attendant_to_location[attendant] # the location associated with that attendant

        # Make the API call to change the Auto Attendant schedule to what the user specified
        change_schedule_endpoint = "/telephony/config/locations/{}/autoAttendants/{}".format(location, attendant)
        change_schedule_body = {
            "businessSchedule": schedule
        }
        change_response = requests.put(BASE_URL+change_schedule_endpoint, headers=headers, data=json.dumps(change_schedule_body))

        # Build card response
        response = Response()
        if change_response.status_code == 204:
            attendant_name = attendant_id_to_name[attendant]
            response.text = "You have successfully changed the schedule of attendant {} to {}".format(attendant_name, schedule)
        else:
            response.text = "There was a {} error when trying to change the schedule.".format(change_response.status_code)

        return response
