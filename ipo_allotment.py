import random

i = 0
list = []
while(i<500):
	num = random.randint(3156344500, 3156390000)
	list.append(num)
	i+=1
print(list)

# take input from user
num = int(input("Enter Your Transaction Number : "))

# check for entered num in list
if num in list:
	print("You got the IPO")
else:
	print("Better Luck Next Time!, Your Money will be releazed by tomorrow!")