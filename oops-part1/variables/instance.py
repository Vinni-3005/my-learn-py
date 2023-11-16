

''' how to create instance variable ?
  --> inside a constructor '''

# variable value is varied from obj to obj, we use instance variable


class Employee:
    
    def __init__(self,id,name,sal):
        self.acc_id=id
        self.name_name=name
        self.sal_sal=sal
       



e1=Employee(101,'Rahul',45000)
e2=Employee(102,'Sonia',55000)
print(e1.__dict__)
print(e2.__dict__)