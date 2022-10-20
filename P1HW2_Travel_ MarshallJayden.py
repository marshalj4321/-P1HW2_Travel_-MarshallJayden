# Calculating Travel Expenses
# September 22, 2022
# CTI-10 P1HW2 - Travel Expense
# Jayden Marshall
#
#                     Psuedocode
# Display "This program calculates and displays travel expenses"
# Display "Enter Budget:"
# Input Budget
# "Enter Your Travel Destination:"
# Input Travel Destination
# "How much do you think you will spend on gas?"
# Input Gas Money
# "Approximately how much will you need to for accomdation/hotel?"
# Input Accomodations Cost
# "Last, how much do you need for food?"
# Input Food Cost
# "------------Travel Expenses-----------"
print('This Program Calculates and Displays Travel Expenses')
print('')
budget = int(input("Enter Budget: "))
print('')
location = input("Enter Your Travel Destination: ")
print('')
fuel = input("How much do you think you will spend on Gas? ")
print('')
accomodation = int(input("Approximately how much will you need to for Accomdation/hotel? "))
print('')
food = int(input("Last, how much do you need for Food? "))
print('-----------Travel Expenses------------')
print('Location: ', location)
print('Initial Budget: ', float(budget))
print('')
print('Fuel: ', float(fuel))
print('Accomodation: ', float(accomodation))
print('Food: ', float(food))
x = 750
print('')
print('Remaining Balance: ', float(budget - x))
