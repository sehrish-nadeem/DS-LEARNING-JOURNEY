"""Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)"""

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

"""Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python"""

print("my name is sehrish")
print("my family name is xxx")
print("my country is xxx")
print("I am enjoying 30 days of python")

"""Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country"""
type(10)
type(9.8)
type(3.14)
type(4 - 4j)
type(['Asabeneh', 'Python', 'Finland'])
type("sehrish")
type("xxx")

"""Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
Find an Euclidean distance between (2, 3) and (10, 8)"""
i = 3
f = 4.5
c = 4 + 3j
s = "ccc"
b = True #python is case sensitive
l = [1,2,3,4,1]
t = ("ccc","ddd","eee") #tuples use ()
s = {1,2,3,4} # a set always use {}
d = {'firstname': 'sehrish', 'lastname': "nadeem", 'age': 19}
#dictionary uses {} and colons for key:value pair

#\(d=\sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}\)
print(((10-2)**2 + (8-3)**2)**0.5)