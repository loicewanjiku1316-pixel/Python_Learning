print(" Hello, this is my first step towards making my dream come true! ")
print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)

print(3 < 1 or 5 < 1)
print(3 < 1 or 5 < 1)

# checks if the system is under pressure
cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)

# checking user credentials before login
email = True
password = False
print(email and password)

# NOT Operator
print(not 3 > 2)
print(not True)
print(not False)
print(not not False)
name = ""
print(not name)
print(not 0)

# Parentheses () First
# Task
# Allow access only if the user is logged in
# or they are guest 
# but they must not be banned.

is_logged_in = True
is_guest = False
is_banned = True
print((is_logged_in or is_guest) and not is_banned )

# Python Challenges

# Challenge 1
# Check if a user's name is not empty and the age is greater than or equal to 18.
user_name = "Loise Wanjiku" 
age = 25
print(user_name != "" and age >= 18)

# Challenge 2
# Check if the password is at least 8 characters long and does not contain spaces
password = "richgirll5"
print(len(password) >= 8 and " " not in password)

# Challenge 3
# Check if a user's email is not empty, contains '@', and ends with '.com'
email = "loicewanjiku@gmail.com"
print((email != "" and '@' in email) and email.endswith('.com'))

# Challenge 4
# Check if username is a string, is not None, and is longer than 5 characters.
user_name = "Loisewanjiku"
print((type(user_name) == str and user_name is not None) and len(user_name) > 5)
# NB: The parentheses is not necessary here because it will execute in the order you have written since it's only using AND.

# Challenge 5
# Check if the user is either an admin or a moderator, and either they're not banned or they've verified their email.
Admin = True
Moderator = False
is_banned = False
email = "loisewanjiku@gmail.com"
is_verified = True
print((Admin or Moderator) and (not is_banned or email is is_verified))

# NB: made a mistake on email is is_verified. 
# The mistake is that email is a string and is_verified is boolean, IS cannot used to compare string and boolean.
# Therefore OR should have been used, and no need for "email string" since email is a non-issue according to the question.
# Correct answer is:
Admin = True
Moderator = False
is_banned = False
is_verified = True
print((Admin or Moderator) and (not is_banned or is_verified))








