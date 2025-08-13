# Bank Backend (OOP)

A small, self-contained Python project that demonstrates Object-Oriented Programming concepts for a banking domain: accounts, first-deposit rewards, people, transfers, and custom error handling.

## Features

**BankAccount**:

1. Create accounts with name, age, initial balance.
2. Deposit and withdraw with validation
3. Transfer funds between accounts
4. Custom exceptions: DepositException, WithdrawException

**FirstAccountReward (subclass)**:

1. Overrides deposit to double the first deposit
2. Falls back to base deposit afterwards

**Person (composition)**

1. A Person has a BankAccount and/or a FirstAccountReward
2. DOB tracking, age calculation, and limited DOB updates
3. Helper methods to open accounts

---

## Installation

Clone this repo

## 🛠️ How to Use

```python
# Create a customer
python Customer.py
#(Optional) Sanity-check the account classes
python Bank_Account.py

# Get member info
print(member1.get_member_id())        # e.g., 1
print(member1.get_full_name())        # "Alice Johnson"

from Person import Person

p1 = Person("David","2000-01-11","51422164352","Male","3023 Marsal Avenue")
p1.person_info()                      # prints profile
p1.open_bankAccount(3000)             # creates and stores p1.account (BankAccount)
print(p1.account.get_balance())       # 3000

p2 = Person("Smith","2002-04-18","5145385929","Male","1063 Loveland Avenue")
p2.open_bankAccount(5000)

p3 = Person("Linlin","2006-12-18","5534585929","Female","4032 Cristine Avenue")
p3.open_firstBankAccount(2000)        # creates and stores p3.firstRewardAccount
p3.firstRewardAccount.deposit(500)    # first deposit doubled

# Transfer from Linlin's reward account to David's regular account:
p3.firstRewardAccount.transfer(1000, p1.account)   # pass a BankAccount, not a Person


## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit changes with clear messages.
4. Open a pull request describing the change and reasoning.
```
