'''opr = (lambda a,b,c: a*b/c )
print(opr(2,5,5))

a= [1,2,3,4]
b=a
del a
print(b)

print("this is {} {}".format("Nikhil","Vichare"), ", hello to world!!")'''

from time import sleep

def timer(seconds):
    while seconds:
        min, sec = divmod(seconds,60)
        count='{:0d}:{:0.1d}'.format(min,sec)
        print(count,end="\r")
        sleep(1)
        seconds -= 1
timer(10)