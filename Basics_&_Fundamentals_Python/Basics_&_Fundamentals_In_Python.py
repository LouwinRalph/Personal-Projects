#NOT FINISHED, I MIGHT ADD MORE DETAILS TO EACH NUMBER!!!!!!!

# 1️⃣ PRINTING #######################################################################################
# ➤ What: Displays output to the console.
# ➤ Why: Essential for debugging and user interaction.

print("Hello, World!")  # Basic greeting

# ➤ Printing multiple items
print("Name:", "Lou", "Age:", 19)  # Outputs multiple values separated by spaces

# ➤ Using variables
name = "Lou"
age = 25
print("User:", name, "| Age:", age)

# ➤ String concatenation
print("Welcome " + name + "!")  # Combines strings using +

# ➤ f-strings (Python 3.6+)
print(f"Hello {name}, you are {age} years old.")  # Cleaner and more readable

# ➤ Escape characters
print("Line1\nLine2")  # \n creates a new line
print("Tab\tSeparated")  # \t adds a tab space

# ➤ Printing special characters
print("She said, \"Python is awesome!\"")  # Escaping quotes
print("Backslash: \\")  # Prints a single backslash

# ➤ Custom separator and end
print("Python", "HTML", "PHP", sep=" | ")  # Custom separator
print("Loading", end="...")  # Keeps cursor on same line

# ➤ Printing lists and dictionaries
skills = ["Python", "HTML", "PHP"]
user_info = {"name": "Lou", "age": 25}
print("Skills:", skills)
print("User Info:", user_info)

# ➤ Debugging tip
print("DEBUG:", name, age, skills)  # Quick way to check variable states

print("2. Variables & Data Types ------------------------------------")
# 2️⃣ VARIABLES & DATA TYPES ############################################################################################
# ➤ What: Store data in memory using names.
# ➤ Why: Lets you reuse and manipulate values easily.
name = "Lou"         # String: text data
age = 25                # Integer: whole number
height = 1.1           # Float: decimal number
is_active = True        # Boolean: True or False
skills = ["Python", "HTML", "PHP", "JAVA"]  # List: collection of items

print("3. Conditional Statements ------------------------------------")
# 3️⃣ CONDITIONAL STATEMENTS
# ➤ What: Executes code based on conditions.
# ➤ Why: Adds logic and decision-making to programs.
if age > 18:
    print("Adult")  # Runs if age is greater than 18
elif age == 18:
    print("Just turned adult")  # Runs if age is exactly 18
else:
    print("Minor")  # Runs if age is less than 18

print("4. LOOPS ------------------------------------")
# 4️⃣ LOOPS
# ➤ What: Repeats code multiple times.
# ➤ Why: Useful for processing lists, automation, and repetition.

# For loop: iterates over items
for skill in skills:
    print("Skill:", skill)

# While loop: runs as long as condition is true
counter = 0
while counter < 3:
    print("Counter:", counter)
    counter += 1  # Increments counter

print("5. FUNCTIONS ------------------------------------")
# 5️⃣ FUNCTIONS
# ➤ What: Blocks of reusable code.
# ➤ Why: Makes code organized and avoids repetition.
def greet(user):
    return f"Hello, {user}!"  # Returns a personalized greeting

print(greet(name))  # Calls the function with 'name'

print("6. ARRAY LISTS ------------------------------------")
# 6️⃣ LISTS (Arrays)
# ➤ What: Ordered collection of items.
# ➤ Why: Stores multiple values in one variable.
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")       # Adds item to list
print(fruits[0])             # Accesses first item
print(len(fruits))           # Gets number of items

print("7. DICTIONARIES ------------------------------------")
# 7️⃣ DICTIONARIES
# ➤ What: Key-value pairs.
# ➤ Why: Great for storing structured data.
person = {
    "name": "Louwin",
    "age": 25,
    "location": "Mall"
}
print(person["location"])    # Accesses value by key

print("8. Looping with index ------------------------------------")
# 8️⃣ LOOPING WITH INDEX
# ➤ What: Combines loop with position tracking.
# ➤ Why: Useful when you need both item and its index.
for i in range(len(fruits)):
    print(f"Fruit {i}: {fruits[i]}")

print("9. EXCEPTION HANDLING ------------------------------------")
# 9️⃣ EXCEPTION HANDLING
# ➤ What: Catches and handles errors.
# ➤ Why: Prevents program from crashing unexpectedly.
try:
    result = 10 / 0  # This will cause an error
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Handles the error gracefully

print("10. Classes & Objects ------------------------------------")
# 🔟 CLASSES & OBJECTS
# ➤ What: Blueprint for creating objects (OOP).
# ➤ Why: Organizes code around real-world entities.
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} got grade {self.grade}")

s1 = Student("Louwin", "A")  # Creates a student object
s1.display()                 # Calls method to show info

print("11. Importing Modules ------------------------------------")
# 1️⃣1️⃣ IMPORTING MODULES
# ➤ What: Brings in external tools/functions.
# ➤ Why: Extends Python’s capabilities.
import math
print(math.sqrt(16))  # Uses math module to get square root

print("12. File Handling ------------------------------------")
# 1️⃣2️⃣ FILE HANDLING
# ➤ What: Reads and writes files.
# ➤ Why: Useful for saving data or reading input.
with open("sample.txt", "w") as file:
    file.write("This is a sample file.")  # Writes to file

print("13. List Comprehension ------------------------------------")
# 1️⃣3️⃣ LIST COMPREHENSION
# ➤ What: Short way to create lists.
# ➤ Why: Makes code cleaner and faster.
squares = [x**2 for x in range(5)]  # Creates list of squares
print(squares)

print("14. Enumerate ------------------------------------")
# 1️⃣4️⃣ ENUMERATE
# ➤ What: Adds index to loop items.
# ➤ Why: Cleaner than using range(len(...)).
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")













