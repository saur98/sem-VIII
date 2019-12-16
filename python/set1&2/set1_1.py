""" Write a Python function to swap two numbers	 """
def swap(a,b):
	return b,a

a=int(input())
b=int(input())
print a,b
a,b=swap(a,b)
print a,b
