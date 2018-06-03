s=input("ENTER THE STRING");
s2=s.upper()
s_sort="".join(sorted(set(s2)))
la=len(s2)
lb=len(s_sort)
counter=0
for i in range(0,lb):
	for j in range(0,la):
		if s_sort[i]==s2[j]:
			counter=counter+1;
			
	print(s_sort[i],counter);
	counter=0;

