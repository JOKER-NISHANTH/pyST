'''
Normal Lock Mechanishm
import threading as th
Lock = th.Lock --> Lock.acquire()  --> Lock.release() --> Lock.acquire()  --> Lock.release()

RLock Mechanishm
Lock = th.RLock --> Lock.acquire()  --> Lock.acquire()  --> Lock.acquire()
'''

import threading as th

class Thread:
    def __init__(self):
        self.a = 5
        self.b = 10
        self.Lock = th.Lock()

    def first(self):
        print('Entering into first')
        with self.RLock:
            self.a += 5
    def second(self):
        print('Entering into second')
        with self.Lock:
            self.b -= 5

    def main(self):
        print("Entering into main")
        with self.Lock:
            self.first()
            self.second()
            print("A",self.a,"B",self.b)

obj = Thread()
obj.main()