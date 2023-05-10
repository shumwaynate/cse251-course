"""
Course: CSE 251
Lesson Week: 04
File: team.py
Author: Brother Comeau

Purpose: Team Activity

Instructions:

- See in I-Learn

Question: is the Python Queue thread safe?  (https://en.wikipedia.org/wiki/Thread_safety)

"""

import threading
import queue
import requests
import json

# Include cse 251 common Python files
from cse251 import *

RETRIEVE_THREADS = 4        # Number of retrieve_threads
NO_MORE_VALUES = 'No more'  # Special value to indicate no more items in the queue

def retrieve_thread(data_queue, number_in_queue_sem, log):  # TODO add arguments
    """ Process values from the data_queue """

    while True:
        # TODO check to see if anything is in the queue
        number_in_queue_sem.aquire()
        value = data_queue.get()
        if value == NO_MORE_VALUES:
            return
        
        response = requests.get(value)

        if response.status_code == 200:
            data = response.json()
            log.write(data['name'])
        else:
            log.write(f"Error with {value}")


        



def file_reader(data_queue, number_in_queue_sem, filename, log): # TODO add arguments
    """ This thread reading the data file and places the values in the data_queue """

    # TODO Open the data file "urls.txt" and place items into a queue
    

    with open(filename) as f: 
        for line in f:
            value = line.strip()

            data_queue.put(value)
            number_in_queue_sem.release()
    log.write('finished reading file')

    for _ in range(RETRIEVE_THREADS):
        data_queue.put(NO_MORE_VALUES)
        number_in_queue_sem.release()




def main():
    """ Main function """

    log = Log(show_terminal=True)

    # TODO create queue
    data_queue = queue.Queue()
    # TODO create semaphore (if needed)
    sem = threading.Semaphore(0)


    # TODO create the threads. 1 filereader() and RETRIEVE_THREADS retrieve_thread()s
    # Pass any arguments to these thread need to do their job

    log.start_timer()

    # TODO Get them going - start the retrieve_threads first, then file_reader

    # TODO Wait for them to finish - The order doesn't matter

    log.stop_timer('Time to process all URLS')


if __name__ == '__main__':
    main()




