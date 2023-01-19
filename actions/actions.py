# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


bank_db = {
    'binamra': '1234567890',
    'ram': '0123456789'
}


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_bank"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities'][0]['value']
        print(entities)

        name = tracker.get_slot("name")

        # e_name = tracker.latest_message['entity']
        # print(e_name)

        match = bank_db.get(name, None)
        number = tracker.get_slot("number")
        

        if number == match:
            dispatcher.utter_message(text=f"Hello {name} your account {number} balance is rs. 1000")
        else:
            print(match)
            dispatcher.utter_message(text=f"Hello {name} your account {number} not found")


        # if not match:
        #     msg = f"SORRY. {name} Wrong Details"
        #     dispatcher.utter_message(text=msg)
        #     return []


        return []
