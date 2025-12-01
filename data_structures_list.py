# Data structures
# List
# Ordered collection of items
# Changeable
# Allows duplicates

# Create List
empty = []
print(empty)
print(type(empty))

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
mixed = [1, 'a', True, None]
print(numbers)
print(type(mixed))

empty = list()
print(empty)

letters = list('Python')
print(letters)

numbers = list(range(5))
print(numbers)

# Nested list "Matrix"
matrix = [['a', 'b', 'c'], 
          ['d', 'e', 'f']]
print(matrix)
print(type(matrix))

mixed_matrix = [['a', 'b'],
                [1, 2, 3],
                [True]]
print(mixed_matrix)

# Access & Read
lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[0])
print(lst[-1])
print(lst[-2])

# Nested List (Matrix)
matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

print(matrix)
print(matrix[-1])
print(matrix[-1][-1])
print(matrix[0][0])
print(matrix[1][1])

# Slicing
lst = ['a', 'b', 'c', 'd']
print(lst[:2])
print(lst[2:])
print(lst[:])

matrix = [
     ['a', 'b', 'c'],  # Row 0
     ['d', 'e', 'f'],  # Row 1
     ['g', 'h', 'i']   # Row 2
 ]

print(matrix[:2])
print(matrix[1:])
print(matrix[2][:2])

# Unpacking
person = ['Maria', 29, 'Data Engineer', 'Spain']
name = person[0]
age = person[1]
role = person[2]
country = person[3]

name, age, role, country = person
print(country)

# Rest Collector
# Asterisk*
# Rule: Only one asterisk is allowed in unpacking
person = ['Maria', 29, 'Data Engineer', 'city', 'Spain']
*details, city, country = person
print(details)
print(city)
print(country)

# Rules
# 1. No. of variables must match the values exactly - not less, not more
numbers = 'Hi'
first, *rest = numbers
print(first)
print(rest)

# Skipping items Underscore "_"
person = ['Maria', 29, 'Data Engineer', 'Spain']
name, _, role, _ = person
print(name)
print(role)

person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *_, country = person
print(name)
print(country)

# Explore & Analyze
# Functions
numbers = [1, 5, 5, 2, 4, 3]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers)) # For integers only
print("Length:", len(numbers))

print("All:", all(numbers))
print("All:", all([1, 0, 2]))
print("All:", all(['a', '', 'b']))
print("All:", all(['a', 'c', 'b']))

print("Any:", all(numbers))
print("Any:", any([1, 0, 2]))
print("Any:", any(['a', '', 'b']))
print("Any:", any([0, 0, 0]))

# # Methods
print("Count:", numbers.count(5))  # Shows the number of times a value occurs
print("Index:", numbers.index(5))  # Returns the position of the first occurrence of a value / positive no.s only

# Operators
# IN: checks if a value exists in a sequence
numbers = [1, 5, 5, 4, 3]
print(4 in numbers)
print(8 in numbers)
print(8 not in numbers)  

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)

list1 = [5, 8, 3]
list2 = [5, 2, 3]
print(list1 < list2)

# Checks the memory address
list1 = [5, 8, 3]
list2 = [5, 8, 3]
print(list1 is list2)

# Change Your List
# 1. Add items
letters = ['a', 'b', 'c']
letters.append('x')
letters.append('y')

letters.insert(0, 'x')     # index of values change with each addition
letters.insert(3, 'y')
print(letters)

matrix = [
      ['a', 'b', 'c'],  # Row 0
      ['d', 'e', 'f'],  # Row 1
      ['g', 'h', 'i']   # Row 2
  ]
matrix.append(['x', 'y', 'z']) # ['x', 'y', 'z'] added as last list in matrix 
matrix.insert(0, ['a', 'a', 'a']) # ['a', 'a', 'a'] inserted as first list in matrix
matrix[1].append('x') # x added as the last value in row 1
matrix[0].insert(0, 'z')  # z inserted as the first value in first row
print(matrix)

# .append(value): Add item at the end
# .insert(Index,Value): Add item at specific position

# 2. Remove items
letters = ['a', 'b', 'c']
letters.clear()
print(letters)

letters = ['a', 'b', 'a']
letters.remove('a')   # Removes first match (value) and stops there
letters.remove('a')
print(letters)

