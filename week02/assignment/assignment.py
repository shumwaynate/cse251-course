"""
Course: CSE 251 
Lesson Week: 02
File: assignment.py 
Author: Brother Comeau

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
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

#call_count = 0


# TODO Add your threaded class definition here
class Request_thread(threading.Thread):
  # TODO - Add code to make an API call and return the results
  #response = requests.get('https://realpython.com/python-requests/')
  def __init__(self, url):

    super().__init__()
    

    self.url = url
    self.response = {}
    
    self.newdirpath = ""

  def run(self):
      theReturn = requests.get(self.url)
      if theReturn.status_code == 200:
        self.response = theReturn.json()
        # global call_count
        # call_count = call_count+1
        
      else:
        print('RESPONSE = ', theReturn.status_code)


# TODO Add any functions you need here
def printItems(FilmPieces):
   for i in FilmPieces:
      print(i)


def main():
  log = Log(show_terminal=True)
  log.start_timer('Starting to retrieve data from the server')

  global call_count
  call_count = 0

  # TODO Retrieve Top API urls
  topResponse = Request_thread(TOP_API_URL)
  topResponse.start()
  topResponse.join()
  # TODO Retireve Details on film 6
  # print("")
  # print("")
  # print(topResponse.response)
  filmListresponse = Request_thread(f'{topResponse.response["films"]}6')
  filmListresponse.start()
  filmListresponse.join()
 
  titlename = filmListresponse.response['title']
  directorname = filmListresponse.response['director']
  producername = filmListresponse.response['producer']
  releasedate = filmListresponse.response['release_date']
  characters3 = filmListresponse.response['characters']
  planets3 = filmListresponse.response['planets']
  starships3 = filmListresponse.response['starships']
  vehicles3 = filmListresponse.response['vehicles']
  species3 = filmListresponse.response['species']



  charactersT = []
  characters = []
  for i in characters3:
    characters2 = Request_thread(i)
    call_count = call_count +1
    charactersT.append(characters2)
  
  for i in charactersT:
    i.start()
    
  for i in charactersT:
    i.join()

  for i in charactersT:
    characters1 = i.response['name']
    characters.append(characters1)

  planetsT = []
  planets = []
  for i in planets3:
    characters2 = Request_thread(i)
    call_count = call_count +1
    planetsT.append(characters2)
  
  for i in planetsT:
    i.start()
    
  for i in planetsT:
    i.join()

  for i in planetsT:
    characters1 = i.response['name']
    planets.append(characters1)

  starshipsT = []
  starships = []
  for i in starships3:
    characters2 = Request_thread(i)
    call_count = call_count +1
    starshipsT.append(characters2)
  
  for i in starshipsT:
    i.start()
    
  for i in starshipsT:
    i.join()

  for i in starshipsT:
    characters1 = i.response['name']
    starships.append(characters1)

  vehiclesT = []
  vehicles = []
  for i in vehicles3:
    characters2 = Request_thread(i)
    call_count = call_count +1
    vehiclesT.append(characters2)
  
  for i in vehiclesT:
    i.start()
    
  for i in vehiclesT:
    i.join()

  for i in vehiclesT:
    characters1 = i.response['name']
    vehicles.append(characters1)

  speciesT = []
  species = []
  for i in species3:
    characters2 = Request_thread(i)
    call_count = call_count +1
    speciesT.append(characters2)
  
  for i in speciesT:
    i.start()
    
  for i in speciesT:
    i.join()

  for i in speciesT:
    characters1 = i.response['name']
    species.append(characters1)







  # TODO Display results
  log.write('-----------------------------------------')
  
  
  #s = ' '.join(names)
  log.write(f'Title : {titlename} ')
  log.write(f'Director : {directorname} ')
  log.write(f'Producer : {producername} ')
  log.write(f'Release Date  : {releasedate} ')
  log.write(f' ')
  characters4 = ', '.join(characters)
  log.write(f'Characters  : {characters4}')
  log.write(f' ')
  planets4 = ', '.join(planets)
  log.write(f'Planets  : {planets4} ')
  log.write(f' ')
  starships4 = ', '.join(starships)
  log.write(f'Starships  : {starships4} ')
  log.write(f' ')
  vehicles4 = ', '.join(vehicles)
  log.write(f'Vehicles  : {vehicles4} ')
  log.write(f' ')
  species4 = ', '.join(species)
  log.write(f'Species  : {species4} ')
  log.write(f' ')

  log.stop_timer('Total Time To complete')
  log.write(f'There were {call_count} calls to the server')
    

if __name__ == "__main__":
    main()
