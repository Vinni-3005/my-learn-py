#case 1
num=int(input("enter a number"))
if(num>=100 and num<=999):
    print("its a 3-dgit number")
else:
    print("its not a 3-digit number")


#case 2

num=100
if len(str(num))==3:
    print("its a 3-digit number")
else:
    print("its not a 3-digit number")

