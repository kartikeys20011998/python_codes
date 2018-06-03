f=list()
cost=list()

n=int(input("Enter the number of furniture needed"));

for i in range(0,n):
	f.append(input("Enter the furniture name"));
	cost.append(float(input("Enter the cost of furniture")));

furn=input("Enter the furniture name");
quant=int(input("Enter the quantity"));
for i in range(0,n):
	if  furn==f[i]:
		amt=quant*cost[i];
		print("You have purchased ",quant,"quantity of",furn);
		print("Your cost is ",amt);

