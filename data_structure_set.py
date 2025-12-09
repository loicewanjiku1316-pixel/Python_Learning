# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable, and unindexed.
# Note: Set items are unchangeable, but you can remove items and add new items.

thisset = {'apple', 'banana', 'cherry'}
print(thisset)
# Unordered, so you cannot be sure in which order the items will appear.
# Set items: Unordered, unchangeable, and do not allow duplicate values.

thisset = {'apple', 'banana', 'cherry', 'apple'}
print(thisset)
# Ignore dupicate values

thisset = {'apple', 'banana', 'cherry', True, 1, 2}
print(thisset)
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates

# Get the Length of a Set
thisset = {'apple', 'banana', 'cherry'}
print(len(thisset))

# Set Items - Data Types
set1 = {'apple', 'banana', 'cherry'}
set2 = {1, 2, 3, 4}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

set1 = {'Loise', 34, True}
print(set1)

myset = {'apple', 'banana', 'cherry'}
print(type(myset))

# The set() Constructor
myset = set(('apple', 'pie', 'sweet'))
print(myset)

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But can loop through using a for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Use 'in' keyword to check if item is present
thisset = {"apple", "banana", "cherry"}
print('banana' in thisset)
print('pie' in thisset)
print('banana' not in thisset)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.
# Add set items
thisset = {"apple", "banana", "cherry"}
thisset.add('orange')
print(thisset)

# Add sets
thisset = {"apple", "banana", "cherry"}
tropical = {'pineapple', 'mango', 'papaya'}
thisset.update(tropical)
print(thisset)

# Add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ['kiwi', 'orange']
thisset.update(mylist)
print(thisset)

# Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove('banana')
print(thisset)
thisset.remove('pie')
print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard('banana')
print(thisset)
thisset.discard('pie')
print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

myset = {'Loise', 'Sammy', 'Love'}
x = myset.pop()
print(x)
print(myset)
# Removes random item but since sets are unordered, not sure what gets removed.

# Empty set
myset = {'Me', 'Myself', 'I'}
myset.clear()
print(myset)

# Delete set
myset = {'Me', 'Myself', 'I'}
del myset
print(myset)

# Loop Sets
myset = {'pink', 'blue', 'teal'}
for x in myset:
    print(x)

# Join sets
# 1. Union: returns a new set with all items from both sets.
# Join set1 and set2 into a new set:
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# '|' operator
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Join Multiple Sets
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = {'Loise', 'Sammy'}
set4 = {'apple', 'banana', 'cherry'}
myset = set1.union(set2, set3, set4)
print(myset)

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = {'Loise', 'Sammy'}
set4 = {'apple', 'banana', 'cherry'}
myset = set1 | set2 | set3 | set4
print(myset)

# Join a Set and a Tuple
x = {'a', 'b', 'c'}
y = (1, 2, 3)
z = x.union(y)
print(z)
# Note: The '|' operator only allows you to join sets with sets, and not with other data types like you can with the union() method.

# 2. Update '|='
# Inserts all items from one set into another.
# Changes the original set, and does not return a new set.
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Note: Both union() and update() will exclude any duplicate items.

# 3. Intersection
# Keep ONLY the duplicates
# Will return a new set, that only contains the items that are present in both sets.
# Join set1 and set2, but keep only the duplicates:
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.intersection(set2)
print(set3)

# '&' Operator
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1 & set2
print(set3)
# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# The intersection_update() '&=' method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set1.intersection_update(set2)
print(set1)

# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {'apple', 1, 'banana', 0, 'cherry'}
set2 = {False, 'google', 1, 'apple', 2, True}
set3 = set1.intersection(set2)
print(set3)

set1 = {'apple', 1, 'banana', 0, 'cherry'}
set2 = {False, 'google', 'apple', 2, True}
set3 = set1.intersection(set2)
print(set3)

set1 = {'apple', 1, 'banana', 0, 'cherry'}
set2 = {False, 'google', 1, 'apple', 2, True}
set1.intersection_update(set2)
print(set1)

# 4. Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# Keep all items from set1 that are not in set2:
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.difference(set2)
print(set3)

# Use '-' operator
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1 - set2
print(set3)
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

# The difference_update() '-=' method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set1.difference_update(set2)
print(set1)

# 5. Symmetric Differences
# Will keep only the elements that are NOT present in both sets.
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.symmetric_difference(set2)
print(set3)

# Use '^' Operator
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1 ^ set2
print(set3)
# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

# The symmetric_difference_update() '^=' method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set1.symmetric_difference_update(set2)
print(set1)

# Frozenset
# An immutable version of a set.
# Unlike sets, elements cannot be added or removed from a frozenset.

# Creating a frozenset
# Create a frozenset and check its type:
x = frozenset({'apple', 'sauce', 'bacon'})
print(x)
print(type(x))

# Frozenset Methods
# 1. copy(): Returns a shallow copy
fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)

# 2. difference(): Returns a new frozenset with the difference
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b))
print(a - b)

# 3. intersection(): Returns a new frozenset with the intersection
a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)

# 4. isdisjoint(): Returns whether two frozensets have an intersection
# Returns True if no element is shared, otherwise False
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))

# 5. issubset()
# Returns True if this frozenset is a (proper) subset of another
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)

# 6. issuperset(): Returns True if this frozenset is a (proper) superset of another
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)

# 7. symmetric_difference(): Returns a new frozenset with the symmetric differences
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))
print(a ^ b)

# 8. union(): Returns a new frozenset containing the union
a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)
