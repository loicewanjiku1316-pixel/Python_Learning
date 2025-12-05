# List
my_list = [10, 20, 30, 10]

print(my_list) # Ordered # Allow duplicates
print(my_list[1])  #Indexed
my_list[3] = 40
print(my_list)  # Mutable

# Tuple
# Ordered collection that can't be changed after creating it
my_tuple = (10, 30, 20, 10)

print(my_tuple) # Ordered # Allows duplicates
print(my_tuple[1]) # Indexed
my_tuple[3] = 40 # Immutable

print(sorted(my_tuple)) 
# output is a list therefore still immutable
# Use case: Protect your values

this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
print(len(this_tuple))

this_tuple = ("apple",)
print(type(this_tuple))

# Not a tuple
this_tuple = ("apple")
print(type(this_tuple))

# Can be of any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 2, 3, 4)
tuple3 = (True, False, False)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

# Different data types within a tuple
tuple1 = ('abc', 34, True)
print(tuple1)

# Using tuple() method to make a tuple:
this_tuple = tuple(("apple", "banana", "cherry"))
print(type(this_tuple))

# Access Tuple Items
this_tuple = ("apple", "banana", "cherry")
print(this_tuple[1])
print(this_tuple[-1])

# Range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

# Check if item exists
# To determine if a specified item is present in a tuple use the in keyword:
thistuple = ('apple', 'banana', 'cherry')
if 'apple' in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Update Tuples
# Change tuple values
x = ('apple', 'banana', 'cherry')
y = list(x) # Change to list so that tuple becomes mutable
y[1] = 'kiwi'
x = tuple(y) # Convert back to tuple
print(x)

colors = ('pink', 'blue', 'teal')
color_change = list(colors)
color_change[2] = 'green'
colors = tuple(color_change)
print(colors)

food = ('Ugali', 'Fish', 'Pilau')
food_change = list(food)
food_change[0] = 'Rice'
food = tuple(food_change)
print(food)

# Add items 
# Method 1: Convert into a list
current_tuple = ('blue', 'green', 'pink')
added_tuple = list(current_tuple)
added_tuple.append('orange')
current_tuple = tuple(added_tuple)
print(current_tuple)

my_tuple = ('Me', 'Myself', '&')
new_tuple = list(my_tuple)
new_tuple.append('I')
my_tuple = tuple(new_tuple)
print(my_tuple)

# Method 2: Add tuple to a tuple
thistuple = ('apple', 'banana', 'cherry')
addition = ('orange',)
thistuple += addition
print(thistuple)

x = (9, 2)
y = (2000, "Lucky Year")
x += y
print(x)
# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

# Remove Items
countries = ('Kenya', 'Uganda', 'Tanzania')
remove_country = list(countries)
remove_country.remove('Uganda')
countries = tuple(remove_country)
print(countries)

# Delete completely
# The del keyword can delete the tuple completely:
countries = ('Kenya', 'Uganda', 'Tanzania')
del countries
print(countries) # This will raise an error because the tuple no longer exists

# Unpack Tuples
fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Loop Tuples
fruits = ('apple', 'mango', 'orange')
for x in fruits:
    print(x)

# Using index numbers
fruits = ('apple', 'mango', 'orange')
for i in range(len(fruits)):
    print(fruits[i])

# Using a while loop
fruits = ('apple', 'mango', 'orange')
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

# Join Tuples
# Use '+' operator
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
fruits = ('apple', 'banana', 'cherry')
mytuple = fruits * 2
print(mytuple)

# Tuple Methods
# 1. count(): Returns the number of times a specified value occurs in a tuple
# 2. index(): Searches the tuple for a specified value and returns the position of where it was found
tuple1 = (1, 2, 1, 3, 5)
print(tuple1.count(1))
print(tuple1.index(1))


