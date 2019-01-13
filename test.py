
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        ranger=input("enter the range")
        for i in range(int(ranger)):
            print("Hello")
            sleep(1)
            
class Hi(Thread):
    def run(self):
        for i in range(20):
            print("Hi")
            sleep(1)
t1=Hello()
t2=Hi()

t1.start()
sleep(2)
t2.start()


'''
datalist=[]

for i in range(5):
    datalist.append({"range":i,"name":"Nikhil","surname":"Vichare","Address":"abc","works at":"ISS"})

for x in range(len(datalist)):
    keyValuePair=datalist[x]
    print(keyValuePair["range"])'''