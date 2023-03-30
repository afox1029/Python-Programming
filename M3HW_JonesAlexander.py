# Create an array based off of a set of numbers
# 3/30/2023
# CSC221 M3HW – Array Manipulations
# Alexander Jones
# 
# Display menu
# Ask user to enter choice
# Process choice
# Create array
# Square values
# Add 4
# Multiply by 6
# Exit program
#

import numpy as np

array = None

while True:
    print()
    print("MENU\n" + "_" * 33)
    print("1) Create a 3-by-3 Array")
    print("2) Display square Values for elements in array")
    print("3) Add 4 to every element and display result")
    print("4) Multiply elements by 6 and display result")
    print("5) Exit")
    
    
    print("Please input an integer.")
    choice = input("Enter your choice (1-5): ")
    
    
    if choice == "1":
        
        print("Enter values for 3-by-3 array:")
        values = []
        for i in range(3):
            row = []
            for j in range(3):
                value = input(f"Enter value for row {i+1}, column {j+1}: ")
                if "." in value:
                    value = float(value)
                else:
                    value = int(value)
                row.append(value)
            values.append(row)
        array = np.array(values)
        print("Array created:")
        print()
        for row in array:
            print(*row)
            
    elif choice == "2":
        if array is None:
            print("Array is empty. Please create an array first.")
        else:
            squared_array = array ** 2
            print("Squared values:")
            print()
            for row in squared_array:
                print(*row)
                
    elif choice == "3":
        if array is None:
            print("Array is empty. Please create an array first.")
        else:
            added_array = array + 4
            print("Added 4 to every element:")
            print()
            for row in added_array:
                print(*row)
                
    elif choice == "4":
        if array is None:
            print("Array is empty. Please create an array first.")
        else:
            multiplied_array = array * 6
            print("Multiplied every element by 6:")
            print()
            for row in multiplied_array:
                print(*row)
                
    elif choice == "5":
        
        break
        
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
