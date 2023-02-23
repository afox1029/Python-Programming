# CSC121
# M7HW - Expenses
# Alexander Jones
# 2/23/23

account_amount = int(input("Enter starting amount in account $"))
print()
expense = input("Enter expense 1: ")
try:
    int(expense)
except ValueError:
    print("Please enter a number.")
    print()
    expense = int(input("Enter expense 1: "))
expense = int(expense)  
account_amount1 = account_amount - expense
user_input = input("Do you want to enter another expense?(y/n) ")
x = 1
print()

while user_input == "y":
    x += 1
    new_expense = input("Enter expense " + str(x) + ": ")
    try:
        int(new_expense)
    except ValueError:
        print("Please enter a number.")
        print()
        new_expense = int(input("Enter expense " + str(x) + ": "))
    new_expense = int(new_expense)    
    expense = expense + new_expense
    user_input = input("Do you want to enter another expense?(y/n) ")
    print()
    if user_input =="n":
        break
print()
print(f'Amount in account before expenses subtracted ${account_amount:.1f}')
print("Number of expenses entered: ", x)
final_amount = account_amount - expense
print(f'Amount in account After expenses subtracted is $ {final_amount:.1f}')
