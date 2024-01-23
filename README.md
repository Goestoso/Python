
<h1>Python Games</h1>
  
<div style="display: flex; justify-content: center; gap: 40px;">
<figure style="margin-right: 20px;">
  <img align="center" alt="Goes-Python" height="100" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg"  >
   <figcaption><b>Games to introduce the concept of language and its structure.</b></figcaption>
</figure>
</div>

<br>

> `Function:` block of reusable code that performs a specific task when called.

<h2>Built-in Functions</h2>

These are functions that are integrated directly into the language and are always available for use, without the need to import additional modules.

* `help():` Provides documentation and help information about Python.

<details>

<summary>how to use help</summary>

* Get help on a specific object: 

```
help(object)
```

* Get help on a built-in function:

```
help(print)
```

</details>

* `print():` Print values ​​to the console.

> print(*args, sep=' ', end='\n', file=None, flush=False)
> <br>
>`args:` values that will be printed;
> <br>
> `sep:` separator between values;
> <br>
> `end:` what happens at the end ('/n' is a line break);
> <br>
> `file:` here you can put the file name and its extension (.txt, for example);
> <br>
> `flush:` controls whether the buffer should be flushed after calling the function;

```
var = Brazil
print(var, ' is a country', sep=':', end='.' )
```

* `type():` Returns the type of the object declared inside the parentheses.

```
type(var)
# output: 'str'
```

* `.format():` used to perform `string interpolation`, that is, it allows you to insert values ​​into a formatted string, replacing placeholders `{}`.

```
name = "Alice"
age = 30
print("My name is {} and I am {}".format(name,age))
```

<details>

<summary>strings interpolation</summary>

* In the format function you can pass parameter index {`0`}, {`1`}

* It is possible to format floats {`:f`} to define the type, {`:.2f`} 2 places after the comma, {`:.7.2f`} width of 7 characters and 2 of which will be after the decimal point., {`:02d`} an integer in a string with a total width of 2 characters, and padding with leading zeros if necessary (type `d` = integers).

* `f-strings:` can tell Python that values ​​will be inserted directly into a string.

```
name = 'Mathew'
print(f'My name is {name}')
# It is also possible to pass functions and methods
```
</details>

* `round():` is used to round float values ​​to the nearest integer.

```
round(5.678) # 6
round(5.678,1) #is rounding the number to one decimal place, 5.7
```

* `abs():` for absolute (positive) values.

```
print(abs(-3.14)) # Output: 3.14
```

<h3>Python Typing</h3>

In Python, it is not necessary to declare the variable's type explicitly ('str', int(1), float(1.2), bool(true or false)...), as it is automatically determined based on the value assigned to it.

→ This makes the language `flexible` and `dynamic`.

<details>

<summary>Curiosity</summary>

> It is possible to make type annotation to facilitate reading:
> <br>
> name: str = "Alice"

</details>

📃 Python uses the `snake_case` pattern by convention!

* `input():` function that captures a value entered by the user in the console.

```
var = input("Type your name: ")
```

🚨 Attention: this function always returns str type!

<h3>Conversion Functions</h3>

* `int():` converts to an integer value;
* `float():` converts to an float value;
* `bool():` converts to an boolean value (empty values ​​and 0 when applied return False);
* `list(), tuple(), set(), dict():` used to create lists, tuples, sets and dictionaries, respectively;

<details>

<summary>decimal</summary>

* for more precision of floating point numbers:

```
from decimal import Decimal

num1 = Decimal('3.1415')
num2 = Decimal('2.7182')
multiplication = num1 * num2
```

→ `Decimal():` class method.

→ `decimal:` library.
</details>

→ `/` returns float and `//` returns int

