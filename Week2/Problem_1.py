# Paste your code into this box
for i in range(12):
    balance = (balance - (balance*monthlyPaymentRate)) + (annualInterestRate/12 * (balance - (balance*monthlyPaymentRate)))
    
print("Remaining balance: " + str(round(balance,2)))
