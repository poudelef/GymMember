class BankAccount:
    __count = 0
    def __init__(self, age = None, initial_balance = 0):
        if age < 18:
            raise ValueError("You should be atleast 18 years old")
        BankAccount.__count += 1
        self.__acc_no = BankAccount.__count
        self.__age = age
        self.__balance = initial_balance

    def get_acc_no(self):
        return self.__acc_no

    def get_age(self):
        return self.__age

    def change_age(self, age):
        if age < 18:
            raise ValueError("You can't open account. You should be atleast 18 years old")
        self.__age = age
        print(f"Your age has been updated to: ", self.__age)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Thanks for depositing ${amount} to account number {self.__acc_no}")
            print("Your total balance is: $", self.__balance)
            return
        return ValueError("Deposit amount should be more than $0")   

    def withdraw(self, amount):
        if self.__balance > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"You took ${amount} from {self.__acc_no} account number")
            print("Your total balance is: $", self.__balance)
            return
        return ValueError("You don't have sufficient amount in your account")
    



Sambhav_acc = BankAccount(20, 2000)

Sambhav_acc.change_age(21)
Sambhav_acc.deposit(1000)
Sambhav_acc.withdraw(500)
