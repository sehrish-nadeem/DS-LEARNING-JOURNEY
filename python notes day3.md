# Python: Day 3, Strings & Dictionaries

## Strings
- Strings can be defined by both single & double quotes.
- Python's triple quote syntax allows us to write a string on multiple lines without adding the newline character.
- The `print()` function auto adds `\n` except when we specify it otherwise.
- Strings are basically a sequence of characters. We can apply every list operation to strings as well.
- We can also loop over them.
```python
planet = "pluto"
[char + '!' for char in planet]
# → ['p!', 'l!', 'u!', 't!', 'o!']
```

### But the way they differ from lists: they're immutable
- Assigning items to an index doesn't work in strings.
- `.append()` does not work either.

### String Methods
- `.upper()`, `.lower()`
- `.index()` → searches for the first index of a substring
- `.startswith()` → returns bool, basically verifies if the argument passed is the starting word or not
- `.endswith()`
- `.isdigit()` → checks whether a string contains only digits or not.

---

## Going Between Strings & Lists
- `.split()`: turns a string into a list of smaller strings, breaking on whitespace by default.
- `.join()`: joins small strings into a big one, using the string it was called on as a separator.

```python
words = claim.split()
# → ['Pluto', 'is', 'a', 'planet']

dates = '2006-12-21'
year, month, day = dates.split('-')
# in this case the splitting happens when a hyphen occurs
```
```python
'/'.join([month, day, year])
# → '21/12/2006'
```

- We can concatenate strings using the `+` operator. To concatenate non-string objects, call `str()` on them first.
- A more readable way to do this is by using `.format()`
```python
"{}, you'll always be the {} planet.".format(planet, position)
```

### `.format()` in More Detail
We call `.format()` on a format string where the Python values we want to insert are represented by `{}`.
```python
"{:.2f}"    # → 2 decimal places
"{:.3%}"    # → 3 decimal places, formatted as a percent
"{:,}"      # → separates using commas
```
The `:` tells Python what follows next is how I want this data to look.
- We can also refer to `.format()` arguments by index, starting from 0.

---

## Dictionaries
Built-in Python data structure for mapping keys to values.
```python
numbers = {'one': 1, 'two': 2, 'three': 3}
```
`'one'`, `'two'`, & `'three'` are keys, and `1`, `2`, `3` are the corresponding values.

We can use the same syntax to add another key:value pair.
```python
numbers['eleven'] = 11
```
Values are accessed via square brackets, similar to indexing into lists & strings. You can also change the value associated with an existing key the same way:
```python
numbers['one'] = 'Pluto'
```

### A loop over a dictionary will loop over its keys.

### Core Operational Differences (Lists vs Dicts)
- Lists allow duplicates.
- Dictionaries enforce unique keys: when a dictionary comprehension encounters duplicate keys, Python is free to overwrite the previous value with the newest one.
```python
cars = ["Ford", "Ferrari", "Fiat"]
{brand[0]: brand for brand in cars}
# → {'F': 'Fiat'}
# so basically the previous values will never show up in the output
```
- Basically, multiple keys can point to the same value, but a single key can't point to multiple values.

### Dict Methods
- We can access a collection of all the keys using `dict.keys()` or values using `dict.values()`.
- `dict.items()` lets us iterate over the keys & values simultaneously.
```python
for planet, initial in planets.items():
    ...
# 2 variables, one for key and one for value
```

*(Gap-fill note: `dict.items()` actually returns each key-value pair as a **tuple**. If you only provide one loop variable instead of two, Python won't unpack it, you'll just get the whole `(key, value)` tuple as-is, not split into two separate variables.)*

### Dictionary Comprehension
Similar syntax to list comprehension.
```python
planetInitial = {planet: planet[0] for planet in planets}
```
You can read this shifted right to left, it loops through the list, and for each planet: `planetInitial[planet] = planet[0]` extracts the char from the first index. `key: value` defines the key:value pair for the new dictionary, the full planet name becomes the key.

### Difference Between List & Dictionary Comprehension
| Feature | List | Dictionary |
|---|---|---|
| Output Type | list (ordered) | dict (unordered) |
| Brackets | square brackets `[]` | curly braces `{}` |
| Internal Element Syntax | single value (item) | key : value pair, separated by `:` |
| Use Case | transforming/filtering an existing sequence | building a lookup table / mapping one thing to another |

---

## `.rstrip()`
Strips off specified characters from the end of a word.
```python
"word,".rstrip(',')
# will remove any commas after the word
```

---

## Working With External Libraries
- A module is a collection of variables. Someone else defined these variables, for eg. `math` is a module, and we can see all the names in it using `dir()`.
```python
import math
dir(math)
```
- If we know we'll be using functions from a library frequently, we can import it under a shorter alias.
```python
import math as mt
mt.pi
mt.log()
```
- We can also refer to the variables directly (without the dotted prefix) if we import everything from a module using `*`:
```python
from mt import *
```
- If you're using more than one library, it's better to just import the specific things you need from each module.
- Modules can also have variables referring to other modules.
```python
import numpy
numpy.random.randint()
```

### Tools for Understanding Strange Objects
1. `type()` → what is this thing?
2. `dir()` → what can I do with it?
3. `help()` → tell me more

---

## Escape Characters (gap-fill note based on your notes)
When you use a backslash in a string to create an escape character (like `\n` for newline), Python treats that whole escape sequence as **1 character**, even though you typed 2. So `len("\n")` is `1`, not `2`. Also, the length of an empty string, when converted to a Boolean, evaluates to `False`.

---

## `enumerate()`
Adds a running counter to an iterable (list, tuple, or string), lets you track both the index & value of items simultaneously during a loop. Basically eliminates the need to put a manual counter.
```python
enumerate(iterable, start=0)

for index, fruit in enumerate(fruits):
    ...
```
