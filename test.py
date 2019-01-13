#test=[1,2,3,4]

datalist=[]

for i in range(5):
    datalist.append({"range":i,"name":"Nikhil","surname":"Vichare","Address":"abc","works at":"ISS"})

for x in range(len(datalist)):
    keyValuePair=datalist[x]
    print(keyValuePair["range"])