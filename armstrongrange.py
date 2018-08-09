n=int(raw_input())
for i in range(n):
	num=i
	result=0
	len(str(i))
	while(i!=0):
		digit=i % 10
		result=result+digit**n
		i=i//10
		if(num==result):
			print(num,end" ")
