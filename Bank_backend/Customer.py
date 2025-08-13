
from Person import *

person1 = Person("David","2000-01-11", "51422164352", "Male", "3023 Marsal Avenue")
person1.person_info()
person1.open_bankAccount(3000)

person2 = Person("Smith","2002-04-18", "5145385929", "Male", "1063 Loveland Avenue")
person2.person_info()
person2.open_bankAccount(5000)

## First time user will get 2x the first deposit
person3 = Person("Linlin","2006-12-18", "5534585929", "Female", "4032 Cristine Avenue")
person3.person_info()
person3.open_firstBankAccount(2000)

person3.firstRewardAccount.deposit(500)

person3.firstRewardAccount.transfer(1000, person1.account)
