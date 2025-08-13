import datetime
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
        return {
            "name:": self.name, 
            "DOB": self.DOB, 
             "age": self.calculate_age(),
            "phone number": self.phoneNumber, 
            "gender": self.gender, 
            "address": self.address, 
            "registered date": self.__registered_date,
            }
    
