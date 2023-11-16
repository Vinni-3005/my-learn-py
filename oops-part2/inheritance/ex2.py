class parent1:
    def m1(self):
        print("parent1 class-1 method")
    def m2(self):
        print("parent1 class-2 method")

class parent2:
    def m3(self):
        print("parent2 class-1 method")

class child(parent1, parent2):
    def m4(self):
        print("child class method")

c1 =  child()


c1.m1()
c1.m2()
c1.m3()
c1.m4()

