
#check whether it is valid gst number or not

import re

gstin = input("enter a gst number :")

gstno=re.fullmatch('[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}',gstin)


if gstno != None:
    print(" It is valid gst number")
else:
    print("It is not a valid gst number")