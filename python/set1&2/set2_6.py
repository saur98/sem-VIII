""" Write a program called time.py that prompts the user to enter the
current time in HH:MM format, and then prints a message that states the time in a
sentence """

tim = raw_input("What is the time please (HH:MM)? ")
x,y = tim.split(":")
print "Thanks! It is now ",y," minutes after ",x,"o'clock"
