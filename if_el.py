bill_id=1001
customer_id=101
bill_amount=200.0
discounted_bill_amount=0.0;
print("BILL ID :",bill_id);
print("Customer ID:",customer_id);
print("Bill AMount : Rs - ",bill_amount);
if bill_amount> 500:
	discounted_bill_amount=bill_amount-bill_amount*2/100;
else:
	discounted_bill_amount=bill_amount-bill_amount*1/100;
print("DISCOUNTED BILL AMOUNT: Rs.",discounted_bill_amount);
