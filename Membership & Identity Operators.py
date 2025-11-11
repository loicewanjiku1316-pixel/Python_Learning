# Mebership (in) Operator
# Checks if a value is inside another value.
# Like string, list, tuple, or other sequence.
print("o" in "python")
print("f" in "python")
print("f" not in "python")
print(3 not in [1, 2, 3])

# Task
# Validate that the domain is not on the banned list
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)

domain = "spam.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)

# Identity Operators
# Checks if 2 variables refer to the same object in memory
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)
print(x is y)

# x = 10
# y = 10

print(x == y)
print(x is y)

# = Between 2 variables: Assigns one variable to the same object that another variable is referring to
x = ['a', 'b', 'c']
y = x

print(x == y)
print(x is y)

# Task
# Validate the email address
# It must be filled in and not empty
email = "l@gmail.com" 
print(email != "")

# "" - means an EMPTY but it is KNOWN, it is string 
email = "" 
print(email != "")

# None - means NO VALUE at all, it is UNKNOWN
email = None
print(email != None and email != "")

email = None
print(email is not None and email != "")

# Conditional Statements
# Standalone If
# Defines first condition
# True? Do nothing
# False? Skip it

score = 100
if score >= 90:
    print("A")

score = 50
if score >= 90:
    print("A")

# Two-way Decision (if-else)
# Runs only if all previous conditions are false
score = 50
if score >= 90:
    print("A")
else:
    print("F")

score = 95
if score >= 90:
    print("A")
else:
    print("F")

# Multiple Conditions
# if-elif-else
score = 100
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

score = 50
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

# Branching
# if-elif-elif-else
score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

score = 65
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Nested if-else
# Nested if
# if statement inside another if.
# if the first is true then check the second.

score = 95
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

score = 95
submitted_project = False
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

score = 50
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

score = 50
submitted_project = False
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Connecting conditions
# Logical operators
score = 100
submitted_project = False
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

score = 50
submitted_project = True
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")

score = 50
submitted_project = False
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")

# Independent ifs
# Each if is checked separately
# All conditions are tested even if one is already true
score = 50
submitted_project = False

if score >= 90:
    print("High Score")
else:
    print("Low Score") 

if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")

# Challenge
# Validate the quality and correctness of email values
# 1. Must not be empty
# 2. Must contain '.' and '@'
# 3. Must contain exactly one '@' symbol
# 4. Must end with '.com', '.org', '.net'
# 5. Must not be longer than 254 characters
# 6. Must start and end with a letter or digit
# My attempt
email = "1trynaberich@gmail.com"
if email != "":
    print("Not empty")
else:
    print("Empty")

if '.' in email and '@' in email:
    print(". and @ present")
else:
    print(". and @ not present")

if email.count('@') == 1:
    print("Only one @")
else:
    print("Multiple @")

if email.endswith(".com") or email.endswith(".org") or (".net"):
    print("Correct ending")
else:
    print("Incorrect ending")

if len(email) <= 254:
    print("Correct length")
else:
    print("Incorrect length")

if len(email) > 0:
    if (email[0] >= "A" and email[0] <= "Z") or (email[0] >= "a" and email[0] <= "z") or (email[0] >= "0" and email[0] <= "9"):
        if (email[-1] >= "A" and email[-1] <= "Z") or (email[-1] >= "a" and email[-1] <= "z") or (email[-1] >= "0" and email[-1] <= "9"):
            print("Starts and ends with a letter or digit")
        else:
            print("Does not start and end with a letter or digit")

# Tutor's answer
email = "loice@gmail.com"
valid = True
# # # Clean the string
email = email.strip()
# # # Must not be empty
if email == "":
    print("Email cannot be empty.")
    valid = False
# # Must contain '.' and '@'
if not('.' in email and '@' in email):
    print("Email must contain . and @")
    valid = False
# # Must contain exactly one '@' symbol
if email.count('@') != 1:
    print("Email must contain exactly one @.")
    valid = False
# Must end with '.com', '.org', '.net'
# Alternative 1:
# elif email.endswith('.com') or email.endswith('.org') or email.endswith('.net'):
# Alternative 2:
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com, .org, or .net")
    valid = False
# Must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters")
    valid = False
# Must start and end with a letter or digit
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    valid = False
if valid:
    print("Email is valid")

# Challenge 2
# Validate the quality and correctness of passwords
# 1. Must not be empty
# 2. Must be at least 8 characters
# 3. Must include at least 1 uppercase
# 4. Must include at least 1 lowercase
# 5. Must not be same as the email
# 6. Must not contain any spaces
# 7. Must start and end with a letter or digit

password = "1HinkuyWi"
email = "isolde13@gmail.com"
valid = True
# Must not be empty
if password == "":
    print("Password must not be empty")
    valid = False
# Must be at least 8 characters
if len(password) < 8:
    print("Password must be at least 8 characters") 
    valid = False
# Must include at least 1 uppercase
if password == password.lower(): 
    print("Password must include at least 1 uppercase")
    valid = False
# Must include at least 1 lowercase
if password == password.upper():
    print("Password must include at least 1 lowercase")
    valid = False
# Must not be same as the email
if password == email:
    print("Password must not be same as the email")
    valid = False
# Must not contain any spaces
if " " in password:
    print("Password must not contain any spaces")
    valid = False
# Must start and end with a letter or digit
if not(password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")
    valid = False
if valid:
    print("Password is valid")


