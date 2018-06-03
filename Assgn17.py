a=input("ENTER FIRST STRING");
b=input("ENTER SECOND STRING");
c="";
for i in range(0,len(a)):
	if a[i].isupper() == True:
		c=c+a[i];
for i in range(0,len(b)):
	if b[i].isupper() == True:
		c=c+b[i];

print(c);
