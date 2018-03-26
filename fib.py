n=int(input("ENter the range"));
a=0;
b=1;
i=1;
c=0;
while c<=n:
	if(i==1):
		print(a);
		c=a+b;
		a=b;
		b=c;
		i=i+1;
		continue;
	print(c);
	c=a+b;
	a=b;
	b=c;
	i=i+1;

