# Paste your code into this box
flag,init_bal = True,10
while flag:
    a = balance
    for i in range(12):
        a = (a - (init_bal)) + (annualInterestRate/12 * (a - (init_bal)))
    if a <= 0:
        flag = False
    else:
        init_bal += 10    
print("Lowest Payment: " + str(init_bal))    
