
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

> if (condition):
> <br>
>----#execute code if true
> <br>
> else: 
> <br>
>----#execute code if false         

📑 Indentation is mandatory in Python to create blocks of code!

