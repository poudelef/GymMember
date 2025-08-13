import datetime
from Bank_Account import *

class Person:
    __count = 0 # class variabe aka static field
    MAX_DOB_UPDATES = 3

  
    def __init__(self, name = "", __DOB = "", phoneNumber = "", gender = "", address = "", ): # __init__ is a constructor in python
        Person.__count += 1
        self.name = name
        self.DOB = __DOB
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.address = address
        self.__registered_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        self.__DOB_count = 1
        self.account: BankAccount | None = None
        self.firstRewardAccount: FirstAccountReward | None = None

    

    def update_DOB(self, new_DOB):
        if self.__DOB_count > Person.MAX_DOB_UPDATES:
            raise PermissionError("You already updated your DOB 3 times, you can't update it anymore. Please contact support if you need to update it again.")
        else:
            self.DOB = new_DOB
            if self.__DOB_count - Person.MAX_DOB_UPDATES == 0:
                print("You can't update your DOB anymore")
            else:    
                print(f"DOB Updated Successfully, You can update it {Person.MAX_DOB_UPDATES-self.__DOB_count} more times")

            self.__DOB_count += 1
            return True
    
    def calculate_age(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.DOB, "%Y-%m-%d").date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def person_info(self):
        print(f"\n Name: {self.name}\n Date of Birth: {self.DOB} \n Age: {self.calculate_age()} \n Phone Number: {self.phoneNumber} \n Gender: {self.gender} \n Address: {self.address} \n Registered Date: {self.__registered_date} \n" )
        return 

    def open_bankAccount(self, amount):
        print("Account Created")
        self.account = BankAccount(self.name, self.calculate_age(), amount)
        return self.account 
    
    def open_firstBankAccount(self, amount):
        print("First time accound created")
        self.firstRewardAccount = FirstAccountReward(self.name, self.calculate_age(), amount)
        return self.account 
    
