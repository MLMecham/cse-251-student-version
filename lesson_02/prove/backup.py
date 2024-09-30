"""
Course: CSE 251 
Lesson: L02 Prove
File:   prove.py
Author: Mitchell Mecham

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py" and leave it running.
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the description of the assignment.
  Note that the names are sorted.
- You are required to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a separate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}

Outline of API calls to server

1) Use TOP_API_URL to get the dictionary above
2) Add "6" to the end of the films endpoint to get film 6 details
3) Use as many threads possible to get the names of film 6 data (people, starships, ...)

"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0



# TO?DO Add your threaded class definition here
class makeThread(threading.Thread):
    
    def __init__(self,url, lock=None):
        super().__init__()
        self.url = url
        self.lock = lock
        self.data = {}
        self.status_code = 0
    
    def run(self):
        global call_count

        response = requests.get(self.url)
        self.status_code = response.status_code
        if self.status_code == 200:
            # print("yay")
            self.data = response.json()
        else:
            print("ERROR: ", self.status_code)
        
        # with self.lock:
        call_count += 1

# T?ODO Add any functions you need here
def get_urls(url):
        req = makeThread(url)
        req.start()
        req.join()

        # print("TOP LEVEL DATA\n")
        # print(req.data)
        return req.data

def get_film6(url):
    # req = makeThread(f'{TOP_API_URL}/films/6')
    req = makeThread(f"{url['films']}6")
    req.start()
    req.join()

    # print("FILM 6 DATA\n")
    # print(req.data)
    return req.data

# def get_title():
#     req = makeThread(f'{TOP_API_URL}/films/6/title')
#     req.start()
#     req.join()

#     print("TITLE\n")
#     print(req.data)
        
def make_threads(data, key):
     threads = []
     for url in data[key]:
          thread = makeThread(url)
          threads.append(thread)

    #  print(len(threads))
     return threads


    #  print("CHARACTERS")
    # print(film_6['characters'])
    # character_threads = []
    # for character in film_6['characters']:
    #     thread = makeThread(character)
    #     character_threads.append(thread)


def start_threads(threads):
     for thread in threads:
          thread.start()


def end_threads(threads):
     for thread in threads:
          thread.join()

def get_details(threads):
     details = []
     for thread in threads:
      details.append(thread.data['name'])
     details.sort()
     return details
        

    
# def display_results():
#         pass

def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    lock = threading.Lock()

    # T.ODO Retrieve Top API urls
    url_data = get_urls(TOP_API_URL)
    film_6 = get_film6(url_data)

    

    # TODO Retrieve Details on film 6

    # make threads
    character_threads = make_threads(film_6, 'characters')
    planet_threads = make_threads(film_6, 'planets')
    starship_threads = make_threads(film_6, 'starships')
    vehicule_threads = make_threads(film_6, 'vehicles')
    species_threads = make_threads(film_6, 'species')


    


    
    # start threads
    start_threads(character_threads)
    start_threads(planet_threads)
    start_threads(starship_threads)
    start_threads(vehicule_threads)
    start_threads(species_threads)

    # end threads
    end_threads(character_threads)
    end_threads(planet_threads)
    end_threads(starship_threads)
    end_threads(vehicule_threads)
    end_threads(species_threads)

    # put the details into a list. Sort the list
    characters = get_details(character_threads)
    planets = get_details(planet_threads)
    starships = get_details(starship_threads)
    vehicules = get_details(vehicule_threads)
    species = get_details(species_threads)
    
         
    

    # TODO Display results
    print("-" * 30)
    print(f'Title: {film_6["title"]}')
    print(f'Director: {film_6["director"]}')
    print(f'Producer: {film_6["producer"]}')
    print(f'Release Date: {film_6["release_date"]}')
    print('')

    print(f'Characters: {len(characters)}')
    print(*characters, sep=', ')
    print('')

    print(f'Planets: {len(planets)}')
    print(*planets, sep=', ')
    print('')
    
    print(f'Starships: {len(starships)}')
    print(*starships, sep=', ')
    print('')

    print(f'Vehicules: {len(vehicules)}')
    print(*vehicules, sep=', ')
    print('')

    print(f'Species: {len(species)}')
    print(*species, sep=', ')
    print('')


    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')
    

if __name__ == "__main__":
    main()


# unpacking notes, print(*values, sep=', '). Works like a forloop.