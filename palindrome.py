b=int(input())
temp=b
rev = 0
while (temp !=0):
	rev=(rev*10)+(temp%10)
	temp=temp//10
if (b==rev):
		print("yes")
else:
			print("no")
	
