a=input("ENTER THE STRING");
start=0;
end=len(a)-1;
f=0;
while start<end:
	if a[start]==a[end]:
		start=start+1;
		end=end-1;
		continue;
	else:
		f=1;
		break;

if f==1:
	print("STRING IS NOT PALINDROME");
else:
	print("STRING IS PALINDROME");

for i in a:
	print(i,end=",");
print("\n");
for i in range(len(a)-1,-1,-1):
	print(a[i],end=",");
