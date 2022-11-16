#Multi Threading
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")

p1 = Hello()
p2 = Hi()

p1.start()
sleep(0.1)
p2.start()

p1.join()
p2.join()
print("Bye......................................")