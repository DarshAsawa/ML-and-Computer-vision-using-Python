print("\tVarious way of Looping in Python \n")

# 'while' loop
print("While Loop")
count=0
while count<5 :	
	print(count)
	count+=1
print("\n")

# 'for' loop while defining a set of numbers
print("For Loop with defined set of numbers")
number=[1,2,3]
for numbers in number:
	print(numbers)
print("\n")

# 'for' loop with a single digit range 
print("For Loop with a single digit range(i.e. starting from zero and exclusive of the number)")
for x in range(5):
	print(x)
print("\n")

# 'for' loop with a range between two numbers, and '2' increment x twice before printing.
print("For Loop with a range between two numbers")
for x in range(3,10,2):
	print(x)
