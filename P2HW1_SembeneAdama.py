# Adama Junior Sembene
# July 3, 2025
# P2HW1 – Travel Budget Calculator (modified Output)
# This program asks the user for a trip budget, destination, and expenses.
# It calculates total expenses and remaining balance and displays everything nicely formatted.

# Get user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate total expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results with aligned formatting
print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accomodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining_balance:.2f}")
