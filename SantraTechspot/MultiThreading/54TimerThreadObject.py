
import threading
import time

def demo():
    print("Welcome")
print(" External Time Module ")
t = threading.Thread(target=demo)
time.sleep(3)
t.start()

print(" Timer method in threading ")
t1 = threading.Timer(3.0, demo)  # 3.0 = 3 sec
t1.start()

print("Canceling the thread ")
time.sleep(2) # Becoz Timer set 3sec but here set 2sec layaa cancel pandroim
t1.cancel()