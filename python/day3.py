"""Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)."""
age = 19
my_height = 158.5
c = 1 + 4j
base = float(input('enter base:'))
height = float(input('enter height:'))
area = 0.5 * base * height
print("area of triangle is:", area)
side1 = float(input('enter side 1:'))
side2 = float(input('enter side 2:'))
side3 = float(input('enter side 3:'))
perimeter = side1 + side2 + side3
print("perimeter of triangle is:", perimeter)

"""Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement."""
length = int(input('enter length:'))
wid = int(input('enter width:'))
area = length * wid
print("are of rect:", area)
perimeter = 2 * (length + wid)
print("perimeter of rect", perimeter)
rad = float(input("enter radius:"))
area_of_circle = 3.14 * (rad ** 2)
circum_of_circle = 2 * 3.14 * rad
print("area of circle", area_of_circle)
print("circumference of circle", circum_of_circle)
print('slope', 2)
print('x intercept', 1)
print('y intercept', -2)
euclidean_dist = ((6-2)**2 + (10-2)**2)**0.5
print("euclidean dist:", euclidean_dist)
slope = (10 -2) / (6-2)
print('slope', slope)
print("is slope1 > slope2", 2 > slope)
x = int(input("ener a value that makes y = 0 in the eq: y = x^2 + 6x + 9: "))
y = x**2 + (6* x) + 9
print("is your ans correct", y == 0)
print("is dragon longer than jargon?", len("dragon") > len("jargon"))

"""Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10"""
print("on" in "python" and "on" in "dragon")
print("is jargon in the sentence: I hope this course is not full of jargon?", "jargon" in "I hope this course is not full of jargon")
length = len("python")
print(float(length))
print((str(length))) #the func is str() not string()
num = int(input("enter a num: "))
print("this is an even number", num % 2 == 0)
print(7//3 == int(2.7))
print(type('10') == type(10))
print(int(float('9.8')) == 10)
#you cant directly change a float str to an int first convert the str to a float then to an int
"""Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years"""
hours = int(input("enter hours worked: "))
rate = int(input("enter rate per hr:"))
pay = hours * rate
print("Your weekly earning is: ", pay)
years = int(input("Enter number of years you have lived:"))
lived = years * 365 * 24 * 3600
print("ypou have lived for", lived, "secs")
"""Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125"""
#im doing this qs using loops rn, this course teaches loops on day 10
for n in range(6): #loops start from index 0 to n-1
  print(n, end= " "),
  print(n ** 0, end= " "), #print can take in parameters with what to end the statement with in this case im ending eachno with a space
  print(n ** 1, end= " "),
  print(n ** 2, end= " "),
  print(n ** 3)


