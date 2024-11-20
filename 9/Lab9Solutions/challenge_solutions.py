# Advanced f-string Formatting

# 1. f-string Precision and Alignment
# Given the following variables:
name = "Alice"
age = 30
experience = 3
units = "months"
score = 47
total = 60

# Create an f-string that prints the information in the following format:
"""Alice is 30 years old and has 3 months of programming experience. 
She scored 78.3% in her Python exam."""

# Solution:
print(f'{name} is {age} years old and has {experience} {units} of programming experience. \nShe scored {score/total:.1%} in her Python exam.')


# 2. Mathematical Operations in f-strings
# Use f-strings to calculate and display the result of the expression:

x = 5
y = 3

# The output should be:
"5 times 3 is 15."

# Solution:
print(f'{x} times {y} is {x * y}.')


# 3. Conditional Expressions in f-strings
# Given the boolean variable:
is_student = True

# Create an f-string that prints:
"Welcome to the class!"
# If is_student is True, otherwise print:
"Welcome to the jungle!"

# Solution:
print(f'Welcome to the {"class" if is_student else "jungle"}!')


# File I/O with JSON

# 1. Writing and Reading JSON Files
# Create a list of Python dictionaries representing three people with the
# attributes: name, age, and city. 
# Write this dictionary to a JSON file named "person.json". 
# Then, read the contents of the JSON file and print them in alphabetical order.

# Solution:
import json

people = [{"name": "John", "age": 25, "city": "New York"},
          {"name": "Jean", "age": 32, "city": "Paris"},
          {"name": "Jane", "age": 27, "city": "London"}]

with open("person.json", "w") as json_file:
    json.dump(people, json_file)

with open("person.json", "r") as json_file:
    loaded_person = json.load(json_file)
    print(loaded_person)


# 2. JSON Data Manipulation
# Given a JSON file named "data.json" with the following structure:

{
  "students": [
    {"name": "John", "grades": [55, 63, 77]},
    {"name": "Alice", "grades": [92, 84, 89]},
    {"name": "Bob", "grades": [78, 80, 73]}
  ]
}

# Load the data from the file, add a new student named "Charlie" with grades of
# 64, 71, 75, print out each student with their average grade and then write
# the updated data back to the file.

# Solution:
import json

with open("data.json", "r") as json_file:
    data = json.load(json_file)

data["students"].append({"name": "Charlie", "grades": [64, 71, 75]})
for student in data["students"]:
    print(f'{student["name"]}: {sum(student["grades"]) / len(student["grades"]):.1f}')

with open("data.json", "w") as json_file:
    json.dump(data, json_file)


# Exercise Set: Logging

# 1. Basic Logging Setup
# Implement basic logging in Python. Create a script that logs messages of
# different levels (debug, info, warning, error, critical) to a file named
# "app.log."

# Solution:
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')


# 2. Custom Log Format
# Enhance the logging from Exercise 6 by customizing the log format to include
# the timestamp, log level, and the message itself.

Solution:
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')


# 3. Log File Rotation
# Extend the logging configuration to enable log file rotation. 
# Ensure that log files are rotated every day, keeping a backup of the last 
# 7 log files.

# Solution:
import logging
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler('app.log', when='midnight', interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)

logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')
