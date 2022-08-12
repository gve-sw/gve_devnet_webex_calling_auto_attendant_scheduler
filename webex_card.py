#!/usr/bin/env python3
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

# This function returns the JSON format of the location adaptive card
def getLocationCard(location_choices):
    location_card = {
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2",
        "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "Webex Calling Auto Attendant Scheduler",
                                "weight": "Bolder",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "Container",
                "items": [
                    {
                        "type": "TextBlock",
                        "text": "Welcome to the Auto Attendant Scheduler Bot! Use the options provided by the cards to schedule a new time for the Auto Attendant.",
                        "wrap": True
                    }
                ]
            },
            {
                "type": "Container",
                "items": [
                    {
                        "type": "TextBlock",
                        "text": "Choose the location where the Auto Attendant is:",
                        "wrap": False
                    },
                    {
                        "type": "Input.ChoiceSet",
                        "id": "location",
                        "isMultiSelect": False,
                        "value": "1",
                        "choices": location_choices
                    }
                ]
            },
            {
                "type": "ActionSet",
                "actions": [
                    {
                        "type": "Action.Submit",
                        "id": "submit",
                        "title": "Submit",
                        "data": {
                            "callback_keyword": "schedule"
                        }
                    }
                ]
            }
        ]
    }

    # Notice the callback_keyword is schedule, so it triggers the actions for the bot to send the schedule card

    return location_card


# This function returns the JSON format of the location adaptive card
def getScheduleCard(attendant_choices, schedule_choices):
    schedule_card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.2",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Webex Calling Auto Attendant Scheduler",
                                    "weight": "Bolder",
                                    "wrap": True,
                                    "color": "Light",
                                    "size": "Large",
                                    "spacing": "Small"
                                }
                            ],
                            "width": "stretch"
                        }
                    ]
                },
                {
                    "type": "Container",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Welcome to the Auto Attendant Scheduler Bot! Use the options provided by the cards to schedule a new time for the Auto Attendant.",
                            "wrap": True
                        }
                    ]
                },
                {
                    "type": "Container",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Choose the Auto Attendant that needs a schedule change:",
                            "wrap": False
                        },
                        {
                            "type": "Input.ChoiceSet",
                            "id": "autoAttendant",
                            "isMultiSelect": False,
                            "value": "1",
                            "choices": attendant_choices
                        },
                        {
                            "type": "TextBlock",
                            "text": "Choose the schedule that the Auto Attendant should use:",
                            "wrap": False
                        },
                        {
                            "type": "Input.ChoiceSet",
                            "id": "schedule",
                            "isMultiSelect": False,
                            "value": "1",
                            "choices": schedule_choices
                        }
                    ]
                },
                {
                    "type": "ActionSet",
                    "actions": [
                        {
                            "type": "Action.Submit",
                            "id": "submit",
                            "title": "Submit",
                            "data": {
                                "callback_keyword": "makeChanges"
                            }
                        }
                    ]
                }
            ]
        }
    }

    # Notice the callback_keyword is "makechanges." This will trigger the bot to perform the actions to change the attendant schedule
    return schedule_card
