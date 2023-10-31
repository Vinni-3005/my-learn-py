

''' how to create instance variable ?
  --> inside a constructor '''

class Employee:
    
    def __init__(self,id,name,sal):
       



e1=Employee(101,'Rahul',45000)
e2=Employee(102,'Sonia',55000)
print(e1.__dict__)
print(e2.__dict__)