letters = ['a', 'b', 'c']
letters.pop()      # Removes by position, if not specified default will be last item.
print(letters)         

letters = ['a', 'b', 'c']
removed = letters.pop()    # Retutns the value too
print('Removed Item:', removed)

letters = ['a', 'b', 'c']
removed = letters.pop(1) 
print(letters)   
print('Removed Item:', removed)

matrix = [
      ['a', 'b', 'c'],  # Row 0
      ['d', 'e', 'f'],  # Row 1
      ['g', 'h', 'i']   # Row 2
  ]
matrix.remove(['a', 'b', 'c'])
matrix.pop()
matrix[1].remove('e')
matrix[-1].pop(0)
matrix[0].pop()
print(matrix)

# Update
letters = ['a', 'b', 'c']
letters[0] = 'x'
letters[1] = 'y'
print(letters)

matrix = [
      ['a', 'b', 'c'],  # Row 0
      ['d', 'e', 'f'],  # Row 1
      ['g', 'h', 'i']   # Row 2
  ]
matrix[-1] = ['x', 'y', 'z']
matrix[0][0] = '-'
matrix[1][1] = '-'
matrix[-1][-1] = '-'
print(matrix)

# Order
letters = ['c', 'a', 'b']
letters.sort()   # lowest to highest
print(letters)

letters = ['c', 'a', 'b']
letters.sort(reverse = True)  # Highest to lowest
print(letters)

matrix = [
      ['d', 'e', 'f'],  # Row 0
      ['g', 'h', 'i'],  # Row 1
      ['a', 'b', 'c']   # Row 2
  ]
matrix.sort()  # Compares only the first item of each list
print(matrix)

matrix = [
      ['d', 'e', 'f'],  # Row 0
      ['a', 'z', 'i'],  # Row 1
      ['a', 'a', 'c']   # Row 2
  ]
matrix.sort()  
matrix[1].sort()
print(matrix)

# Sort the data without changing the list. Kinda like copying but now sorted.
letters = ['c', 'a', 'b']
new_list = sorted(letters)
new_list = sorted(letters, reverse = True)
print('Original List:', letters)
print('Sorted List:', new_list)

# Reversing List
# Flip list around
letters = ['c', 'a', 'b']
letters.reverse()
new_list = reversed(letters)   
print('Original List:', letters)
print('Reversed List:', new_list)
# Reversed() creates an iterator object, not a list

letters = ['c', 'a', 'b']
new_list = list(reversed(letters))   
print('Original List:', letters)
print('Reversed List:', new_list)

# Copying List
# Assignment = : This makes a reference only, not a copy

# Task: Create a copy of the list in a new variable
letters = ['a', 'b', 'c']
letters_copy = letters
letters.pop()
letters_copy.append('z')
print('Original:', letters)
print('Copy:', letters_copy)
# NB: Both variables reference the same list in memory

# Shallow copy
letters = ['a', 'b', 'c']
letters_copy = letters.copy()
letters.pop()
letters_copy.append('z')
print('Original:', letters)
print('Copy:', letters_copy)
# copy() creates a separate list in memory

# Deep copy
matrix = [
      ['a', 'b'],  # Row 0
      ['c', 'd'],  # Row 1  
  ]
matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copy:    ', matrix_copy)
# NB: The copy() method creates a shallow copy

import copy
matrix = [
      ['a', 'b'],  # Row 0
      ['c', 'd'],  # Row 1  
  ]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copy:    ', matrix_copy)
# NB: copy.deepcopy() creates a true, independent copy for all levels

import copy
matrix = [
      ['a', 'b'],  # Row 0
      ['c', 'd'],  # Row 1  
  ]
matrix_copy = copy.copy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copy:    ', matrix_copy)
# NB: copy.copy() creates a shallow copy just like the method copy()
# NB: copy.copy() is more general than list.copy(), not limited to lists

import copy

original = [
      ['a', 'b'],  # Row 0
      ['c', 'd'],  # Row 1  
  ]
# Use IS operator: It checks if 2 variables refer to the same object

# Assignment
copy1 = original
print("Same Object?", original is copy1, '\n')

