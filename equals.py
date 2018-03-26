def equality(x,y):
	if(x==y):
		print("x and y are equal");
		if(y!=0):		
			print("THEREFORE ",x,"/",y," is ",x/y);
	elif(x<y):
		print(x," is smaller than y");
	else:
		print(y," is smaller than",x);

a=int(input("ENter first number"));
b=int(input("enter second number"));
equality(a,b);
print("THANKS FOR COMING,DO COME AGAIN ");
