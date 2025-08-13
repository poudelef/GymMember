import datetime
class Person:
    __count = 0 # class variabe aka static field
    
    __MAX_DOB_UPDATES = 3
    __registered_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    def __init__(self, name = "", __DOB = "", phoneNumber = "", gender = "", address = "", ): # __init__ is a constructor in python
        Person.__count += 1
        self.name = name
        self.DOB = __DOB
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.address = address
        self.__registered_date = Person.__registered_date
        self.__DOB_count = 1
    

    def update_DOB(self, new_DOB):
        if self.__DOB_count > Person.__MAX_DOB_UPDATES:
            raise PermissionError("You already updated your DOB 3 times, you can't update it anymore. Please contact support if you need to update it again.")
            return False
        else:
            self.DOB = new_DOB
            if self.__DOB_count - Person.__MAX_DOB_UPDATES == 0:
                print("You can't update your DOB anymore")
            else:    
                print(f"DOB Updated Successfully, You can update it {Person.__MAX_DOB_UPDATES-self.__DOB_count} more times")

            self.__DOB_count += 1
            return True
    
    def calculate_age(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.DOB, "%Y-%m-%d").date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def person_info(self):
        return {
            "Name:": self.name, 
            "DOB": self.DOB, 
             "Age": self.calculate_age(),
            "Phone Number": self.phoneNumber, 
            "Gender": self.gender, 
            "Address": self.address, 
            "Registered Date": self.__registered_date,
            }
    

# Sambhav = Person("Sambhav", "2005-01-31", "513-276-2979", "Male", "1234 Elm St, Springfield, IL")    
# print(Sambhav.person_info())

# Sambhav.update_DOB("2005-02-01")
# Sambhav.update_DOB("2005-02-02")
# Sambhav.update_DOB("2005-02-03")
# Sambhav.update_DOB("2005-02-04")
# Sambhav.update_DOB("2005-02-05")


