'''
Lock        --> lock.acquire()
Release     --> lock.release() 
'''

import threading
import time

# Lock_Object_name
lock = threading.Lock()

def runThread(name):
    time.sleep(3)
    #lock.acquire()
    display(name)
    #lock.release()

def display(name):
    for i in range(1,6):
        time.sleep(2)
        print(name,"Excecuted : Value of i is ", i)

t1=threading.Thread(target=runThread,args=("Thread : 1",))
t2 = threading.Thread(target=runThread, args=("Thread : 2",))
t3 = threading.Thread(target=runThread, args=("Thread : 3",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
