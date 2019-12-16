# Write a Python function to evaluate power function using while loop

num=int(input())
power=int(input())
ans=1
for i in range(power):
	ans=num*ans
print ans
