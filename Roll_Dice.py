import random 
no_of_dices=int(input("how many dice you want :"))
end_count=no_of_dices*6
print("Since you are rolling %d dice or dices, you will get numbers between 1 and %d" % (no_of_dices,end_count))
count=1
while count==1 :
	user_inp=input("Do you want to roll a dice : ")
	if user_inp=="yes" or user_inp=="y" or user_inp=="Y":
		print("Your number is : %d" % random.randrange(1,end_count,1))
	else :
		break
