def mul_2_3(num):
	if(num%2==0):
		if(num%3==0):
			print("DIVISIBLE BY 2 and 3");
		else:
			print("DIVISIBLE BY 2 but not by 3");
	else:
		if(num%3==0):
			print("Not DIVISIBLE BY 2 but Divisible by 3");
		else:
			print("NOT DIVISIBLE BY EITHER 2 or 3");

a=int(input("ENTER A NUMBER"));
mul_2_3(a);
