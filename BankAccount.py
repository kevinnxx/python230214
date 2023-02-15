# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    #def print(self):
        #print("{0}, {1}, {2}".format(self.id, 
        #self.name, self.balance))
    def __str__(self):
        return "{0}, {1}, {3}".format(self.__id, self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#account1.print()
#account1.balance = 150000000
print(account1._BankAccount__balance)


