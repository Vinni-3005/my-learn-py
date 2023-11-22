
# check whether it is Correct vehicle number or not

import re

vehicle = input("Enter Vehicle number")

vehicleno = re.fullmatch('[A-Z]{2}\d{2}[A-Z]{2}\d{4}',vehicle)

if vehicleno != None:
    print("It is a valid vehicle number")

else:
    print("it is not valid number")