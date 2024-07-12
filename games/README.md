
<h1>Python Games</h1>
  
<div style="display: flex; justify-content: center; gap: 40px;">
<figure style="margin-right: 20px;">
  <img align="center" alt="Goes-Python" height="100" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg"  >
   <figcaption><b>Games to introduce the concept of language and its structure.</b></figcaption>
</figure>
</div>

<br>

> `Function:` block of reusable code that performs a specific task when called.
> <br>
> `**kwargs:` an abbreviation for keyword arguments, they are used when you want to allow a function to accept any number of named arguments that have not been explicitly defined beforehand.

In Python, ___functions___ are first-class _objects_, that is, they can be passed as arguments and assigned to variables.
> `def` creates an instance of the `function` class

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
* `str():` converts to a string value (text);
* `chr(int i):` returns the returns the `ASCII` character of an integer;
* `ord(char a):` returns the integer value of a character from the ASCII table;
* `bool():` converts to an boolean value (empty values ​​and 0 when applied return False);
* `list(), tuple(), set(), dict():` used to create lists, tuples, sets and dictionaries, respectively;

 <details>

<summary>ASCII</summary>

The `ASCII Table` (American Standard Code for Information Interchange) is a set of characters encoded to represent text.

> The printable values ​​start from index __32__ and go up to __126__.

</details> 

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

→ `round():` is used to round float values ​​to the nearest integer.

```
round(5.678) # 6
round(5.678,1) #is rounding the number to one decimal place, 5.7
```

→ `abs():` for absolute (positive) values.

```
print(abs(-3.14)) # Output: 3.14
```

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

<h4>Truth Evaluation in Python</h4>

→ In the context of Python, __true__ and __false__ are not limited to just the Boolean values ​​`True` and `False`; other values ​​are ___implicitly converted to True or False___ based on certain rules:

* Values ​​considered __false__: `None`, `False`, `0`, `0.0`, `0j` (complex zero), `''` (empty string), `[]` (empty list), `()` (empty tuple), `{}` (empty dictionary), `set()` (empty set), custom _class objects_ that implement the `__bool__()` or `__len__()` method and return `False` or `0`.
* Values ​​considered __true__: Any value ___that is not implicitly false___, such as `non-zero numbers`, `non-empty strings`, `non-empty lists`, etc.

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

> import __random__

→ Offers a variety of methods for generating pseudorandom numbers and performing random selections.

```
random.random() * 100 # To increase the value 100 times
```

```
random.randrange(1,100) # creates a value from 1 to 100
```

```
random.randint(a, b) # returns a random integer between the values ​​a and b (inclusive).
```

* Random numbers are pseudo-random, as the value generated is actually a new `seed`. Therefore, it uses the milliseconds as a seed behind the scenes with the `seed()` function.

```
random.sample(seq, k) # : returns a list with k random elements of a sequence, without repetitions.
```

```
random.choice(seq) # randomly selects an element from a sequence.
```

```
random.shuffle(seq) # shuffles the elements of a sequence.
```

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
one_day = timedelta(days=1) # Define a timedelta object representing an interval of one day
tomorrow_date = now + one_day # Calculate tomorrow's date by adding one day interval to the current date

# Subtract a week from the current date
one_week = timedelta(weeks=1)
past_date = now - one_week

# Calculate the difference between two dates
other_date = datetime(2023, 12, 31)
difference = other_date - now

# String for Date or Time
date_string = "2023-05-20"
date = datetime.strptime(date_string, "%Y-%m-%d")
print(date)  # Output: 2023-05-20 00:00:00

