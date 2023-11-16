from json import loads, load, dumps,dump
fp=open('emp.json','r')
emp_List=load(fp)

print(type(emp_List))

for emp in emp_List:
    if emp['gender']=="Male":
	    #print(emp['name'])
	    print(emp)
	
fp.close()

fp1=open('emp.csv','w')
emp_List=load(fp1)
print(type(emp_List))
fp1.close()