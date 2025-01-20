class BankAccount:
  """
  A simple bank account class to demonstrate OOP concepts.
  """

  def __init__(self, initial_balance=0.0):
    """
    Initializes a bank account with a starting balance.

    Args:
      initial_balance (float, optional): The initial balance of the account. Defaults to 0.0.
    """
    self.account_balance = initial_balance

  def deposit(self, amount):
    """
    Deposits a specified amount into the account balance.

    Args:
      amount (float): The amount to deposit.
    """
    self.account_balance += amount

  def withdraw(self, amount):
    """
    Withdraws a specified amount from the account balance if sufficient funds exist.

    Args:
      amount (float): The amount to withdraw.

    Returns:
      bool: True if the withdrawal was successful, False otherwise.
    """
    if amount <= self.account_balance:
      self.account_balance -= amount
      return True
    else:
      return False

  def display_balance(self):
    """
    Prints the current balance of the account in a user-friendly format.
    """
    print(f"Current Balance: ${self.account_balance:.2f}")