# Formatting the date to "dd/MM/yyyy" format
date = datetime(2023, 5, 20)
formatted_date = data.strftime("%d/%m/%Y")
print(formatted_date) # Output: 05/20/2023
```

<h3>re (regex)</h3>

> import __re__

→ Provides functions and classes for working with regular expressions (`regex`).

* `String raw (r):` means that the characters will be treated literally, without interpretation of escape characters, such as '\n'.

```
regex = r'C:\PathFolder\File'
```

<h4>Impersonation shortcuts</h4>

→ `\` is used in `regex` to indicate special characters or ___metacharacters___ (also to disregard shortcuts, such as '\.').
* `\d:` any decimal digit;
* `\w:` any alphanumeric character;
* `\s:` any whitespace character;
*  `.:` any character except line break;

<h4>Search ranges</h4>

→ __Comprehension__ with `[]`, __negation__ with `^`.

* `Numeric(\d):` use the format [0-9];
* `Letters:` [a-z], [A-Z];
* `Alphanumerics(\w):` [a-zA-Z0-9];
* `ASCII Printables:` [!-~];

<h4>Border shortcuts</h4>

* `^:` represents the beginning of a line or string;
* `$:` end of a line or string;
* `\A:` start of string, but not affected by multiple lines;
* `\Z:` end of string, case similar to `\A`;
* `\b:` word boundary, indicating a transition between an alphanumeric character and a non-alphanumeric character;
* `\B:` a position that is not the word boundary, regardless of whether it is at the beginning or end of a word;

<h4>Quantifier shortcuts</h4>

* `*:` matches zero or more occurrences of the previous pattern. 
* `+:` matches one or more occurrences of the previous pattern. 
* `?:` matches zero or one occurrence of the previous pattern. 
* `{n}:` correspond to exactly n occurrences of the previous pattern. 
* `{n,}:` matches n or more occurrences of the previous pattern. 
* `{n,m}:` with a minimum and maximum number {n,m} correspond to n to m occurrences of the previous pattern. For example, a{2,4} matches two to four occurrences of the letter "a".

```
regex = r'\b\d{3}\.\d{3}\.\d{4}\b'
```

<h4>Methods</h4>

* `re.compile(pattern, flags=0)`:

> Compiles a regular expression into a regular expression pattern object for later use.
>  <br>
> `pattern:` the regular expression to be compiled.
>  <br>
> `flags (optional):` modifiers that change the behavior of the regular expression.

```
default_phonenumber = re.compile(regex)
```

* `re.match(pattern, string, flags=0):`

> Checks if the regular expression matches the beginning of the string.
> <br>
> Returns a match object if the regular expression matches; otherwise, returns _None_.

* `re.search(pattern, string, flags=0):`

> Searches for a match anywhere in the string.
> <br>
> Returns a match object if the regular expression matches; otherwise, returns _None_.

```
case1 = "My number is 123.456.7890"
match1 = default_phonenumber.search(case1)
```

* `re.findall(pattern, string, flags=0):`

> Finds all occurrences of the regular expression in the string.
> <br>
> Returns a list of all matches found.

```
default = re.compile(r'\Bword\B')
text = "sword, word, wordpress, wordy"
result = default.findall(text)
print(result) # Output: ['word', 'word']
```

* `re.finditer(pattern, string, flags=0):`

> Finds all occurrences of the regular expression in the string.
> <br>
> Returns an iterator that produces match objects for each match found.

```
text = "banana"
default = re.compile(r'ana')

for match in pattern.finditer(text):
    start = match.start() # match start index
    end = match.end() # match end index
    print(f"Found '{match.group()}' between indexes {start} and {end}.") 
```

* `re.sub(pattern, repl, string, count=0, flags=0):`

> Replaces all occurrences of the regular expression in the string with new text.
>  <br>
> Returns a new string with all replacements made.
>  <br>
> `count:` limits the maximum number of replacements, if greater than 0, replaces _n_ matches from left to right, if less than 0, will replace except the last _n_ matches;
> <br>
> `repl:` value that will replace in the `string`;

* `re.split(pattern, string, maxsplit=0, flags=0)`:

> Splits the string into substrings using the regular expression as delimiter.
> <br>
> Returns a list of the resulting substrings.
> <br>
> `maxsplit:` limits the maximum number of divisions to _n_ times;

* `match.group(n=0):`

> Method of matching objects returned by search methods (`findall()`, `finditer()`, `match()`, `search()`).
> <br>
> It is used to get the matching text found in the original string.
> If you provide an integer argument n, where n is the capture group number, it returns the text corresponding to the specified capture group.
> If there are no capturing groups in the regular expression, the default argument is 0, matching the entire match.

```
text = "Date of birth: 03/12/1990"
default = re.compile(r'Date of birth: (\d{2})/(\d{2})/(\d{4})')

