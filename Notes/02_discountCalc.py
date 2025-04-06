'''
Write a prograam that calculates discount based on the amount of purchase. Ask the
user for the purchase amount and apply the following discount rates:
    No discount if the amount is less than 50
    10% discount if the amount is between 50 and 100
    20% discount if the amount is equal to or over 100
You need to report to the user the final amount after discount. Also tell them how
much discount was applied.


Need to take input from user
    REAL
    Declare

CHECK which discount rate applies
    depends upon amount (the inputted value)
    CHECK using IF statements
'''

# DECLARE originalAmt, finalAmt : REAL
originalAmt = float(input("please enter your purchase amount: "))

if originalAmt >= 100:
    finalAmt = originalAmt * 0.8
    print(f"Your new total is {finalAmt}. You recieved a 20% discount.")
elif originalAmt >= 50 and originalAmt < 100:
    finalAmt = originalAmt * 0.9
    print(f"Your new total is {finalAmt}. You recieved a 10% discount.")
else:
    print(f"Your final total is {originalAmt}. You get no discount")