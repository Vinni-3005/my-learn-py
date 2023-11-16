class parent:
    def parent1(self):
        print("This is first parent method")
    def parent2(self):
        print("this is second parent method")

class child(parent):
    def child1(self):
        print("inheriting the properties of parent child")

c1 = child()
c1.parent1()
c1.parent2()
c1.child1()


'''
class Parent:
    def m1(self):
        print("Parent Class - m1 method")

    def m2(self):
        print("Parent Class - m2 method")


class Child(Parent):
    def m3(self):
        print("Child Class - m3 method")


c1 = Child()
c1.m1()
c1.m2()
c1.m3()'''

