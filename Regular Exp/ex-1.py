
# Regular expression is a sequence of characters that forms a search pattern 

#Regular exp can be used to check if a string contains the specified search pattern.


#check whether it is indian mobile or not
import re
mobileno = input("Enter a number : ")

mobile =re.fullmatch("[6-9]\d{9}",mobileno)

if mobile != None :
    print("this is indian phne number")
else:
    print("not a valid phne number")


