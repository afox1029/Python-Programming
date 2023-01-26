# CSC121
# M2HW
# Alexander Jones
# 1/26/2023
#
# Input amount
# Display "Your change is"
# If statment for "no change"
# If statement to get and display quarter amount
# If statement to get and display dime amount
# If statement to get and display nickel amount
# If statement to get and display penny amount
# Else that displays total

import math

total = int(input("Enter the amount of change out of 100: "))
print("Your change is:")
if total >= 25:
    quarters = total // 25
    total = total % 25
    print(quarters, " quarters")
if total >= 10:
    dimes = total // 10
    total = total % 10
    print(dimes, " dimes")
if total >= 5:
    nickels = total // 5
    total = total % 5
    print(nickels, " nickels")
if total >= 1:
    pennies = total // 1
    print(pennies, " pennies")
