nub=int(input())
length=len(str(nub))
sum=0
temp=nub
while(temp!=0):
	sum=sum+((temp%10)**length)
	temp=temp//10
if sum==nub:
		print("yes")
else:
			print("no")
