# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompting the user to select type of account to calculate interest earned     

    while True:
        calculate_balance = input("Calculate balance for (C)D accout, (S)avings account or (Q)uit ").upper()
        if calculate_balance == 'C':
            account_type = "CD account"
        elif calculate_balance == 'S':
            account_type = "savings account"
        else:
            False
            break

    # Prompt the user to set the balance, interest rate, and months for the selected account type.
    # ADD YOUR CODE HERE
    
        account_balance = float(input(f"Please enter {account_type} account balance? "))
        account_interest = float(input(f"Enter annual interest rate on {account_type} ? "))
        account_maturity = float(input("Please enter time period in years to calculate intereste earned ? "))
        account_maturity_months = account_maturity * 12


        match(calculate_balance):
#        if calculate_balance == 'S':
            case 'S':
            # Call the create_savings_account function and pass the variables from the user.
                updated_balance, interest_earned = create_savings_account(round(account_balance,2), round(account_interest,2), account_maturity_months)

            case 'C':
            # Call the create_cd_account function and pass the variables from the user.             
                updated_balance, interest_earned = create_cd_account(round(account_balance,2), round(account_interest,2), account_maturity_months)
 
        # Print out the interest earned and updated CD account balance with interest earned for the given months.
        # ADD YOUR CODE HERE

        print(f"On {account_type} with ${account_balance}, earning {account_interest}% interest per year, interest earned after {account_maturity} years will be ${interest_earned}")
        print(f"Updated balance for {account_type} at the end of {account_maturity} years will be ${updated_balance}")

# call main() function

if __name__ == "__main__":
    main()


