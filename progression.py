N,A,D=map(int,input().split())
sum=0
for b in range(N):
	sum=sum+A
	A=A+D
	b=b+1
print(sum)
