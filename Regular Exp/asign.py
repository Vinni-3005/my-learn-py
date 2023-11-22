
'''i have data.txt file , in that there is some context is there including phone numbers and emails
so, i have to extract all the phone numbers and emails and write it to the new file'''

import re

phpattern= ('\+?(91)?[ -]?[6-9]\d{9}\b')
emailpattern = ('[a-zA-Z0-9]+@[A-Za-z0-9]+.com')

fp=open('data.txt','r')
data= fp.read()
fp.close()

phone_numbers= re.findall(phpattern,data)
emails = re.findall(emailpattern,data)

new_fp=open('newfile.txt','w')

new_fp.write("Phone numbers:\n")
for phone in phone_numbers:
    new_fp.write(phone + '\n')

new_fp.write("emails:\n")
for email in emails:
    new_fp.write(email +'\n')

new_fp.close()