# Shallow copy
copy2 = original.copy()
print("Same Object?", original is copy2)
print("Shared Lists?", original[0] is copy2[0], '\n')

# Deep copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Shared Lists?", original[0] is copy3[0], '\n')
# Tip: Use the IS operator to check if the copies are truly independent

# Recap
# Avoid assignment = (Risky + Confusing)
# Use .copy() for simple, flat lists
# Use copy.deepcopy for nested lists
# Always make extra copy for experiment and tests

# Combining Lists
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = letters + numbers # Order depends on the arrangement here
comb = [letters, numbers]
print(comb)
print(letters * 2)

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)
print(numbers)
# NB: extends() doesn't create a new list; it expands the original one

# Combining using zip()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers, "Hi"))
print(comb)

ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']
print(list(zip(ids, names)))

# Iterators & Iterables
# For looping
# To save memory
# For speed and flexibility

letters = ['a', 'b', 'c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)
# NB: We use iteration to transform data
letters = 124589
for l in letters:
    print(l)
# Integers are not iterable

# Enumerate reversed zip
letters = ['a', '', 'c']
for index, value in enumerate(letters):
    print(index, value)
# Enumerate use case: Find exact position of the bad data in your list

# Reversed: Returns an iterator that flips the data order
letters = ['a', 'b', 'c']
for l in reversed(letters):
    print(l)

# Zip: Combines two or more sequences into pairs(tuples)
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
print(list(zip(letters, numbers)))

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for l, n in zip(letters, numbers):
    print(l, n)

# Map
# Task: Make every letter uppercase
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))

numbers = ['1', '2', '3']
print(list(map(int, numbers)))

# Task: Clean up the list by removing all unwanted spaces
names = ['Maria ', 'John ', ' Kumar']
print(list(map(str.strip, names)))

names = ['Maria ', 'John ', ' Kumar']
for n in map(str.strip, names):
    print(n)
# NB: map is fast, clean way to do data transformations

# Filter
# Task: Clean up list by removing unvalid data
letters = ['a', 'b', None, 'c', False]
print(list(filter(None, letters))) # None removes all falsy values like 0, "", or False
print(list(filter(bool, letters)))   # Works the same, filters out all falsy values

# Task: Keep only letters(alphabetic) items
items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items)))
for i in filter(str.isalpha, items):
    print(i)
# filter() is perfect for cleaning up data in your structures

# Lambda functions
multiple = lambda x: x*2
# Variable(multiple): Stores a lambda function which doubles a number
print(multiple(2))

add = lambda x, y: x + y
print(add(1, 2))
# When a lambda has two parameters, you must pass two values when calling it

# A lambda can contain any expression, including conditions
# check = lambda i: i in "python"
# print(check('n'))
# print(check('z'))

# Lambda + Map
# Task: Prices are stored as messy strings and need cleaning to floats
prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))
# Go step-by-step
# 1. Data transformation (replace())
# 2. Put it in lambda
# 3. Map the function to iterator to manipulate my data

# Lambda + Filter
# Task: Remove all prices lower than 100
prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices)))
# 1. Filter logic (p >= 100)
# 2. In lambda
# 3. Filter to apply the function to filter all your data in list

# Task: Keep only students with scores higher than 70
students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]
# NB: Matrix iteration happens one row at a time
print(list((filter(lambda row: row[1] > 70, students))))

# Challenge
# Keep only students with names starting with "M"
students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]
print(list(filter(lambda row: row[0].startswith("M"), students)))
# print(students[0][0].startswith("M")): For testing my filter logic

# List comprehension
domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.DATAWITHBARAA.COM']

cleaned = [
    # Data Transformation
    d.lower().replace('www.', '')
    # For Loop
    for d in domains
    # Data Filtering
    if '.' in d
]
print(cleaned)
# NB: In comprehensions, filtering data is optional

# Get the bad data here in this scenario without the filtering
cleaned = [
    d.lower().replace('www.', '')
    for d in domains
]
print(cleaned)

# NB: Only Filtering: Using only the variable name means no transformation
# No manipulations
cleaned = [d for d in domains if '.' in d]
print(cleaned)

# Recap (list comprehension)
# 1. Data transformation e. g p * 2
# 2. Loop e.g p for prices
# 3. Filter e.g if p > 50

