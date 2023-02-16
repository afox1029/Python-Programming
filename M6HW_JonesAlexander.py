# program to print dates
# 2/16/2023
# CSC121 M6HW – Reading String
# Alexander Jones
#
#store months into a list
#create function for date calculations
#create function to display the menu
#display menu
#display calulations

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def date_calculation():
    print()
    input_date = input("Enter a date in the following format(mm/dd/yyyy): ")
    input_month = input_date[0:2]
    input_day = input_date[3:5]
    input_year = input_date[6:10]

    if input_month == '01':
        user_month = months[0]
    elif input_month == '02':
        user_month = months[1]
    elif input_month == '03':
        user_month = months[2]
    elif input_month == '04':
        user_month = months[3]
    elif input_month == '05':
        user_month = months[4]
    elif input_month == '06':
        user_month = months[5]
    elif input_month == '07':
        user_month = months[6]
    elif input_month == '08':
        user_month = months[7]
    elif input_month == '09':
        user_month = months[8]
    elif input_month == '10':
        user_month = months[9]
    elif input_month == '11':
        user_month = months[10]
    elif input_month == '12':
        user_month = months[11]
    print(user_month, input_day + ",", input_year)

def display_menu():
    print()
    print('----------Menu----------')
    print('1) Enter date')
    print('2) Exit')
    print('------------------------')
    
    
        
    
menu_choice = '1'

while menu_choice == '1':
    display_menu()
    user_input = input()
    if user_input == '1':
        date_calculation()
    elif user_input == '2':
        print()
        print('Bye!')
        menu_choice = '2'
    else:
        print()
        print("Invalid entry. Please try again.")
    
