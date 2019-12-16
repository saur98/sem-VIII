# Write a Python function to find the roots of a quadratic equation

a=int(input())
b=int(input())
c=int(input())

check=b*b-4*a*c
if check>=0:
	root1=(-1*b+pow(check,0.5))/(2*a)
	root2=(-1*b-pow(check,0.5))/(2*a)
	print root1,root2
