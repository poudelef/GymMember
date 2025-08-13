import datetime
class Person:
    count = 0
    DOB_count = 0
    __registered_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    def __init__(self, name = "", __DOB = "", phoneNumber = "", gender = "", address = "", ):
        Person.count += 1
        self.name = name
        self.DOB = __DOB
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.address = address
        self.__registered_date = Person.__registered_date
    

    def update_DOB(self, new_DOB):
        if Person.DOB_count > 4:
            raise Exception("You can only update your DOB three times")
        self.DOB = new_DOB
        Person.DOB_count += 1
        print(f"DOB Updated Successfully, You can update it {3-Person.DOB_count} more times")
        return True
    
    def calculate_age(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.DOB, "%Y-%m-%d").date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def Person_info(self):
        return {
            "Name:": self.name, 
            "DOB": self.DOB, 
             "Age": self.calculate_age(),
            "Phone Number": self.phoneNumber, 
            "Gender": self.gender, 
            "Address": self.address, 
            "Registered Date": self.__registered_date,
            }
    

Sambhav = Person("Sambhav", "2005-01-31", "513-276-2979", "Male", "1234 Elm St, Springfield, IL")    
print(Sambhav.Person_info())