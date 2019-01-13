
for i in range(1,6):
    for j in range(1,i+1):
     #   a.append("*")
    #for j in range(0,i):
        print("*", end ="")
    print()
    
    
for i in reversed(range(5)):
    for j in reversed(range(i)):
        print("*",end = "")
    print()

    
for i in range(5):
    for j in range(5):
        print("*",end = "")
    print()
       
a=["A","B","C","D"]
p=["P","Q","R"]
for i in range(4):
    for k in range(i+1):
        print(a[k], end="")
    for j in range(3-i):
        print(p[j],end = "")
    print()