match = pattern.search(text)
if match:
    print("Day:", match.group(2))
    print("Month:", match.group(1))
    print("Year:", match.group(3))
    print("Match:", match.group())
```

<h5>flags</h5>

* `re.IGNORECASE` or `re.I`:

> Matches patterns in a case-insensitive manner.

* `re.MULTILINE` or `re.M`:

> Allows the ^ and $ metacharacters to match the start and end of each line (in addition to the start and end of the string).

* `re.DOTALL` or `re.S`:
  
> Makes the dot (.) metacharacter match any character, including line breaks (\n).

* `re.VERBOSE` or `re.X`:

> Allows you to write more readable regular expressions by ignoring whitespace and comments within the regular expression.

```
# Regular expression with re.VERBOSE
default_with_verbose = re.compile(r'''
    \b # Start of word
    (?: # Non-capturing group for the first set of digits
        \d{3}\. # Three digits followed by a period
    )?          # The first set is optional
    \d{3} # Three digits
    \.          # A dot
    \d{3} # Three digits
    - # A hyphen
    \d{2} # Two digits
    \b # End of word
''', re.VERBOSE)

# Testing regular expressions
cpf = "My CPF is 123.456.789-01"

result_with_verbose = default_with_verbose.search(cpf)
```

* `re.ASCII` or `re.A`:

> Ensures that only ASCII characters are considered by the regular expression.

* `|:`

> Bitwise operator to add multiple flags in the regex;

```
flags=re.IGNORECASE | re.DOTALL
```

<h3>tkinter (GUI)</h3>

> import __tkinter__ as __tk__

→ It is a built-in module that allows the creation of graphical interfaces in a simple way.

* root_window = `tk.Tk()`

<h4>The main window</h4>

> `tk.Tk():` creates the main application window, being essential because it is the ___starting point for any graphical interface___.

* The `Tk` _class instance_ is the root of windows, widgets and components.

* The window is like a _container_ of widgets.

<h4>Main methods</h5>

* root_window`.mainloop():` starts the application's ___event loop___.
* root_window`.destroy():` destroys the window.
* root_window`.title(str):` sets the window title.
* root_window`.geometry(<width>x<height>+or-<posx>+or-<posy>):` determines the size to be displayed and the position on the screen.
* root_window`.protocol(protocol, command):` used to associate a function (or method) with a specific window event (_protocol example_: try `'WM_DELETE_WINDOW'` when the user tries to close the window by clicking the close button (X)).
* root_window`.inconbitmap('image.ico'):` change the window icon.
* root_window`.withdraw():` hide the window.
* root_window`.deiconify():` show hidden window.
* root_window`.minsize(with, height):` sets the minimum window size.
* root_window`.maxsize(with, height):` sets the maximum window size.
* root_window`.winfo_screenwidth():` captures the user's screen width.
* root_window`.winfo_screenheight():` captures the user's screen height.
* root_window`.winfo_children():` gets all child _widgets_ of the window.

<h4>Event loop</h4>

→ It is a _continuous cycle_ that waits for and dispatches _events_ or messages in a program.

* Detects user actions;
* Calls the callback functions associated with these _events_;
* Manages GUI update;
* 🔄 It runs continuously throughout the life of the application, waiting for events and responding to them.

<h5>Methods for handling events</h5>

* root_window`.quit():` close the loop;
* root_window`.update():` processes all queued events and updates the GUI;
* root_window`.update_idletasks():` processes tasks that need to be executed when the program is idle;
* root_window`.after(ms, callback, *args):` schedules a function to be called after certain milliseconds;
* root_window`.bind(event, callback, add=None):` associates a function with an event that can occur in a widget or in user interaction;
* root_window`.unbind(event, id=None):` removes the association of an event with a function;
* root_window`.event_generate(event, **kwargs):` generates an event manually, which can be useful for simulating user events.

<h4>Control variables</h4>

→ They are special objects that serve as intermediaries between _widgets_ and the values ​​they display or store.
* `tk.StringVar()`
* `tk.IntVar()`
* `tk.DoubleVar()`
* `tk.BooleanVar()`
> Use variable`.get()` to capture the object's value and variable`.set(value)` to modify its value.

<h4>Widgets</h4>

→ _Widgets_ are elements of a graphical user interface (GUI) that allow users to interact with the program, they can be _buttons_, _text boxes_, _labels_, _menus_, and other controls that receive and display information or provide a specific way for the user to interact with the operating system or an application.

* `tk.Label(window, text or image, **kwargs)`
> `**kwargs:` it is possible to customize the label text, using __anchor__ for the text position (N, E, S, W, NE, SE, SW, NW or CENTER), __font__ and __size__ (it is possible to pass a tuple with the name of the font and the size, such as font=("Arial", 12)), __fg__ for font color ("white", "black", "blue"...) and __bg__ for background color...
* `tk.Button(window, text, command)`
> `command` is the _reference_ of the function or method to be used on the button; the function/method reference does not involve its call, so it ___does not need the parentheses ()___.
* `tk.Entry(window)`
* `tk.Checkbutton(window, text, var)`
> `var` is the variable associated with the checkbox, usually a `tk.BooleanVar()`
* `tk.Radiobutton(window, text, var, value)`
> `value` is the value that the associated variable will receive when this radiobutton is selected.
* `tk.Listbox(winsow, selectmode)`
> `selectmode` is the selection mode (SINGLE, BROWSE, MULTIPLE, EXTENDED).
> <br>
> selection_list = tk.Listbox(window, SINGLE), use selection_list`.insert(position, item)` to insert items into the Listbox.
* `tk.Canvas(window, width, height)`
> `canvas.create_*(x1, y1, x2, y2, ..., *kwargs)` creates geometric figures, such as lines, circles, squares, rectangles, among others.
* `tk.Frame(window, **kwargs)`
> `what is it for:` serves as a container to organize other widgets visually.
> <br>
> `**kwargs:` _borderwidth_: specifies the width of the frame border (default is zero); _height_ and _width_: defines the height and the width of the frame; _padding_: creates spacing within the frame and around the contained widgets; _cursor_: changes the appearance of the cursor when it is over the frame; _style_: specifies a custom style for the widget...

<h5>Widget methods</h5>

* widget`.pack(**kwargs):` to organize and position widgets within a _container_, such as a window or _frame_.
> The method automatically calculates the position and size of the widget.
> <br>
> `**kwargs:` __side__ to specify which side the widget should be wrapped on, __fill__ to define how it should fill the available space, __expand__ to determine whether it should expand to fill the entire space, __padx__ and __pady__, to control the _horizontal_ and _vertical_ padding around of the widget.
> <br>
> widget`.pack_forget():` used to temporarily hide a widget when using pack.
* widget`.grid(**kwargs):` geometry manager that organizes widgets into a grid (or table) of rows and columns.
> `**kwargs:` __row__, __column__, __rowspan__ and __columnspan__(defines how many rows and columns the widget will cover), __sticky__(defines where the widget should "stick" within the grid cell, it can be a combination of directions, N, S, E, W), __padx__ and __pady__, __ipadx__ and __ipady__ (internal horizontal and vertical padding).
> <br>
> widget`.grid_remove():` used to temporarily hide a widget when using grid.
* widget`.place(x, y, width, heigth, **kwargs):` allows you to explicitly set the position and size of a widget relative to the window or another widget.
> This method gives you a little more control over the interface design.
> <br>
> `**kwargs:` _relx_ and _rely_: specify the relative coordinates of the widget's top-left corner relative to the size of the parent widget; _aanchor_: sets the widget's anchor point (“N”, “NE”, “E”, “SE”, “S”, “SW”, “W” or “NW”); _bodermode_: defines whether other options refer to the inside or outside of the widget ( “INSIDE” (default) or “OUTSIDE”; _in__: allows you to place a widget inside another...
> <br>
> widget`.place_forget():` used to temporarily hide a widget when using place.

<h4>Secondary window</h4>

→ 👑 `Heritage:` the Toplevel class inherits the methods and attributes of the Tk class, as a consequence, it depends on a main window and the ___event loop___ is called only on the Tk instance.

* `tk.Toplevel(root_window):` creates a new window that is a child of the main window, that is, it is part of the same application.
* window`.wait_window(window):` causes program execution to wait until the specified window is destroyed.

<h4>Message boxes and dialogs</h4>

> from `tkinter` import `simpledialog`

→ `simpledialog:` provides methods for creating simple dialog boxes.

* `simpledialog.askstring(title, question, **kwargs)`
* `simpledialog.askinteger(title, question, **kwargs)`
* `simpledialog.askfloat(title, question, **kwargs)`
> `**kwargs:` title, prompt, initialValue, minvalue and maxvalue.

> from `tkinter` import `messagebox`

→  `messagebox:` provides methods for displaying predefined message boxes, such as warning, error, information, and question messages.

* `messagebox.showinfo(title, message, **kwargs)`
* `messagebox.showwarning(title, message, **kwargs)`
* `messagebox.showerror(title, message, **kwargs)`
* `messagebox.askquestion(title, message, **kwargs)`
> `askquestion` returns the strings 'yes' or 'no' depending on the option chosen by the user.
> <br>
> `**kwargs:` title, message, icon and type.

➡️ <a href="https://docs.python.org/pt-br/3/library/tkinter.ttk.html" target="_blank">Also discover the ttk module...</a>

<h3>time</h3>

> import __time__

→ Offers a variety of powerful features for working with dates and times.

* __time__`.time():` returns the number of seconds since the reference date (milestone zero or EPOCH).
> It is useful for measuring the execution time of a piece of code.

```
start = time.time()
# code
end = time.time()
duration = end - start
```

* __time__`.sleep(seconds):` pauses program execution for a specified number of seconds.
> Useful for creating delays or gaps between operations.

```
time.sleep(2) # pause the program for 2 seconds
```

* __time__`.localtime():` returns a local date and time object.
> Contains information such as year, month, day, hour, minute, second, etc.

* __time__`.strftime(format, object_date_hour):` converts a datetime object to a formatted string.
> The format can include codes to represent different parts of the date and time (for example: _%Y_ for the full year, _%m_ for month in two-digit format, _%d_ for the day of the month, _%A_ for the full name of the day of the week, _%B_ for the full name of the month...).

* __time`.gmtime():` returns a date and time object in UTC (Coordinated Universal Time) format.
> Useful for dealing with time zones and conversions between different time zones.

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

→ It is possible to import only specific functions `from` the module, use aliases `as` to re-present the module or even load all functions, methods and classes from the module using `*`:

```
from module_name import function_name1, function_name2
import module_name as my_module
from module_name import *
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

