# Write a Python program to print the series of prime numbers until the number entered by the user

num=int(input())
for i in range(2,num):
	flag=0
	for j in range(2,i):
		if i%j==0:
			flag=1
			break
	if flag==0:
		print i
