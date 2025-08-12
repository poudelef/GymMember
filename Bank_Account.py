class BankAccount:
    count = 0
    def __init__(self, age = None, initial_balance = 0):
        if age < 18:
            raise ValueError("You should be atleast 18 years old")
        self.acc_no = BankAccount.count
        self.age = age
        self.balance = initial_balance
        BankAccount.count += 1

    def get_acc_no(self):
        return self.acc_no

    def get_age(self):
        return self.age

    def change_age(self, age):
        if age < 18:
            raise ValueError("You can't open account. You should be atleast 18 years old")
        self.age = age
        print(f"Your age has been updated to: ", self.age)

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Thanks for depositing ${amount} to account number {self.acc_no}")
            print("Your total balance is: $", self.balance)
            return
        return ValueError("Deposit amount should be more than $0")   

    def withdraw(self, amount):
        if self.balance > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"You took ${amount} from {self.acc_no} account number")
            print("Your total balance is: $", self.balance)
            return
        return ValueError("You don't have sufficient amount in your account")
    



Sambhav_acc = BankAccount(1, 200)
print(Sambhav_acc.get_balance())

