from abc import *


class Account:
    @abstractmethod
    def cal_bal(self):
        return 
    

a1 = Account()
print(a1)
print(id(a1))