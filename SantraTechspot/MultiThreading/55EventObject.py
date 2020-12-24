'''
# Event Object  --> Handling flag --> True , Flase

1. set()
2. clear()
3. wait()
4. is_set()

'''

import threading
import time

def isSet():
    time.sleep(2)
    event.set()
    print("Event is Set")
    time.sleep(10)
    event.clear()
    print("Event is clear ")

def eventOperation():
    event.wait()
    while event.is_set():
        time.sleep(1)
        print("Thread is waiting for singal....")

    print("Thread is received singal")


# Create event object
event = threading.Event()
t1 = threading.Thread(target=isSet)
t2 = threading.Thread(target=eventOperation)
t1.start()
t2.start()
t1.join()
t2.join()
