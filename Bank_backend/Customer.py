from Bank_Account import *

Sambhav = BankAccount("Sambhav", 20,  700)

Ruksha = FirstAccountReward("Ruksha", 21, 0)


Ruksha.deposit(300)
Ruksha.deposit(300)
Ruksha.deposit(300)



print(Ruksha.get_balance())

Ruksha.transfer(200, Sambhav)