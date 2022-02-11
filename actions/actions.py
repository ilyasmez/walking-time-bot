# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os
import requests


class ActionTellWalkDuration(Action):

    def name(self) -> Text:
        return "action_tell_walk_duration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        origin = tracker.get_slot('origin_address')
        destination = tracker.get_slot('destination_address')

        r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', {
            'origins': origin,
            'destinations': destination,
            'mode': 'walking',
            'key': os.environ.get('GOOGLE_API_KEY'),
        })
        duration = r.json()['rows'][0]['elements'][0]['duration']['text']

        dispatcher.utter_message(text='It should take you around ' + duration + ' to go from ' + origin + ' to ' + destination + '. You better start walking! :D')

        return []
