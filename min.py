## PYTHON PROGRAM FOR FINDING THE MINIMUM OF THREE NUMBERS
def min(x,y,z):
	if(x<=y and x<=z):
		print(x,"is minimum");
	elif(y<=x and y<=z):
		print(y,"is minimum");
	else:
		print(z,"is minimum");

a=int(input("ENTER FIRST NUMBER"));
b=int(input("ENTER SECOND NUMBER"));
c=int(input("ENTER THIRD NUMBER"));
min(a,b,c);

