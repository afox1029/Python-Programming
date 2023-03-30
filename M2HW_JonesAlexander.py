# Program that quizzes user on countrys capitals
# 3/28/2023
# CSC221 M2HW – Country Capitals
# Alexander Jones
#Create a holder for the capitals and countries
#loop a question asking a random capital
#Count all of the answers
#Exit the program when told to quit

import random

capitals = {
    "Argentina": "Buenos Aires",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "China": "Beijing",
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Mexico": "Mexico City",
    "Nigeria": "Abuja",
    "Russia": "Moscow",
    "South Africa": "Pretoria (administrative); Cape Town (legislative); Bloemfontein (judiciary)",
    "Spain": "Madrid",
    "Switzerland": "Bern",
    "Thailand": "Bangkok",
    "Turkey": "Ankara",
    "United Kingdom": "London",
    "United States": "Washington, D.C."
}

correct = 0
incorrect = 0

while True:
    country = random.choice(list(capitals.keys()))
    capital = capitals[country]
    answer = input("What is the capital of " + country + "? ")
    if answer == "quit":
        break
    elif answer == capital:
        print("Correct!")
        correct += 1
    else:
        print("Incorrect. The capital of " + country + " is " + capital + ".")
        incorrect += 1

print("You got", correct, "correct and", incorrect, "incorrect.")
