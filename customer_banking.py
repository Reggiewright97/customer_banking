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
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('What is your savings account balance?'))
    savings_interest = float(input('What is the APR for the savings account?'))
    savings_maturity = int(input('What is the length of the months for your savings account?'))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the saving account.')
    print("The balance is: $", format(savings_balance, ',.2f'))
    print("APR Interest Rate is:", format(savings_interest, '.2f'),'%')
    print(f"Length of CD is: {savings_maturity} months.")
    print("CD interest earned would be : $", format(savings_interest_earned, ',.2f'))
    print(f"your projected CD balance would be: ${updated_savings_balance}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('What is your CD account balance?$'))
    cd_interest = float(input('What is the APR for the CD account?'))
    cd_maturity = int(input('What is the length of months for your CD account?'))

    
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_cd_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the CD account.')
    print("The balance is: $", format(cd_balance, ',.2f'))
    print("APR Interest Rate is:", format(cd_interest, '.2f'),'%')
    print(f"Length of CD is: {cd_maturity} months.")
    print("CD interest earned would be : $", format(interest_cd_earned, ',.2f'))
    print(f"your projected CD balance would be: ${updated_cd_balance}")
   
    
    

if __name__ == "__main__":
    main()
    
    
   
