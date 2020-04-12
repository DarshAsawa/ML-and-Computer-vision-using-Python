#FUNCTIONS ARE DEFINED BY USING 'def' KEYWORD.

# sum function to add two numbers passed as arguments...
def sum(a,b):
	return a+b

#function to print welcome messages...
def welcome():
	print("Hello and welcome!")

welcome()

def welcome1(user,greet):
	print("Hello %s , %s !!" % (user,greet))

name=input("Enter your name: ")
welcome1(name,"you are most welcome")



print("\nExample : ")

print("Adding two numbers -")
#inputs to be asked in order to be passed to sum function...
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
print("Sum of two numbers : %d " % sum(number1,number2))


print("\n")


#USING FUNCTIONS TO PRINT ITS OWN BENEFITS, i.e. WHAT BENEFITS YOU GET IN PYTHON BY USING FUNCTIONS.
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
