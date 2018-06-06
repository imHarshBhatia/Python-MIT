# Paste your code into this box
min_bal = 0
max_bal = balance
while True:
    a = balance
    monthly = (min_bal+max_bal)/2
    for i in range(12):
        a = (a - (monthly)) + (annualInterestRate/12 * (a - (monthly)))
    if a<=0.01 and a>=-0.01:
        break
    else:
        if a > 0:
            min_bal = monthly
        else:
            max_bal = monthly
print("Lowest Payment: " + str(round(monthly,2)))
