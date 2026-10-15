class BankAccount: 

  bank_name = "PyBank"      # class attribute: shared by all objects 
  MIN_BALANCE = 0.0 
  total_accounts = 0
  def __init__(self, owner: str, balance: float = 0.0) -> None: 

        self.owner = owner                # instance attribute 
        self.balance = balance            # instance attribute 
        self.transactions = [] 
        BankAccount.total_accounts += 1
        if self.balance<self.MIN_BALANCE:
            raise ValueError("add min balance")
        @staticmethod
        def is_valid_owner(owner):
           if owner.split().isalpha() and len(owner)>2:
              return True
           else:
              return False
           

  @staticmethod
  def validate_amount(amount):
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise ValueError("Enter a valid amount")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        return amount


  @staticmethod
  def format_money(amount):
        return f"{amount:,.2f}"

        
  def deposit(self, amount: float) -> float:
      BankAccount.validate_amount(amount)
      balancebefore=self.balance
      self.balance+=amount
      self.transactions.append(("deposit",balancebefore,self.balance))
      print(f"New balance {self.balance}")

  def print(self):
    print(f"Name {self.owner}")
    print(f"Balance {self.balance}")

  def withdraw(self, amount: float) -> float:
    amount = BankAccount.validate_amount(amount)

    if amount > self.balance:
        raise ValueError("Insufficient funds")

    balance_before = self.balance
    self.balance -= amount

    self.transactions.append(
        ("withdraw", balance_before, self.balance)
    )

    print(f"New balance: {self.format_money(self.balance)}")
    return self.balance

  def summary(self):
   print(f"{self.owner} . {self.balance :,.2f}")

  def transfer_to(self, other, amount):
     self.withdraw(self,amount)
     other.deposit(amount)
   