'''
threading.current_thread()
threading.enumerate()
threading.active_count()

'''

import threading
import time

def worker_a():
    print("Thread started...")
    print(threading.current_thread())
    time.sleep(5)

def worker_b():
    time.sleep(10)

t2 = threading.Thread(target=worker_b, daemon=True)
t2.start()

for i in range(5):
    t1 = threading.Thread(target=worker_a)
    t1.start()
    #time.sleep(1) # 1st thread missing because the file sleep for 1 sec total 5 sec , 1st thread time is exprie
    time.sleep(1)

print("Enumerate")
print(threading.enumerate())  # return Alive_Threads in list format

print("Total Thread Count")
print(threading.active_count())