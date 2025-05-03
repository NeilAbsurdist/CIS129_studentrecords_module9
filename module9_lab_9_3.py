# Neil Pritchett
# CIS129 - Module 9 Lab
# 9.3: Write student records to a CSV file using the csv module

import csv

# Open the CSV file in append mode (so we don't overwrite existing data)
with open('grades.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    # Ask for student info
    first = input("Enter student's first name: ")
    last = input("Enter student's last name: ")
    exam1 = int(input("Enter grade for exam 1: "))
    exam2 = int(input("Enter grade for exam 2: "))
    exam3 = int(input("Enter grade for exam 3: "))

    # Write the row to the CSV file
    writer.writerow([first, last, exam1, exam2, exam3])

print("Student record written to grades.csv")