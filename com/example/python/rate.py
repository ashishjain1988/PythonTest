balance = 4842;
annualInterestRate = 0.2;
monthlyPaymentRate = 0.04;
totalPaid = 0;
for i in range(0,12):
    monthIntrest = annualInterestRate/12;
    minimumMonthlypayment = (balance*monthlyPaymentRate);
    totalPaid +=minimumMonthlypayment;
    unpaidbalance =  balance -minimumMonthlypayment;
    balance = unpaidbalance + (monthIntrest*unpaidbalance);
    print "Month:",(i+1),"\n";
    print "Minimum monthly payment:%.2f" % minimumMonthlypayment,"\n";
    print "Remaining balance:%.2f" % balance,"\n";
print "Total paid: %.2f" % totalPaid,"\n";
print "Remaining balance:%.2f" % balance;