<h3>Variables</h3>

<h4>Local Variables:</h4>

* Defined within a method or function;

* The scope is limited to that function or method;

* It is _created when the function is called_ and _destroyed when completed_;

```
def example():
    var_local = "local"
```

⚠️ They are ***not accessible outside*** the function;

<h4>Global Variables</h4>

* Defined outside the function;

* It is accessible anywhere in the code;

```
var_global = "global"
def example():
    pass
```

⚠️ If you need to modify a global variable within a function, you will need to declare it as global within the function;

➡️ <a href="https://www.w3schools.com/python/python_functions.asp" target="_blank">More about creating functions...</a>

<h3>Lambda</h3>

→ `lambda` functions are small functions that can have any number of arguments, but only one expression. 

→ They are useful when you need a temporary function for a simple operation.

> __lambda__ _args_: _expression_ # assignature

```
square = lambda x:x**2
result = square(5) #25
```

<h3>🔁 Callback function</h3>

→ When a function is passed as an argument to another function and is invoked within that function.

> _Example_: You can use a callback function to perform an action when an ___event___(mouse clicks and movements, key presses, screen loadings...) occurs or when an ___asynchronous operation___(is an operation that allows the program to continue performing other tasks) completes.

```
# Example
def callback(value):
    print(value)
def multitwo(value, callback):
    result = value * 2
    callback(result)
multitwo(5, callback) # using function with callback
```

