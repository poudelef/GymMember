class WithdrawException(Exception):
    """Custom exception for balance-related errors."""
    pass

class DepositException(Exception):
    """Custom exception for deposit-related errors."""
    pass

# @dataclass
# class OpResult:
#     ok: bool
#     message: str
#     balance: float | None = None

class BankAccount:
    __count = 0
    def __init__(self,name, age = None, initial_balance = 0):
        if age < 18:
            raise ValueError("You should be atleast 18 years old")
        BankAccount.__count += 1
        self.__acc_no = BankAccount.__count
        self.__name = name
        self.__age = age
        self._balance = initial_balance
        print(f"Account Name {self.__name}. \nBalance ${self._balance}\n")

    def get_acc_no(self):
        return self.__acc_no

    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name

    def change_age(self, age):
        if age < 18:
            raise ValueError("You can't open account. You should be atleast 18 years old")
        self.__age = age
        print(f"Your age has been updated to: ", self.__age)

    def change_name(self, name):
        self.__name = name
        print(f"Your name has been updated to: ", self.__name)    

    def get_balance(self):
        return self._balance
    

    def viableDepositTransaction(self, amount):
        if amount > 0:
            return
        else:
            raise DepositException(
                f"\n Deposit amount should be greater then $0."
            )
        
    def viableWithdrawTransaction(self, amount):
        if self._balance >= amount:
            return
        else:
            raise WithdrawException(
                f"\nCurrent balance: ${self._balance}, Requested amount: ${amount} \n"
            )    

    def deposit(self, amount):
        try:
            self.viableDepositTransaction(amount)
            self._balance += amount
            print(f"Deposited ${amount} to {self.__name}'s account")
            print(f"Current Balance : ${ self._balance } \n")
        except DepositException as e: 
            print("Deposit failed\n")
            print(e)
    
        
    def withdraw(self, amount):
        try:
            self.viableWithdrawTransaction(amount)
            self._balance -= amount
            print(f"Withdrawed ${amount} from {self.__name}'s account")
            print(f"Current Balance : $ {self._balance}\n")
        except WithdrawException as e:
            print("\nWithDraw failed")
            print(e)    
    
    def transfer(self, amount, account):
        try:
            self.viableWithdrawTransaction(amount)
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"\n\t\t Transferring...... ${amount} to {account.get_name()}\n")
            self.withdraw(amount)
            account.deposit(amount)
            print(f"Success !!!")
            print(f"Your total balance is : ${self._balance}\n")
            print("\t\t\tTransfer Complete \n")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
            
             
        except WithdrawException as e:
            print("\nTransfer failed")
            print(e)    


class FirstAccountReward(BankAccount):
    __count = 0
    def deposit(self, amount):
        if FirstAccountReward.__count == 0:
            self._balance = self._balance + (amount * 2)
            print("Deposit Complete")
            print(f"Total Balance: {self._balance} \n" )

            FirstAccountReward.__count += 1
        else:
            BankAccount.deposit(self,amount)   


    