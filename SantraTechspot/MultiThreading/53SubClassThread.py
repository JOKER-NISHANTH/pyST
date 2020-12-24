import threading

# threading.Thread --> Thread ==> Super class
# ThreadDemo --> SubClass or Derived class
# Like multi-level inheritance

print("Without- Arguments")
class ThreadDemo(threading.Thread):
    # Here run is main
    def run(self):
        print("Hello World")
        self.new()
        return None
    def new(self):
        print("Welcome")
for i in range(5):
    t = ThreadDemo()
    t.start()


print("With- Arguments")

class threadDemo(threading.Thread):
    # Here run is main
    def __init__(self, args=(), kwargs=None):
        threading.Thread.__init__(self)
        self.args = args
        self.kwargs=kwargs
    def run(self):
        print("Thread",self.args,"argument is ",self.kwargs)
        return None

for i in range(5):
    t = threadDemo(args=(i,), kwargs="Hello")
    t.start()
