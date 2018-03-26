
cid=int(input("Enter the customer id"));##TAKING THE CUSTOMER ID
bill_amt=float(input("Enter the bill amount"));## TAKING THE BILL AMOUNT

if cid>=101 and cid<=1000:
	if bill_amt<500.0:
		dis=.01;
	elif bill_amt>=500.0 and bill_amt<1000.0:
		dis=0.02;
	else:
		dis=0.05;
	dis_bill_amt=bill_amt+bill_amt*dis;
	print("BILL AMOUNT IS ",dis_bill_amt);

else:
	print("INVALID CUSTOMER ID ");

