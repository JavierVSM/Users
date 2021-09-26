class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
        print ("Your deposit was succeed. You have $", self.account_balance, "in your account")
  
    def make_withdrawal(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print ("Your withdrawal was succeed. You have $", self.account_balance, "in your account")
        else:
            print( "We cannot process your withdrawal." )
            print( f"You currently have {self.account_balance}." )
            print( f"And you are trying to withdraw {amount}." )
        return self
  
    def display_user_balance(self):
        print ("You have $", self.account_balance, "in your account")
      
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print ("You successfully transferred $", amount, "to", other_user.name)
        print ("You have $", self.account_balance, "in your account")

carlos = User("Carlos Mora", "cmora@python.com")
edgar = User("Edgar Fuentes","efuentes@python.com")

print ("Deposit $100")
carlos.make_deposit(100)
print ("Withdrawal $20")
carlos.make_withdrawal(20)
print ("Display balance")
carlos.display_user_balance()
print ("Transfer $30 to Edgar")
carlos.transfer_money(edgar,30)
print ("Display balance of Edgar")
edgar.display_user_balance()