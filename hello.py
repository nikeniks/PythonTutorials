'''#msg=["hello world",18,4]
#print(msg[-3:-1])

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(10,20, 80)
plt.plot(x, np.sin(x))
plt.show()


msg = "hello world"
print(msg.capitalize())
msg_new=msg.split()
print(msg_new[1])

def farhenite_converter(celciusDegree):
    farenhite=((celciusDegree*9)/5)+32
    return farenhite
print(farhenite_converter(32))


def string_length(mystring):
    if type(mystring)==int:
       return "Sorry integers don't have length"
    elif type(mystring)==float:
        return "Sorry floats don't have length"
    else:
        return len(mystring)

print(string_length(10))

def readFile():
    filename=open("fruits.txt")
    fruits=filename.read()
    fruits=fruits.splitlines()
    for i in fruits:
        print(len(i))
readFile()


    def farhenite_converter(celciusDegree):
    farenhite=((celciusDegree*9)/5)+32
    return farenhite

    a=[10, -20, 100]
    for i in a:
    print(farhenite_converter(i))

'''

class A:
    def __init__(self):
        print("here in A")
    
    def methodOfA(self):
        listing=[1,2,3]
        print(listing)

    def getValue1(self,value1):
        self.value1=value1
    
    def setValue1(self):
        return self.value1


class tempConverter(A):
    num1 = 50

    def __init__(self):
        super().__init__()
        super().methodOfA()
        print("here in tempConverter")

    def farhenite_converter(self):
        farenhite=((tempConverter.num1*9)/5)+32
        return farenhite





#t1 = tempConverter()
#t2 = tempConverter()
#far1=t1.farhenite_converter()
#far2=t2.methodOfA()
#print(far1)

a1=A()
a1.getValue1("nikhil")
print(a1.setValue1())





