# Write a Python function to find the greatest of 3 numbers

a=int(input())
b=int(input())
c=int(input())

if a>b and a>c:
	print a
elif b>c and b>a:
	print b
elif c>a and c>b:
	print c
