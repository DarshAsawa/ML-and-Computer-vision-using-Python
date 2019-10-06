
# Program to calculate the average marks of your subjects
print("\t\t Average Marks Calculator\n")

#asking for number of subjects
no_subjects=int(input("Enter the number of subjects:"))

marks=[]
for i in range(no_subjects):
    mark=int(input("Enter marks for subject %d: " % (i+1)))
    marks.append(mark)

max_marks=100*no_subjects

total=0

for x in marks:
    total+=x

print("\nTotal marks out of %d is: %d" % (max_marks,total))

avg_marks=total/no_subjects
print("\nAverage Mark scored is %d" % avg_marks)

Percentage=(total/max_marks)*100
print("\nPercentage scored: ",Percentage,"%")
