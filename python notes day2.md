# Python — Day 2: Lists

## Quick Note (Booleans, carried over)
- Only two ways XOR can be true — when both variables have opposite values.

## Lists
- Lists represent an ordered sequence of values.
```python
primes = [2, 3, 5, 7]
```
- We can even make a list of lists:
```python
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K']
]
```
- A list can contain a mix of different types of variables.
- Indexing can be performed on lists.

### Types of Indexing
- **Explicit:** we use this when we know the number of elements a list/array contains.
- **Negative:** a special feature in Python which tells the computer to start counting backward from the very end. Doesn't matter how long or short the list is.
```python
# Accessing last element → index = -1
# 2nd last → index = -2
# and so on
```

## `list.index()`
We can get the index of any particular element using this function.
```python
listName.index(element)
```

## The `in` Operator
Used primarily inside `if` statements.
```python
if "Earth" in planets:
    ...
if "Pluto" not in planets:  # checking for absence
    ...
```
Returns bool values.

## Tuples
### Difference between tuples & lists
- Tuples use parentheses `()` instead of square brackets.
- They are immutable (can't be modified).
- They're often used for functions that return multiple values.

### Python uses tuples to make variable swap happen
```python
a = 1
b = 0
a, b = b, a
print(a, b)
# Output = 0 1
```
This is known as **tuple unpacking**. Because these are commas, Python automatically groups these values into a single temporary tuple in memory — creates tuple `(0, 1)`.

**Note:** the tuple `(0, 1)` itself never changes, only its labels change.

**Unpacking (left side):** Python then takes the temporary tuple & matches the items up with the variables on the left side `(a, b)`, assigning `(0, 1)` to them.

In other languages you can't do this directly — it results in overwriting of data. There you have to use a temporary variable.

### Difference between Arrays & Lists
| Feature | Lists | Arrays |
|---|---|---|
| Size | dynamic | fixed |
| Data type | heterogenous (mixed dt) | homogenous (same dt) |
| Memory | runtime memory → heap; linked or dynamic block ptr array | compile time memory → stack; contiguous (stored in a single block) |
| Performance | slightly slow due to the flexibility functions they contain | high speed bcs of direct memory access |

---

## Slicing
We can basically access specific elements from the lists using slicing.
```python
planets[0:3]  # gives us elements starting from index 0 upto 3
```
- If there's no start index specified, it's said to be 0.
- If no end index specified, it's by default the length of the index.

**Trick to know exactly how many items a slice will return:**
`Stop Index - Start Index`

But in case of the slice `1:-1` you'll have to replace `-1` with its positive index first.

**Note:** In Python, the slice notation `[start:stop]` always includes the start index but excludes the stop index.

In the case where you don't know the number of lists inside a list, you can access the last list using:
```python
team[-1]
```

---

## Changing Lists
Lists are mutable, i.e. they can be modified in place. One way to modify them is to assign to an index or slice expression.

### List Functions
- `len()`: gives the length of a list
- `sorted()`: return a sorted version of a list
- `sum()`
- `max()`
- `min()`

You can use `.imag` to find out the imaginary part of a number.
```python
x = 12
c = 12 + 3j
# x.imag = 0
# c.imag = 3.0
```

An object contains attributes (variables) & methods (functions). These can be accessed using dot syntax.

### List Methods
- `.append`: modifies a list by adding an item to the end
- `.pop`: removes & returns the last element of a list

These are not standalone functions like `max` & `min` — these only exist within lists.

---

## Loops & List Comprehensions
Loops are a way to repeatedly execute some code.

### For loop syntax
```python
for variable in list/type:
    print(variable, end=' ')
    # prints everything on the same line bcs
    # by default end = '\n'
```
`in` links the variable and the list together. The object to the right of `in` can basically be anything that supports iteration.

You can even loop through each char in a string.
```python
s = "Hello world"
for char in s:
    print(char)
```

### `range()`
Returns a sequence of numbers.
```python
for i in range(5):
    print("hi")
# hi will be printed 5 times
```

### While loops
Iterate until a condition is met.
```python
while (condition):
    # code to be executed
```
The argument of the while loop is evaluated as a boolean statement & the loop is executed till the statement evaluates to False.

### List Comprehension
This is basically a way to minimize the lines of code. It's better to not use it too much so that others can understand the code easily.
```python
squares = [n**2 for n in range(10)]
# basically appends squares from 0-9 in the list
```
```python
shortPI = [planet for planet in planets if len(planet) < 6]
# adds short planets to the list
```

### `any()`
Evaluates a collection (list, tuple) & returns True if at least one of the elements is True.

- Python creates lists by default. It does not make an array unless we use a function from an external library.

---

## Comparing List Elements
We can't compare a single element with an entire list unless we use a library in Python.
```python
[1, 2, 3, 4] > 2  # not possible
```

### Implementing a function that solves this problem
```python
def elementWiseGreaterThan(L, thresh):
    result = []  # creating an empty list to store answers
    for i in range(len(L)):
        if L[i] > thresh:
            result.append(True)  # append is necessary here bcs you can't
        else:                    # just assign values to an empty array —
            result.append(False) # you can only overwrite them
    return result
```

### Using List Comprehension
```python
def elementWiseGreaterThan(L, thresh):
    return [num > thresh for num in L]
# this method basically creates a list as we keep on comparing each element.
# the sq brackets tell Python automatically to make a list.
```

- Instead of using the `if` condition, you could've also done:
```python
for num in L:
    result.append(num > thresh)
```

### Implementing a function to check if a menu is boring
```python
def boringMenu(meals):
    for i in range(len(meals) - 1):
        # looping up to the 2nd last element without crashing
        if meals[i] == meals[i+1]:
            return True
    return False
```

---

## Slot Machine Example
Returning the slot machine n times & returning the avg net profit per run.
```python
def estimate(n_runs):
    total = 0  # always initialize local variable outside loop
    for i in range(n_runs):
        total += playSlotMachine()
    total_profit = total - 1
    avg = total_profit / n_runs
    return avg
```

### List Comprehension Version
```python
def estimate(n_runs):
    total = sum(playSlotMachine() for i in range(n_runs))
    return (total - n_runs) / n_runs
```
