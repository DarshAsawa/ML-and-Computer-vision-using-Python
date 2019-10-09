import random
import time

print("\tGuess a Number: ")
wish=input("Do you wanna play this game : ")
if wish=="yes" or wish=="y" or wish=="Y" or wish=="YES" or wish=="Yes":
        time.sleep(1)
        choice=1
        while choice==1 :
       
                print("Let's start the game by first setting the range of numbers :")
                range_start=int(input("Enter the starting number: "))
                range_end=int(input("Enter the ending number: "))

                a=1
                while a==1 :
                        random1=random.randrange(range_start,range_end,1)
                        print("\nA random number is: %d " % random1)
                        time.sleep(1)
                        guess=int(input("Now you guess the next number (in the range only):"))
                        random2=random.randrange(range_start,range_end,1)
                        if random2>random1 and guess>random1:
                                if random2==guess:
                                        print("Your guess is equal to the next number..CONGRATS !!!")
                                else:
                                        print("Congrats your guess and next number, both are greater than the random number")
                        elif random2<random1  and guess<random1 :
                                if random2==guess:
                                        print("Your guess is equal to the next number..Congrats")
                                else:
                                        print("Congrats your guess and next number, both are lower than the random number")
                        else: 
                                print("Wrong Guess")
                                print("Better luck next time. :) " )
                        time.sleep(1)

                        user=input("\nDo you wanna start again? (yes or no )" )
                        if user=="yes" or user=="Y" or user=="y" or user=="YES":
                                break
                        elif user=="No" or user=="no":
                                userinput=input("You wanna quit(q) or continue(c)?")
                                if userinput=="q" or userinput=="Q":
                                        print("\n\t ADIOS AMIGOS")                                        
                                        a=2
                                        choice=2
                        else:
                                print("Wrong input")
                                goto(39) 
                        
else :
        print("\n\t ADIOS AMIGOS")
    
