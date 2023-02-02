# The prpgram gives quick math quizzes and displays random numbers
# 2/2/2023
# CSC121 M4HW - Math Quiz
# Alexander Jones
#
import random

print("Welcome to Math Quiz")
print()
print()
print()
print()

def display_menu():
    print("MAIN MENU")
    print()
    print("----------------")
    print("1) Add Random Numbers")
    print("2) Subtract Random Numbers")
    print("3) Exit")
    print()
    
def input_1():
    x = 1
    try_again = "y"
    while try_again == "y":
        r1 = random.randint(10, 100)
        r2 = random.randint(10, 100)
        total = r1 + r2
        print(" ", r1)
        print("+", r2)
        choice_1 = int(input("Enter answer. "))
        while choice_1 != total:
            if choice_1 > total:
                print("Sorry, guess is too high.")
                choice_1 = int(input("Try again: "))
                x += 1
            else:
                print("Sorry, guess is too high.")
                choice_1 = int(input("Try again: "))
                x += 1
                
        print()
        print("Congratulations!!!! Your answer is correct.")
        print("Number of guesses: ", str(x))
        try_again = "n"

def input_2():
    x = 1
    try_again = "y"
    while try_again == "y":
        r1 = random.randint(10, 100)
        r2 = random.randint(10, 100)
        total = r1 - r2
        print(" ", r1)
        print("-", r2)
        choice_1 = int(input("Enter answer. "))
        while choice_1 != total:
            if choice_1 > total:
                print("Sorry, guess is too high.")
                choice_1 = int(input("Try again: "))
                x += 1
            else:
                print("Sorry, guess is too high.")
                choice_1 = int(input("Try again: "))
                x += 1
                
        print()
        print("Congratulations!!!! Your answer is correct.")
        print("Number of guesses: ", str(x))
        print()
        try_again = "n"

again = "y"

while again == "y":
    display_menu()
    user_input = input("Please choose one of the menu options: ")
    if user_input == "1":
        input_1()
    elif user_input == "2":
        input_2()
    elif user_input =="3":
        break
    else:
        print("That is not a menu option.")
        print()
        
        
