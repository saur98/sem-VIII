# Write a Python function to evaluate the sum of integers between a and b entered by the user that is divisible by 3

a=int(input())
b=int(input())
ans=0
for i in range(a,b+1):
	if i%3==0:
		ans=ans+i
print ans
