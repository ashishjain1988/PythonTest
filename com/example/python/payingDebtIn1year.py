balance = 3200;
annualInterestRate = 0.2;

from math import ceil
minMonthlyPayment = balance/12.0;
minMonthlyPayment = ceil(minMonthlyPayment);
#print minMonthlyPayment;    
if minMonthlyPayment % 10 != 0:
    remainder = minMonthlyPayment % 10;
    #print remainder;
    if remainder < 5:
        minMonthlyPayment = minMonthlyPayment - remainder;
    else:
        minMonthlyPayment = minMonthlyPayment + (10 - remainder);
flag = False;
#print minMonthlyPayment;
while not flag:
    tempBalance = balance;
    for i in range(0,12):
        monthInterestRate = annualInterestRate/12;
        unpaidbalance =  tempBalance - minMonthlyPayment;
        tempBalance = unpaidbalance + (monthInterestRate*unpaidbalance);
    if(tempBalance <= 0):
        flag = True;
    else:
        minMonthlyPayment += 10; 
print "Remaining balance:" ,int(minMonthlyPayment);