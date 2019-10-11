
information={}
n = int(input("Enter the range for iterations: "))
for i in range(n):
        name = input("Enter your name: ")
        poc = input("Enter your birth place: ")
        information[name] = poc

        
for name,place in information.items():
        print(name,place)


