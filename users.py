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
laura = User("Laura Coto","lcoto@python.com")

print ("=== Have the first user make 3 deposits and 1 withdrawal and then display their balance ===")
carlos.make_deposit(100)
carlos.make_deposit(200)
carlos.make_deposit(200)
carlos.display_user_balance()
print ("=== Have the second user make 2 deposits and 2 withdrawals and then display their balance ===")
edgar.make_deposit(100)
edgar.make_withdrawal(200)
edgar.make_deposit(300)
edgar.make_withdrawal(200)
edgar.display_user_balance()
print ("=== Have the third user make 1 deposits and 3 withdrawals and then display their balance ===")
laura.make_deposit(1000)
laura.make_withdrawal(200)
laura.make_withdrawal(100)
laura.make_withdrawal(300)
laura.display_user_balance()
print ("=== Have the first user transfer money to the third user and then print both users' balances ===")
carlos.transfer_money(laura, 100)
print ("Laura balance:")
laura.display_user_balance()