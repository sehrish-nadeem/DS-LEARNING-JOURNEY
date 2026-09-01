"""You're splitting a bill of Rs. 4750 among 6 friends. Find how much each person owes, rounded to the nearest whole rupee using floor division, and find the leftover amount using modulus.
A recipe needs 2 ** 3 cups of flour for a triple batch. What does this evaluate to, and what operation is **?
You have a = 5 and b = 2. Without running it, predict the output of a / b vs a // b, and explain why they differ."""


# Basic Tasks
# Task no 1
total = 4750
share = 4750 // 6
remaining = 4750 % 6
print(f"each person owes Rs. {share}")
#correct syntax for using format
print("each person owes Rs. {}".format(share))
print(f"the leftover amount is {remaining}")

#Task no 2
# ** is exponetiation, it evaluates to 2^3 which is 8

#Task no 3
# 5 / 2 = 2.5 bcs it always returns a float even if it divides evenly
# 5//2 = 2 as it returns int if both values are int and rounds down to the nearest whole no.

"""Intermediate 4. You're tracking temperature and only have a value in Fahrenheit stored as a string, "98.6". Convert it to a float and then check if it's above normal body temp (98.6). 5. Swap the values of two variables score_a = 10 and score_b = 25 without using a third variable."""

#Intermediate tasks
#task no 4
normalTemp = "98.6"
bodyTemp = input("enter body temp: ")
print("is the given temp greater than the normal body temp?: ", float(temp) > bodyTemp)

   

# task no 5
a = 10
b = 25
a,b = b,a

"""Advanced 6. A store rounds all prices to the nearest 50 (e.g. Rs. 1280 becomes Rs. 1300). Write an expression using round() with a negative ndigits that does this."""

#advanced tasks
#task no 6
price = int(input("enter the price of your item: ")) #input by default is string u need to convert it into int or float first
newPrice = round(price / 50) * 50
# ok so like as yk round only rounds to 10, 100, 1000 so like we'' first divide by 50 to see how many 50s we can fit into the number for eg 1280/50 = 25.6 then round it off so it becomes 26 and multiplying it by 50 to get our final price
