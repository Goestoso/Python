
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

</details>

* `f-strings:` can tell Python that values ​​will be inserted directly into a string.

```
name = 'Mathew'
print(f'My name is {name}')
# It is also possible to pass functions and methods
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
* `bool():` converts to an boolean value;
* `list(), tuple(), set(), dict():` used to create lists, tuples, sets and dictionaries, respectively;

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

