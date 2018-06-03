a=input("ENTER THE STRING ");
b=a.upper();
data={'0':0};
for i in range(0,len(b)-1):
	for key in data:
		if b[i]==key:
			data[key]=data[key]+1;
		else:
			data.update({b[i]:1});
for key in data:
	print(key,data[key]);

			
