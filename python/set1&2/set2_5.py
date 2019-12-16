""" Write a Python program to create a very simple pizza-ordering
menu.  At this pizzeria, theres only one kind of pizza you can order:  cheese pizza with
no toppings.  Your choices are what size of pizza, and how many of them.  Youll need to
figure out the total price of the order.  A small pizza costs Rs. 200, a medium Rs. 350,
and a large Rs. 500 """

size = raw_input("What size would you like? a. small (200)  b. medium (350)  c. large (500) Please enter a or b or c:")
count = int(input("How many would you like?"))
if size=='a':
	print(350*count)
elif size=='b':
	print(350*count)
elif size=='c':
	print(350*count)		
 
