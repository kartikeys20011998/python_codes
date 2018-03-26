n=int(input("Enter the number"));
f=0;
for i in range(2,(int)(n/2+1)):
	if n%i==0:
		f=1;

if f==1:
	print("NON-PRIME");
elif f==0:
	print("PRIME");
