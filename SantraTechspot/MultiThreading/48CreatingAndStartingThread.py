import threading
import time

def display(x,s,name):
    #for i in range(5):  # Here 5 is Hotcode
    for i in range(x):
        time.sleep(s)
        print(name," : Thread Started....")

# Create single Thread
t = threading.Thread(target=display , args=(5,1,'Thread 1'))
t.start()

# Create Multi-Thread

t1 = threading.Thread(target=display, args=(5, 1, 'Thread 2'))
t1.start()