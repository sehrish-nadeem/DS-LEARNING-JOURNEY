"""Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line"""

#Day 2: 30 Days of python programming
first_name = "sehrish"
last_name = "nadeem"
full_name = "sehrish nadeem"
country = "xxx"
city = "khi"
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = False
greeting, gr2, date, gr3 = "hi", "have a good day", 300926, "bye"

"""Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division"""
print(
  type(first_name),
  type(last_name),
  type(age),
  type(is_true))
print("first name length", len(first_name))
print(len(first_name) > len(last_name))
num_one, num_two = 5, 4
total = num_one + num_two 
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_div = num_one // num_two

"""The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords"""
rad = 30
area_of_circle = 3.14 * (rad ** 2)
circum_of_circle = 2 * 3.14 * rad
print(area_of_circle)
rad = float(input("enter radius:"))
area_of_circle = 3.14 * (rad ** 2)
circum_of_circle = 2 * 3.14 * rad
print(area_of_circle)
first_name = input("enter your first name:")
last_name = input("enter your last name:")
country = input("enter your country:")
age = int(input("enter your age:"))
help('keywords')