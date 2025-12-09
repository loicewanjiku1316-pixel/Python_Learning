# Dictionaries are used to store data values in key:value pairs.
# Collection which is ordered, changeable and do not allow duplicates.
mydict = {'brand' : 'Ford',
          'model' : 'Mustang',
          'year' : 1964}
print(mydict)

# Dictionary Items
# Print the "brand" value of the dictionary:
mydict = {'brand' : 'Ford',
          'model' : 'Mustang',
          'year' : 1964}
print(mydict['brand'])

# Duplicates Not Allowed: cannot have two items with the same key
thisdict = {'brand' : 'Ford',
            'model' : 'Mustang',
            'year' : 1964,
            'year' : 2020
            }
print(thisdict)
# Duplicate values will overwrite existing values.

# Dictionary Length
thisdict = {'brand' : 'Ford',
            'model' : 'Mustang',
            'year' : 1964,
            }
print(len(thisdict))

# Dictionary Items - Data Types
mydict = {'brand' : 'Ford',
          'electric' : False,
          'year' : 1964,
          'colors' : ['red', 'white', 'blue']
          }
print(mydict)
print(type(mydict))

# The dict() Constructor
thisdict = dict(name = 'John', age = 36, country = 'Norway')
print(thisdict)

# Accessing Items
thisdict = {'brand' : 'Ford',
            'model' : 'Mustang',
            'year' : 1964
            }
x = thisdict['model']
print(x)

# get()
thisdict = {'brand' : 'Ford',
            'model' : 'Mustang',
            'year' : 1964
            }
x = thisdict.get('model')
print(x)

# Get Keys
thisdict = {'brand' : 'Ford',
            'model' : 'Mustang',
            'year' : 1964
            }
x = thisdict.keys()
print(x)

# Task: Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {'brand' : 'Ford',
       'model' : 'Mustang',
       'year' : 1964
       }
x = car.keys()
print(x) # Before the change

car['color'] = 'white'
print(x) # After the change

# Get values
car = {'brand' : 'Ford',
       'model' : 'Mustang',
       'year' : 1964
       }
x = car.values()
print(x)

# Changes
# Task: Make a change in the original dictionary, and see that the values list gets updated as well.
car = {'brand' : 'Ford',
       'model' : 'Mustang',
       'year' : 1964
       }
x = car.values()
print(x)

car['year'] = 2020
print(x)

# Add a new item to the original dictionary, and see that the values list gets updated as well.
car = {'brand' : 'Ford',
       'model' : 'Mustang',
       'year' : 1964
       }
x = car.values()
print(x)

car['color'] = 'red'
print(x)

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
car = {'brand' : 'Ford',
       'model' : 'Mustang',
       'year' : 1964
       }
x = car.items()
print(x)

# Task: Make a change in the original dictionary, and see that the items list gets updated as well.
car = {'brand' : 'Ford',
       'model' : 'Mustang',
       'year' : 1964
       }
x = car.items()
print(x)

car['year'] = 2020
print(x)

# Task: Add a new item to the original dictionary, and see that the items list gets updated as well
car = {'brand' : 'Ford',
       'model' : 'Mustang',
       'year' : 1964
       }
x = car.items()
print(x)

car['color'] = 'blue'
print(x)

# Check if Key Exists
# Use 'in' keyword
car = {'brand' : 'Ford',
       'model' : 'Mustang',
       'year' : 1964
       }
if 'model' in car:
    print("Yes, 'model' is one of the keys in the car dictionary")

# Change Values
# Task: Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict['year'] = 2018
print(thisdict)

# Update Dictionary
# Task: Update the "year" of the car by using the update() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({'year' : 2020})
print(thisdict)
# Note: The argument must be a dictionary, or an iterable object with key:value pairs.

# Add items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict['color'] = 'red'
print(thisdict)

# Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

# Removing items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop('model')
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# Removes the last inserted item

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict['model']
print(thisdict)
# Removes the item with the specified key name

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)
# Delete the dictionary completely

# The clear() method empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one
for x in thisdict:
    print(thisdict[x])

# Use the values() method to return values of a dictionary
for x in thisdict.values():
    print(x)

# Use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)

# Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
  print(x, y)

# Copy a Dictionary
# Task: Make a copy of a dictionary with the copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Use dict() function
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
# Dictionary within dictionary
# Task: Create a dictionary that contain three dictionaries
myfamily = {'child1' : {
            'name' : 'Benson',
            'year' : 1996
            },
            'child2' : {
              'name' : 'Loise',
              'year' : 2000
            },
            'child3' : {
              'name' : 'Sammy',
              'year' : 2004
            }
}
print(myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child1 = {'name' : 'Benson',
          'year' : 2000
}
child2 = {'name' : 'Loise',
          'year' : 2000
}
child3 = {'name' : 'Sammy',
          'year' : 2001
}

myfamily = {
    'child1' : child1,
    'child2' : child2,
    'child3' : child3
}
print(myfamily)

# Access Items in Nested Dictionaries
myfamily = {
    'child1' : {
        'name' : 'Benson',
        'year' : 1996
    },
    'child2' : {
        'name' : 'Loise',
        'year' : 2000
    },
    'child3' : {
        'name' : 'Sammy',
        'year' : 2001
    }
}
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
# Note: Be keen on the indentation of the for loop.

