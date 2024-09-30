"""
Course: CSE 251 
Lesson: L02 Team Activity
File:   team.py
Author: Mitchell Mecham

Purpose: Make threaded API calls with the Playing Card API http://deckofcardsapi.com

Instructions:

- Review instructions in Canvas.
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
    def __init__(self, url):
        super().__init__()
        self.url = url
        # https://realpython.com/python-requests/

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Error in request")

class Deck:

    def __init__(self, deck_id):
        self.id = deck_id
        self.reshuffle()
        self.remaining = 52


    def reshuffle(self):
        print('Reshuffle Deck')
        # TODO - add call to reshuffle
        url = f'https://deckofcardsapi.com/api/deck/{self.id}/shuffle/?remaining=true'
        thread = Request_thread(url)
        data = thread.start()
        print(data)
        thread.join()


    def draw_card(self):
        # TODO add call to get a card
        url = f'https://deckofcardsapi.com/api/deck/{self.id}/draw/?count=2'
        thread = Request_thread(url)
        card = thread.start()
        print(f'card is {card}')
        
        

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

    deck_id = '51ols4zpwv8z'

    # Testing Code >>>>>
    deck = Deck(deck_id)
    for i in range(55):
        card = deck.draw_endless()
        print(f'card {i + 1}: {card}', flush=True)
    print()
    # <<<<<<<<<<<<<<<<<<

    deck.reshuffle()
    deck.draw_card()
