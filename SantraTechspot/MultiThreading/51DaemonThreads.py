# Infinity running

import threading
import time

def worker_a():
    print("Thread 1 is started")
    time.sleep(10)
    print("Thread 1 finished")
def worker_b():
    print("Thread 2 is started")
    print("Thread 2 finished")

print("\n\t Daemon Thread ")
t1 = threading.Thread(target=worker_a, daemon=True)
t1.start()  # daemon = True , Here t1 is running infinity when the complete program stop

print("\n\t Normal Thread ")
t2 = threading.Thread(target=worker_b)
t2.start()

# Here join() give on chance for stop the program
# t1.join()
# t2.join()