<h2>Sequence Types</h2>

The main sequence types are, in addition to strings, lists (vectors and matrices), tuples, dictionaries, ordered and unordered collections.

<h3>str</h3>

A string is considered one of the main sequence types.

→ A string is a `sequence of characters` and can be manipulated (***in Python***) like a sequence, meaning you can access individual characters by index, iterate over the characters, slice the string, and perform various sequence-specific operations.

* `.format():` used to perform `string interpolation`, that is, it allows you to insert values ​​into a formatted string, replacing placeholders `{}`.

```
name = "Alice"
age = 30
print("My name is {} and I am {}".format(name,age))
```

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

* `.split():` splits a string into list using ___sep___ as delimiter, if it is not used, whitespace will be used as ___sep___.

```
words = "for get"
words.split() # returns '["for", "get"]'
```

* `.join():` Concatenates a sequence of strings based on the passed delimiter.

```
delimiter = ""
words = ["for", "get"]
delimiter.join(words) # returns "forget"
```

* `.isdigit()`, `.isalpha()`, `.isalnum():` checks whether the string consists of only digits, letters, or letters and numbers, respectively.

```
s = "12345"
print(s.isdigit())  # Output: True

s = "hello"
print(s.isalpha())  # Output: True

s = "hello123"
print(s.isalnum())  # Output: True
```

