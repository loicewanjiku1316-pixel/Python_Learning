# Loop
# Control flow of code
# Repeat a block of code over and over until a condition is met

# For Loops
# Go through a group of items one by one to do something for each item

print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")

for i in (1, 2, 3, 4, 5):
    print("Round: 1")

items = (1, 2, 3, 4, 5)
for item in items:
    print(f"Round: {item}")

# Sequences you can loop
items = [1, 2, 3, 4, "Hi"]
for item in items:
    print(f"Round: {item}")

items = " Python"
for item in items:
    print(f"Round: {item}")

for item in range(1, 6):
    print(f"Round: {item}")

for item in range(1, 10, 2):
    print(f"Round: {item}")

for item in range(1, 10, 4):
    print(f"Round: {item}")

for item in range(2, 10, 2):
    print(f"Round: {item}")

# Real world applications
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current Total:" , total)
print("Final Total:", total)

files = [' Report.csv', 'DATA.csv ', ' final.TXT']
# Inconsistent casing & unnecessary spaces
for file in files:
    file = file.strip().lower().replace('.txt', '.csv') # Clean first, transform second - always in that order
    print(f"Processing {file}")

# Challenge 1
# Print 7-times table from 1 to 10 using a for loop
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

# Challenge 2
# Print a left-aligned pyramid of stars with 6 rows using a for loop
for item in range(1, 7):
   print("*" * item) 

# Break statement
#  Stops the loop immediately
names = ['john', 'maria', '', 'kumar']
for name in names:
    print(f'Name = {name}')

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print('Empty value detected!')
        break
    print(f'Name = {name}')

# Continue Statement
# Skips one loop cycle without stopping the loop
names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print('Empty value detected!')
        continue
    print(f'Name = {name}')

# Pass statement
# Placeholder where nothing happens
names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        pass #todo: Handle empty value
    print(f'Name = {name}')
    
names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        name = name.replace('', 'unknown')
    print(f'Name = {name}')

# Break vs Continue Real-World Applications
# Task 1: Loop through a list of days and print only the working days, skipping the weekends
days = ['Mon', 'Sun', 'Wed', 'Tue']
weekends = ['Sat', 'Sun']
for day in days:
    if day in weekends:
        continue
    print(f'Workday: {day}')
# NB: Use the same word e.g day
# Variable - singular
# Sequence - plural
# Avoid hardcoding values inside for or if 
# Instead, define them as variables

# Task 2: Scan emails to block unsafe data from entering your system
emails = [
    'data@gmail.com',
    'loise@outlook.de',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack')
        break
    print(f'Processing Email: {email}')

#  Else statement inside loops!
#  Runs a block of code only if the loop finishes naturally
# Loop completed without breaks
items = [1, 3, 4, 7]
for i in items:
    print(i)
else:
    print("Loop is completed")
# Useless here since everything can be executed regardless of the else
# So, use else with loops only when there's a break

# Else + Break
# Check for even number
items = [1, 3, 4, 7]
for i in items:
    if i % 2 == 0:
        print("Even Number Found:", i)
        break
else:
    print("All numbers are odd")
# else will run only if the loop is not interrupted
items = [1, 3, 5, 7]
for i in items:
    if i % 2 == 0:
        print("Even Number Found:", i)
        break
else:
    print("All numbers are odd")

# Else in loops: Real-world applications
names = ['Kamara', 'Tuba', None, 'Monika']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")

names = ['Kamara', 'Tuba', 'Maria', 'Monika']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")

# Task 1: Check if all files are csv files
files = ['data1.csv',
         'report.pdf',
         'report2.csv']

for file in files:
    if not file.endswith('.csv'):
        print(f'{file} is not a CSV')
        break
else:
    print("All files are CSV")

files = ['data1.csv',
         'report.pdf',
         'data2.txt',
         'report2.csv']

for file in files:
    if not file.endswith('.csv'):
        print(f'{file} is not a CSV')
        continue
else:
    print("All files are CSV")
# Executes everything which is not correct
# Makes no sense to use else + continue

files = ['data1.csv',
         'report.pdf',
         'data2.txt',
         'report2.csv']

for file in files:
    if not file.endswith('.csv'):
        print(f'Not all files are CSV')
        break
else:
    print("All files are CSV")

# Challenge
# Check whether any filename appears more than once
#  Print "Duplicate found" if a duplicate exists,
# otherwise print "All files are unique"
file_lists = ['report.pptx',
             'data.xlsx',
             'summary.docx',
             'report.csv',
             'data.csv'
             ]
for file_list in file_lists:
    if file_lists.count(file_list) > 1:
        print("Duplicate found")
        break
else:
    print("All files are unique")

# Nested for loop
# Loop inside another loop
for x in range(3): # outer loop
    for y in range(2):
         for z in range(2):
              
            print(f"({x}, {y}, {z})")

# Real world applications
# For pairing data to see all possible combinations
colors = ['red', 'blue', 'green']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')
# # Used to go through layers or drilling into hierarchy
years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 29)

for y in years:
    for m in months:
        for d in days:
            print(f'report_{y}_{m}_{d}.csv')
# Navigate through tables and columns
# Task: Select count(*) FROM customers wher id is NULL
tables = ['customers', 'orders', 'prices']
columns = ['id', 'create_date']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')

# While Loop
# Repeats a block of code - over and over as long as condition is True
# While Condition
# Task 1: Build a counter that's going to count from 1 to 5
count = 1  # initialization
while count <= 5:  # condition
    print(count)
    count += 2  # update

# Task 2: Write a program that keeps asking "Do you agree?" until the user types "yes"
answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no): ")
print("Thank You")

# While True
while True:
   answer = input("Do you agree?(yes/no): ")
   if answer == "yes":
      break
print("Thank you")  

# Challenge 1: Extend current loop with the following requirements:
# 1. Allow up to 3 attempts
# 2. If the user types "yes" within 3 attempts, print "Glad we are on the same page"
#3. If user didn't give "yes" within 3 attempts, print "3 Strikes, You are Out!"
# Current loop in question:
# while True:
#     answer = input("Do you agree? (yes/no):")
#     if answer == "yes":
#         break
# print("Thank you")
# Answer:
attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts += 1
else:
    print("3 strikes. You're out")

# While Condition               vs             While True
# Exists normally - condition = False       Must have extra if + break
# safer + more readable                     Risk of infinite loop + more flexible
# building counter, limited tries,          open-ended: waiting for Database, Stream, API
# validating the output from user                                



