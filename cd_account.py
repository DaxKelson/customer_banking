"""Import the Account class from the Account.py file."""
from Account import Account  
print("Running cd_account.py")
def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """

    account = Account(balance, interest_rate)

   
    interest_earned = balance * (interest_rate / 100 / 12) * months

    
    updated_balance = balance + interest_earned

    
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned