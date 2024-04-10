# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/10/2024
# Description: The average of 5 numbers
num_numbers = 5
total = 0
print("Please enter five numbers.")
for i in range(num_numbers):
    number= float(input())
    total += number
average = total / num_numbers
print("The average of those numbers is: ")
print(average)
