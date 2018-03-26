##PYTHON PROGRAM FOR PRINTING THREE NUMBERS IN INCREASING ORDER
def compare(x,y,z):
	if(x<y):
		if(y<z):
			print(x,y,z);
		else:
			if(x<z):
				print(x,z,y);
			else:
				print(z,x,y);	
	else:
		if(x<z):
			print(y,x,z);
		else:
			if(y>z):
				print(z,y,x);
			else:
				print(y,z,x);

a=int(input("ENTER FIRST NUMBER"))
b=int(input("ENTER SECOND NUMBER"))
c=int(input("ENTER THIRD NUMBER"))
compare(a,b,c);

	
		
