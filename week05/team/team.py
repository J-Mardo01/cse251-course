"""
Course: CSE 251
Lesson Week: 05
File: team.py
Author: Brother Comeau

Purpose: Team Activity

Instructions:

- See in I-Learn

"""

import threading
import queue
from cv2 import log
import requests
import json

# Include cse 251 common Python files
from cse251 import *

RETRIEVE_THREADS = 4        # Number of retrieve_threads
NO_MORE_VALUES = 'No more'  # Special value to indicate no more items in the queue

def retrieve_thread(q, log):  # TODO add arguments
    """ Process values from the data_queue """
    while True:
        if data == NO_MORE_VALUES:
            break
        # TODO check to see if anything is in the queue
        data = q.get()
        response = requests.get(data)
        if response.status_code == 200:
            data = response.json()

        log.write(data["name"])
        # TODO process the value retrieved from the queue

        # TODO make Internet call to get characters name and log it
        pass



def file_reader(q, log): # TODO add arguments
    """ This thread reading the data file and places the values in the data_queue """

    # TODO Open the data file "urls.txt" and place items into a queue
    urls = open("urls.txt")
    for url in urls:
        queue.put(url.strip())
    for _ in range(RETRIEVE_THREADS):
        q.put(NO_MORE_VALUES)

    log.write('finished reading file')

    # TODO signal the retrieve threads one more time that there are "no more values"



def main():
    """ Main function """

    log = Log(show_terminal=True)

    q = queue.Queue()

    # TODO create queue
    # TODO create semaphore (if needed)

    # TODO create the threads. 1 filereader() and RETRIEVE_THREADS retrieve_thread()s
    # Pass any arguments to these thread need to do their job

    fileReader = threading.Thread(target = file_reader, args = (q, log))
    threads = [threading.Thread(target = retrieve_thread, args = (q, log)) for _ in range(RETRIEVE_THREADS)]

    log.start_timer()

    fileReader.start()

    for t in threads:
        t.start()
    
    for t in threads:
        t.join

    fileReader.join()

    # TODO Get them going - start the retrieve_threads first, then file_reader

    # TODO Wait for them to finish - The order doesn't matter

    log.stop_timer('Time to process all URLS')


if __name__ == '__main__':
    main()




