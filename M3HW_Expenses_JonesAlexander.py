#CSC121
#M3HW - Expenses
#Alexander Jones
#1/26/2023

account_amount = int(input("Enter starting amount in account $"))
print()
expense = int(input("Enter expense 1: "))

account_amount1 = account_amount - expense
user_input = input("Do you want to enter another expense?(y/n) ")
x = 1
print()

while user_input == "y":
    x += 1
    new_expense = int(input("Enter expense " + str(x) + ": "))
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
