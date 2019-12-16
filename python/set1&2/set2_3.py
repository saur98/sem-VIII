# Insert a string 12.5 4.56 7.22 and the output should be the sum of the numbers separated by 

inp2='1.1#2.2#3.3'
l=inp2.split('#')
ans=0.0
for i in l:
	ans=ans+float(i) 
print(ans)
