a=input("ENter the first string");
b=input("ENter the second string");
c=a+b
d=len(c)
for i in range(0,d):
	if(c[i].isupper()):
		print(c[i],end="");
