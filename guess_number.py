import random 
import math

lower = int(input("Enter the Lower bound:"))
higher= int(input("Enter the Higher bound:"))
x = random.randint(lower, higher)
total_chances = math.ceil(math.log(higher - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")
count = 0
flag = False

while count < total_chances:
    count +=1

    guess = int(input("Guess a number:- "))

    if x == guess:
        print ("Congratulations you guessed the right number ", "%d" % x , "in" ,count, "try")
        flag = True
        break
    elif x > guess:
        print ("You guessed too small!")
    elif x < guess:
        print ("You guessed too high!" )

if not flag:
    print ("\n The number id %d" % x)
    print ("\t BETTER LUCK NEXT TIME!")       