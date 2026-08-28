# Python — Day 1

## Variable Assignment
- No need for declaration of variables in Python.
- We can even reassign a variable to a completely different data type.

## Function Calls
- We call functions by putting `()` after their name & passing the inputs/arguments inside the `()`.

## Comments
- Use `#` symbol.

## Conditionals
- Syntax → `if (condition):`
- The `:` indicates that a new code block is starting.
- Subsequent lines are indented as part of that block. Lines which are *not* indented are not part of the same code block.

## Strings
- Can be marked by single or double quotes.
- But if a string includes a single-quote inside it, it might confuse the parser.

## Operator Overloading
- Python includes built-in operator overloading for basic arithmetic & comparison symbols.
- `type()` — a function used to check the data type of a variable. But if we don't type/declare the var, it isn't documented anywhere.

### Some other useful symbols
| Symbol | Name | Meaning |
|---|---|---|
| `a // b` | Floor division | Quotient of a & b, removing the fractional part |
| `a % b` | Modulus | Integer remainder after dividing a by b |
| `a ** b` | Exponentiation | a^b |
| `-a` | Negation | Negative of a |

### True Division vs Floor Division
- **True division:** keeps the entire decimal part. Always returns a float, even if a & b divide evenly.
  ```python
  6 / 3   # → 2.0
  ```
- **Floor division:** drops the remainder & rounds down to the next lower whole number. Returns `int` if both inputs are `int`, returns `float` if either input is a float.
  ```python
  10 // 3    # → 3
  10.0 // 3  # → 3.0
  -10 // 3   # → -4
  ```

### Order of Operations — PEDMAS
Parentheses → Exponentiation → Multiplication/Division → Addition/Subtraction

- `abs()` function can only take ONE argument.

---

## Built-in Functions for Working with Numbers
- `min()`, `max()`, `abs()` → `abs()` gives the abs value of a number.
- `int()` & `float()` can also be used as functions which convert type (even on strings).

### Swapping Variables
You can swap variables either by using a temp variable, or by using a method called **tuple packing & sequence unpacking**:
```python
a, b = b, a
```

## Functions & Getting Help
- `help()` = the function that displays the header of a function + a brief description of what it does.
- The `print()` function can take an argument called `sep` — basically the space we insert between values.

### Functions — syntax
```python
def funcName(arguments):
    # the indented block of code following the def line
    # runs when the function is called
```

## Return Statements
- When Python encounters a `return` statement, it exits the function immediately & passes the value on the right-hand side back to the calling context.

## Docstrings
- A triple-quoted string that immediately comes right after the header of a user-defined function.
- When we call `help()` on the function, it shows the docstring.

- `>>>` is a reference to Python's interactive shell.

## Functions That Don't Return
- Python allows us to define functions that don't return anything.
- Calling them just shows a single space in the interactive shell (returns `None`, i.e. "null").

## Default Arguments
For `print()`, the default value for the `sep` argument is a single space. But we can set a diff value:
```python
print(1, 2, 3, sep=' < ')
```

- Python by default collects output into a temp storage space (buffer) & doesn't display it until it fills up or it hits a newline char. This is triggered by `flush=False` (default).

### Optional Keyword Arguments for `print()`
1. `file` — a file-like object (stream)
2. `sep` — string inserted between values
3. `end` — string appended after the last value (default: newline)
4. `flush` — whether to forcibly flush the stream by clearing the buffer

## Higher Order Functions
Functions that operate on other functions are called **higher order functions**.
```python
fn(fn(arg))
```

## `round(num, ndigits)`
Rounds `num` to the nearest 10^(-ndigits).
- `ndigits = -1` → rounds to nearest 10
- `ndigits = -2` → rounds to nearest 100

This is used when dealing with very large numbers — e.g. areas of countries!

## Default Argument Example
```python
def to_smash(total_candies, friends=3):
    return total_candies % friends

# So basically if we pass the friends param like to_smash(91, 5),
# the 5 will overwrite the 3 — but 3 is the default value if no argument is provided.
```

---

## Booleans & Conditionals

- Variable type: `bool`

### Boolean / Comparison Operators
```
a == b, a != b, a < b, a > b, a <= b, a >= b
```
```python
3.0 == 3      # → True
'3.0' == 3.0  # → False (string vs number)
```

### Combining Boolean Values
- You can use `and`, `or`, and `not`.
- For boolean values, `and` is operated before `or`.

### Conditional Statements
```python
if (condition):
    ...
elif (condition):
    ...
else:
    print("xxx")
```

### `bool()` Function
Turns things into bools.
- All numbers are treated as `True` except `0`.
- All strings are treated as `True` except the empty string `""`.

### Ternary Syntax
```python
return True if (condition) else False
```

When we factor out `not` from a statement like:
```python
return not k and not m and not o
```
we're left with:
```python
return not (k or m or o)
```
