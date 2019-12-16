# Write PYTHON programs to get the following patterns

line=input()
k=0
for i in range(1,line+1):
	for j in range(i):
		k=k+1
		print k,
	print
for i in range(1,line+1):
	for j in range(line-i):
		print " ",
	for j in range(i):
		if i%2==0:
			print "!",
		else:
			print "#",
	print