> print(1/2 + ' and ' + 1//2) # 0.5 and 0

➕ is used to add and concatenate;
> print(1 + 2) returns: 3 // print('1' + 2) returns: 12

❌ Python does not perform implicit conversion, and a `sugar syntax` may occur in cases of `*` for example;

> print('1' * 2) returns: 1 \n 1

<h3>Conditional</h3>

* To create a conditional, use `if`, and comparison signs, such as `==, >, <, <=, >=, !=`;

* To add more conditions contrary to the first, use `elif` for more conditionals and for a condition if no other is satisfied, use `else`;

* Use `and` if two comparisons need to be true and `or` if only one condition needs to be true;

> if (condition1 and condition2):
> <br>
>----#execute code if true
> <br>
> elif (condition or other_condition):
> <br>
>----#execute code if "else if" is true
> <br>
> else: 
> <br>
>----#execute code if false         

📑 Indentation is mandatory in Python to create blocks of code!

> `ternary:` var = 'value' if condition else 'other_value'

❗To negate a Boolean value:

> `not` bool-condition

<h3>Repeat loops</h3>

* `while:` it receives a condition to execute the block of code as long as the condition is true.

> while (condition):
> <br>
>----#execute the code as long as it is true
> <br>
> increment += value

* `+=` is used to update the value of the variable by adding a certain value to it.

* `for:` the idea of ​​for is to define the initial value and the final value, which the loop automatically increments.

→ To define the initial and final value, use the `range()` function, passing them as a parameter.

> The `range()` function in Python is used to generate a sequence of numbers.

```
for i in range(5):
    print(i) # This will print the numbers 0 to 4.
    break # get out of the loop
    continue # to skip the rest of the code in the loop body and go to the next iteration.

for i in range(2, 8):
    print(i) # This will print the numbers 2 through 7.

for i in range(1, 10, 2): # range(start, stop, step), where step is the interval between the numbers
    print(i)
```

 ➡️ <a href="https://docs.python.org/3/library/functions.html" target="_blank">More about built-in functions...</a>

 <h3>Python Key words</h3>

> There are reserved value words (start with `UPPERCASE`):
> `True-False-None`
<br>

> And modifying reserved words (usually in `lowercase`):
> `if-while-in-not`

<h2>Built-in Modules</h2>

These are libraries that come with the Python installation.

<h3>random</h3>

→ Generate random values:

```
import random # import the library
random.random() * 100 # To increase the value 100 times
```

> `random:` it generates values ​​between 0 and 1.

```
random.randrange(1,100) # creates a value from 1 to 100
```

* Random numbers are pseudo-random, as the value generated is actually a new `seed`. Therefore, it uses the milliseconds as a seed behind the scenes with the `seed()` function.

<h3>math</h3>

→ Provides mathematical functions such as sine, cosine, logarithms, etc.

```
import math
print(math.sin(x)) # calculate the sine of x
math.sqrt(x) # Return the square root of x.
math.cos(x) # Return the cosine of x radians.
math.tan(x) # Return the tangent of x radians.
math.log10(x) # Return the base-10 logarithm of x.
math.pow(x, y) # Return x raised to the power y.
```

<h3>datetime</h3>

→ Manipulation of dates and times.

```
from datetime import datetime, timedelta
now = datetime.now() # Gets the current date

# Add a day to the current date
one_day = timedelta(days=1)
tomorrow_date = current_date + one_day

# Subtract a week from the current date
one_week = timedelta(weeks=1)
past_date = current_date - one_week

# Calculate the difference between two dates
other_date = datetime(2023, 12, 31)
difference = other_date - current_date
```

➡️ <a href="https://docs.python.org/3/py-modindex.html" target="_blank">More about built-in modules...</a>

<h2>Creating Functions</h2>

Using the word `def` you can define a function.

> def funtion(): # file function.py
> <br>
>----# function code

→ This way it is possible to call custom functions in other files, using the module name and calling its function:

```
import functionp
functionp.function()
```

→ Functions can have parameters and returns:

```
def sum(a,b):
     return a + b
s = sum(3,4)
```

`__name__:` an execution variable that indicates the context in which a module or script is being executed.

> Therefore, it can be `__main__` when executed `directly` or the `module name` if `imported`:

```
if(__name__ == "__main__")
    function()
```

<h3>Parameters</h3>

* In _dynamic typing_, the passing of object parameters is ***by reference*** (in the case of mutable objects), pointing to the `array` type variable, for example.

* Values ​​of _primitive types_ are immutable, so passing is ***by value***, as in the case of `str` and `int`.


<h2>Sequence Types</h2>

The main sequence types are, in addition to strings, lists (vectors and matrices), tuples, dictionaries, ordered and unordered collections.

<h3>str</h3>

A string is considered one of the main sequence types.

→ A string is a `sequence of characters` and can be manipulated (***in Python***) like a sequence, meaning you can access individual characters by index, iterate over the characters, slice the string, and perform various sequence-specific operations.

* `.find():` used to find the position of a substring occurrence.

```
word = "banana"
word.find("b") # returns the position 0
```

* `.upper():` method of creating a substring with all characters capitalized.

```
word = "banana"
word.upper() # returns BANANA
```

* `.lower():` convert to lowercase.

```
word = "BANANA"
word.lower() # returns banana
```

* `.strip():` removes empty spaces.

```
words = "for get"
words.strip() # returns 'forget'
```

> The `str` type is ***immutable***, so string methods will always create replicas, that is, substrings.


➡️ <a href="https://docs.python.org/3/library/stdtypes.html#string-methods" target="_blank">More about str methods...</a>

<h3>lists</h3>

To create a list we use `[]`:

```
var = []
```

→ There are several list functions, such as `min()`, `max()` or `len()`;

→ It is also possible to access its methods such as `.append()`, `.extend()`, `.index()`, `.remove()`, `.insert()`, `.count()`, `.sort()`, `.pop()` , `.reverse()` or `.clear()`;

> The `in` operator returns _True_ or _False_ if the element is inside the list;

```
list = ['element', 'object']
'element' in list # returns True
 ```

➡️ <a href="https://docs.python.org/3/library/stdtypes.html#lists" target="_blank">More about lists methods...</a>

<h3>tuples</h3>

To create a tuple we use `()`:

```
var = ()
```

> The `list()` is _mutable_, while the `tuple()` is _immutable_.

⚠️ Methods that alter lists ***do not*** work on tuples!

➡️ <a href="https://docs.python.org/3/library/stdtypes.html#tuples" target="_blank">More about tuples methods...</a>

<h3>lists x tuples</h3>

→ It is possible to implement lists within tuples and vice versa;

```
foods = ['rice', 'bean']
drinks = ['water', 'juice']
stock = (foods, drinks)
```

→ To access values ​​from lists or tuples with implementation, use `[][]`;

```
foods = ['rice', 'bean']
drinks = ['water', 'juice']
stock = (foods, drinks)

# Acessing the list of foods
list_foods = stock[0]
print(list_foods)  # Output: ['rice', 'bean']

# Acessing the list of drinks
list_drinks = stock[1]
print(list_drinks)  # Output: ['water', 'juice']

# Acessing the first item of the food list
first_food = stock[0][0]
print(first_food)  # Output: 'rice'
```

→ Using the `list()` and `tuple()` functions it is possible to convert arrays;

> Remember that when you try to convert a tuple to a list, you are creating a new list and not changing the original tuple, since _tuples are immutable_.

<h3>set</h3>

`set()` is used to create a collection (***not a sequence***) with unique elements using `{}`:

```
var = {}
```

→ To add values ​​to _set_ you must use `.add()`;

→ _set_ has no indexes as it is _not a sequence_.

<h3>dict</h3>

The `dict()` creates a collection (***not a sequence***) that associates key with value:

```
var = {'value':1}
```

→ You can also associate a key to create lists:

```
# Creating a empty dict
my_dict = {}

# Adding keys and associating lists to them
my_dict['fruits'] = ['apple', 'banana', 'orange']
my_dict['animals'] = ['dog', 'cat', 'bird']

# Acessing the values associated to the keys
print(my_dict['fruits'])  # Output: ['apple', 'banana', 'orange']
print(my_dict['animals'])  # Output: ['cachorro', 'cat', 'bird']

```

<details>

<summary>OrderedDict</summary>

* Is a subclass of the dict (dictionary) type in Python that maintains the insertion order of items:

```
from collections import OrderedDict

# Creating a OrderedDict
ordered_dict = OrderedDict()

# Adding items
ordered_dict['one'] = 1
ordered_dict['two'] = 2
ordered_dict['three'] = 3

# Iterating over the OrderedDict
for key, value in ordered_dict.items():
    print(key, value)
```

→ `OrderedDict():` class method.

→ `collections:` library.

</details>

<h2>Files</h2>

→ To open a file:

```
file = open("file_name.txt", "w")
```

> `file_name` is the name of the file;
> `w:` to write;
> `r:` to read;
> `rb:` to read binary;
> `a:` to append;

→ To write to a file:

```
file.write("word")
```

→ To close a file:

```
file.close()
```

→ To read a file:

```
file.read() #.readLine reads a line
```

* The read pointer goes to the end of the file, so you have to open it again.

> `with:` guarantees the closure of the file even with an error.

```
with open("file") as name
```

➡️ <a href="https://www.w3schools.com/python/python_ref_file.asp" target="_blank">More about file methods...</a>
