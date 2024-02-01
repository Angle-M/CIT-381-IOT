#CIT 381 - Spring 2024
# Authour: Angel Munoz
# Created: January 10,2024
# Simple number guessing game of a number 1 - 1000

#Basic setup of the program
import random
user_count = 0
answer = int(random.randint(1, 1000))

print("I'm thinking of a number between 1 and 1000. Guess what it is: ")
user_answer = int(input())

#Loop to check if the user's answer is correct, if not it will tell the user if the answer is too high or too low
while user_answer != answer:
    if user_answer > answer:
        print("Too high, try again.")
        user_count += 1
    elif user_answer < answer:
        print("Too low, try again.")
        user_count += 1
    user_answer = int(input())
    
#Checks if the user's answer is correct and if it is it will tell the user how many tries it took them to guess the number and gives a rating
if user_answer == answer: 
    print("Congratulations! You guessed the number in", user_count, "tries.")
    if user_count <= 7:
        print("Rating: Excellent")
    elif user_count > 7 and user_count <= 12:
        print("Rating: Good")
    elif user_count > 12 and user_count <= 20:
        print("Rating: Average")
    elif user_count > 20 and user_count <= 30:
        print("Rating: Needs Improvement")
    else:
        print("Rating: Were you even trying")


