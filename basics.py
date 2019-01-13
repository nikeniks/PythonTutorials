address=["Ashokvan dahisar East", "1701" , "Mumbai"]
pins = {"nikhil":1234,"shantanu":2222,"daya":3333}

print (address[0], address[1])

pin = int(input("Enter Valid pin !!!"))
def check_pin():
    if pin in pins.values():
        print("Welcome !!")
        fruit= input("Please select fruit coice!!")
        #print("Please select fruit choice!!")
        filename = open("sample.txt","r")
        fruits=filename.read()
        fruits=fruits.splitlines()
        if fruit in fruits:
            print("enjoy your " + fruit )
        else:
            print(fruit + " is out of stock come back later !!!!")
    else:
        print("Invalid Pin XXXX")

#def check_Fav_Fruit():
check_pin()