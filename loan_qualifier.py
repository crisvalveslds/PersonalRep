# Loan Qualifier Application
# This script collects user information to determine loan qualification.
print("Welcome to the Loan Qualifier Application!")
print("For each of these questions enter a value between 1-10:")

loan_size = int(input("What is the size of the loan? "))
credit_score = int(input("How good is your credit score? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is the down payment you can provide? "))

should_loan = False

if loan_size >= 5:
    if credit_score >= 7 and income >= 7:
        should_loan = True
    elif credit_score >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if credit_score < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print("Congratulations! You qualify for the loan.")
else:
    print("We are sorry. You do not qualify for the loan.")