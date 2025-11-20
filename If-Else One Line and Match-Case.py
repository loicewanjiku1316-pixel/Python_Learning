# if-else one line
# Used for simple logic only
# Rules
# 1. Else must be included
# 2. Can't use elif

score = 100
if score >= 90:
    print("A")
else:
    print("F")

# Rewrite in if-else one line
print("A" if score >= 90 else "F")
grade = "A" if score >= 90 else "F"
print(grade)

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

# Rewrite in if-else one line
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
grade = ("A" if score >= 90 
         else "B" if score >= 80 
         else "F")
print(grade)

# Match Case
# Evaluate a value against multiple values
# Runs the code of the first match
# Task: Convert the full country names into 2-letter abbreviations

# For flexible logic and multiple conditions
country = "United States"
if country == "United States":
    print("US")
elif country == "India":
    print("IN")                   
elif country == "Kenya":
    print("KE")
elif country == "Egypt":
    print("EG")
else:
    print("Unknown Country")

# Can be used only for matching values
country = "USA"
match country:
    case "United States" | "USA":
        print("US")
    case "India":
        print("IN")
    case "Kenya":
        print("KE")
    case "Egypt":
        print("EG")
    case _: 
        print("Unknown Country")





