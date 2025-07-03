# Adama Junior Sembene
# 07/03/2025
# P2HW2 – Grades Summary
# This program ask the user to enter grades for six modules, stores them in a list,
# then displays the lowest grade, highest grade, average and totla.

# Pseudocode:
# Prompt user separately for grades for each of the six modules
# Convert each input to float and store in a list called grades
# Use min() to find the lowest grade
# Use max() to find the highest grade
# Use sum() to calculate the total of all grades
# Divide the total by the number of grades to get the average
# Print a formatted results section with required spacing and average to 2 decimal places

# Prompting the user for grades and storing them in a list
grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Processing data
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Display results with required formatting
print("--------------------------------------------")
print(f"Lowest Grade:      {lowest}")
print(f"Highest Grade:     {highest}")
print(f"Sum of Grades:     {total}")
print(f"Average:           {average:.2f}")
print("--------------------------------------------")


