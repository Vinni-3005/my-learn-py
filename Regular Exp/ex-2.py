

#check how many a's are there in a given name and return index value

import re

name = input("enter a name")

numberofa=re.finditer('[a]',name)

for number in numberofa:
    print(number.start(),'...' + 'a')