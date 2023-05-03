"""
Course: CSE 251
Lesson Week: 02 - Team Activity
File: team.py
Author: Brother Comeau

Purpose: Playing Card API calls
Website is: http://deckofcardsapi.com

Instructions:

- Review instructions in I-Learn.

"""

from datetime import datetime, timedelta
import threading
import requests
import json

# Include cse 251 common Python files
from cse251 import *

# TODO Create a class based on (threading.Thread) that will
# make the API call to request data from the website

class Request_thread(threading.Thread):
    # TODO - Add code to make an API call and return the results
    #response = requests.get('https://realpython.com/python-requests/')
    def __init__(self, url):
        super().__init__()

        self.url = url
        self.response = {}

    def run(self):
        theReturn = requests.get(self.url)
        if theReturn.status_code == 200:
            self.response = theReturn.json()
        else:
            print('RESPONSE = ', theReturn.status_code)



class Deck:

    def __init__(self, deck_id):
        self.id = deck_id
        self.reshuffle()
        self.remaining = 52


    def reshuffle(self):
        print('Reshuffle Deck')
        # TODO - add call to reshuffle
        reshuff = Request_thread(rf'https://deckofcardsapi.com/api/deck/{self.id}/shuffle/')
        reshuff.start()
        reshuff.join()



    def draw_card(self):
        # TODO add call to get a card
        indCard = Request_thread(rf'https://deckofcardsapi.com/api/deck/{self.id}/draw/?count=2')
        indCard.start()
        indCard.join()
        if indCard.response != {}:
            self.remaining = indCard.response['remaining']
            return indCard.response['cards'][0]['code']
        else:
            return ''

    def cards_remaining(self):
        return self.remaining


    def draw_endless(self):
        if self.remaining <= 0:
            self.reshuffle()
        return self.draw_card()


if __name__ == '__main__':

    # TODO - run the program team_get_deck_id.py and insert
    #        the deck ID here.  You only need to run the 
    #        team_get_deck_id.py program once. You can have
    #        multiple decks if you need them

    deck_id = 'p3e3muuqzbpi'

    # Testing Code >>>>>
    deck = Deck(deck_id)
    for i in range(55):
        card = deck.draw_endless()
        print(i, card, flush=True)
    print()
    # <<<<<<<<<<<<<<<<<<