<details>

<summary>strings interpolation</summary>

* In the format function you can pass parameter index {`0`}, {`1`}
> * It is possible to format floats {`:f`} to define the type, {`:.2f`} 2 places after the comma, {`:.7.2f`} width of 7 characters and 2 of which will be after the decimal point., {`:02d`} an integer in a string with a total width of 2 characters, and padding with leading zeros if necessary (type `d` = integers).

* `f-strings:` can tell Python that values ​​will be inserted directly into a string.

```
name = 'Mathew'
print(f'My name is {name}')
number = 1.2345
print(f'Number with two digits before and after the comma: {number:2.2f}')
# It is also possible to pass functions and methods
```

</details>

> The `str` type is ***immutable***, so string methods will always create replicas, that is, substrings.


➡️ <a href="https://docs.python.org/3/library/stdtypes.html#string-methods" target="_blank">More about str methods...</a>

<h3>lists</h3>

To create a list we use `[]`:

```
var = []
```

→ It is  possible to access its methods such as `.append()` to add an element at the end, `.extend()` to add a iterable, `.index(element)` to return the index of an element in the list , `.remove(element)` to remove an element from the list, `.insert(index, element)` to add the element at a specific position defined by the index, `.count()` to count the quantity of elements in the list, `.sort()` to sort the list, `.pop(index)` to remove the last element of the list or an element in the index position, `.reverse()` to make the list backwardsor or `.clear()` to clear the list;

> The `in` operator returns _True_ or _False_ if the element is inside the list;

```
list = ['element', 'object']
'element' in list # returns True
 ```
<h4>List functions</h4>

> The `reversed()` function returns an iterator that the elements of the original sequence are in reverse order.

```
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers) # Output: [5, 4, 3, 2, 1]
```

> The `sorted()` function returns an ordered iterable of list elements.

```
list = [3, 1, 2]
sorted = sorted(list) # [1, 2, 3]
```

> The `len()` function returns the number of elements in the list.

```
list = [1, 2, 3]
len = len(list) # 3
```

> The `min()` and `max()` functions returns the smallest and largest list elements, respectively.

```
list = [1,2,3]
min = min(list) # 1
max = max(list) # 3
```

> The `sum()` function returns the sum of all numbers in the list (__only works with lists of numbers__).

```
list = [1,2,3]
sum = sum(list) # 6
```

> The `enumerate()` function adds a counter to an iterable and returns an enumerator object that can be used to iterate over the iterable's index and value pairs.

```
list = [1,2,3]
for index, element in enumerate(list):
    print(f'{index}: {element}') # Output: the index of the element and the element separated by ':' 
```

<h4>List comprehension</h4>

→ It's a concise and elegant way to create lists using a for loop to generate the list's elements.

> list = [_expression_ __for__ _item_ __in__ _sequence_]

```
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascii = [ord(char) for char in text]
```

<details>

<summary>Slicing</summary>

Technique for accessing subsequences of sequences, such as arrays.

> ___sequence___[_start_:_stop_:_step_] is the signature

