from prettytable import PrettyTable

# Program to calculate the average marks of your subjects
print("\t\t Average Marks Calculator\n")

#asking for number of subjects
no_subjects=int(input("Enter the number of subjects:"))

#asking for label of subjects.
Subjects=[]
Marks=[]
print("\n\tEnter the name for your respective subjects \n")
for i in range(no_subjects):
    subject=input("Subject %d: " % (i+1))
    Subjects.append(subject)
    mark=int(input("Enter marks for %s: " % subject))
    Marks.append(mark)
    print("\n")


#Displaying Report Card...................................

print("\n\t\t REPORT CARD\n")

table = PrettyTable()
table.field_names=["Subject","Marks"]

Count=len(Subjects)
    
for a in range(Count):
    subject = Subjects[a]
    mark = Marks[a]
    table.add_row([subject,mark])

print(table)


#maximum marks that can be scored:
max_marks=100*no_subjects 

#Calculating Total marks scored
total=0
for x in Marks:
    total+=x
print("\t\nTotal marks out of %d is: %d" % (max_marks,total))

#finding the percentage scored in this semesters
Percentage=(total/max_marks)*100
print("\t\nPercentage scored: ",Percentage,"%")


