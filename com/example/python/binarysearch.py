balance = 34001;
annualInterestRate = 0.2;

lower = balance/12.0;
upper = (balance * pow((1 + annualInterestRate/12), 12))/12.0;
minMonthlyPayment = (lower + upper)/2;
#print lower," ",upper," ",minMonthlyPayment;
flag = False;
while not flag:
    tempBalance = balance;
    for i in range(0,12):
        monthInterestRate = annualInterestRate/12;
        unpaidbalance =  tempBalance - minMonthlyPayment;
        tempBalance = unpaidbalance + (monthInterestRate*unpaidbalance);
    if(tempBalance > 0.01):
        lower = minMonthlyPayment;
        minMonthlyPayment = (minMonthlyPayment + upper)/2;
    elif(tempBalance < -0.01):
        upper = minMonthlyPayment;
        minMonthlyPayment = (minMonthlyPayment + lower)/2;
    else:
        flag = True;
    #print tempBalance,minMonthlyPayment; 

print "Lowest Payment:%.2f" % minMonthlyPayment;