* _start_: subsequence starting index (inclusive);
* _stop_: subsequence end index (unique);
* _step_: interval between indexes;

```
s = "Hello, World!"
sub = s[0:5] # Hello
sub = s[:5] # Hello
sub = s[7:] # World!
sub = s[::2] # Hlo ol!
sub = s[::-1] # reverses the string(array)
```

</details>

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

→ To add values ​​to _set_ you must use `.add()`, to add arrays use `.update(array)`, to remove an item use `.remove(element)` if you want to generate an error if the element does not exist, to remove an item use `.discard(element)` if you don't want to generate errors if the element does not exist, to clear the set use `.clear()`;

→ _set_ has no indexes as it is _not a sequence_.

<h4>set operations</h4>

* `Union:` setA.___union___(setB);
* `Intersection:` setA.___intersection___(setB);
* `Difference:` setA.___difference___(setB);
* `Symetric difference:` setA.___symetric_difference___(setB);
* `If is a subset:` supersetA.___issubset___(subssetB);
* `If is a super set:` subsetB.___issuperset___(supersetA);

<h3>dict</h3>

The `dict()` creates a collection (***not a sequence***) that associates key with value:

```
var = {'value':1}
```

→ You can associate a key to create lists:

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

→ To replace a value or update the dict:

```
my_dict['fruits'][3] = "lemon" # ['apple', 'banana', 'lemon']
my_dict.update('vegetables': ['lettuce', 'potato', 'carrot'])
```

→ To delete keys:

```
del my_dict['animals'] # delete key
my_dict.pop() # delete and return its value
my_dict.popitem() # delete the last key
```

→ To fetch keys:

```
my_dict.items() # return all keys
my_dict.get('animals', "animals not found") # Return: animals not found
my_dict.get('vegetables') # Retturn: ['lettuce', 'potato', 'carrot']
```

→ Iterating a dict:

```
for key, value in my_dict.items():
    print(f'{key}: ')
    for item in value:
        print(f'{item}')
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

<h3>map</h3>

`map()` is a `built-in function` that takes a function and one or more iterables (like lists, tuples, etc.) as arguments. 

→ It applies the function to each element of the iterables and returns an iterator that produces the results.

> __map__(_function_, _iterable1_, _iterable2_, ...) # assignature

- _function_: the function to be applied to each element of the iterables.
_iterable1_, _iterable1_, ...: one or more iterables (lists, tuples, etc.) whose elements will be passed to the function.

```
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x:x**2, numbers)
print(squares) # Output: [1, 4, 9, 16, 25]
names = ['Alice', 'Bob', 'Charlie']
surnames = ['Smith', 'Jones', 'Brown']
# Concatenate the full names
full_names = map(lambda name, surname: name + ' ' + surname, names, surnames)
print(list(full_names)) # Output: ['Alice Smith', 'Bob Jones', 'Charlie Brown']
```

<h4>⚠️ Be careful with maps!</h4>

* `map()` returns an iterator, not a list. You can convert this iterator to a list using `list()`, as shown in the examples above;
* The _function passed_ to `map()` can be any function (defined by `def` or `lambda` function) that accepts the correct number of arguments.
* If the _iterables_ passed to `map()` are of different _lengths_, `map()` will stop when the shortest iterable is exhausted.

<h3>Simulating matrices</h3>

Python can simulate a `matrix` using `linked lists`. 

→ Although Python does not have a built-in matrix data type, you can create a two-dimensional (or multidimensional).

→ Each element of the main list is a list (or other data structure, such as another list) representing a row of the headquarters.

```
array = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
```

→ This makes it possible to simulate some actions that occur in the matrices:

```
array[0][0] = 1 # updated the value of the initial row and column
array[0].append([0,0,0]) # adding another row with 3 zeros in the matrix
for row in array: # adding the value 1 to each row of the array
    row.append(1)
for i, row in enumerate(array): 
    for j, value in enumerate(row):
        print(value) # printing the array values
```

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
content = ""
with open("file_name.txt", "r") as file:
    content = file.read()
```

➡️ <a href="https://www.w3schools.com/python/python_ref_file.asp" target="_blank">More about file methods...</a>
