

#if variable value is not varied from obj to obj , then we use static variable

class Employee:
    org_name='Mphasis'
    or_loc='Bengaluru'
    def __init__(self,id,name,sal):
        self.acc_id=id
        self.acc_name=name
        self.acc_sal=sal

e1=Employee(101,'abc',34000)
e2=Employee(102,'xyz',23000)
print(e1.__dict__)
print(e2.__dict__)
print(Employee.__dict__)
