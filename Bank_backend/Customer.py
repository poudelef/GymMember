from Bank_Account import *

Sambhav = BankAccount("Sambhav", 20,  2000)
Ruksha = BankAccount("Ruksha", 19, 3000)

# Sambhav.withdraw(2001)
# # Sambhav.withdraw(1000)
# Ruksha.deposit(0)

Sambhav.transfer(1000, Ruksha)

print(f"Ruksha balance {Ruksha.get_balance()}")