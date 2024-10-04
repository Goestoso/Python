<h1>Object-Oriented Programming</h1>
  
<div style="display: flex; justify-content: center; gap: 40px;">
<figure style="margin-right: 20px;">
  <img align="center" alt="Goes-Python" height="100" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg"  >
   <figcaption><b>Studies on OOP in Python.</b></figcaption>
</figure>
</div>

<br>

> `Procedural Programming:` is a form (paradigm) concentrated in functions and procedures (sequentially).

```
def calculate_average(list):
    sum = sum(list)
    return sum/len(list)
```

* It is suitable for simple tasks or _scripts_.

> `OOP:` is centered on _objects_, which can ***encapsulate*** data and related functionalities.

```
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I name is {self.name} and I am {self.age} years old.")
```

* Useful for more complex projects, where it is possible _to model the system_ in terms of objects interacting with each other.

> ___General structure of object memory allocation:___

<img src="https://github.com/Goestoso/Python/assets/132786474/7ef4b42f-2cb9-4054-8583-333e8c4f8c88" alt="UML Python" width="1000" height="500">

- 🔋 `STACK:`
- memory on the stack is allocated and deallocated __automatically__ (generally with function calls, variable declaration and replacement of variable values...);
- when a function is called, the space needed for local variables is allocated on the stack, and when the function ends, this space is freed;
- allocating and deallocating memory on the stack is very _fast_ because it only involves moving a pointer;
<br>

- 🗻 `HEAP:`
- memory on the heap is allocated and deallocated __dinamically__ (not limited by the scope of a function, as in creating a new object with its attributes and methods);
- variables allocated on the heap remain allocated until they are explicitly deallocated by the programmer and this allows data to persist beyond the scope of the function that created it.
- allocating and deallocating memory on the heap is _slower_ compared to the stack due to the need to manage free memory.
  
<h2>Classes and Objects</h2>

> `Class:` A class is like a template or a blueprint for creating _objects_.

→ When declaring the name of a class in Python, you must adopt ___CamelCase___.

> `Object:` an object is an instance of a class.

```
class Book:
    pass #keyword to ignore classes and methods
book1 = Book() #creating the object calling the class
#reference
```

- `__init__:` special ___dunder method___ called ___constructor___ (executed automatically when a new object is created);
- `(self):` the _self_ attribute is used to refer to the current object;

```
def __init__(self, name, age):
    self.name = name # instance attribute
    self.age = age # instance attribute
```

> `None:` used to dereference an object.
> <br>
>object = None

<h3>Instance Methods</h3>

→ They are functions associated with objects.

```
value = object.method() # acessing the instance method
```

- When creating instance methods in a class, the first parameter must be `self`;

```
def method(self):
    return f"Hello {self.name}, you are using an instance method."
```

- Python automatically ___passes the instance___ as the method's first argument;

<h3>Static Methods</h3>

> `static method:` are methods that do not depend on a object reference, generally aimed at generalization.

```
@staticmethod
def static_method():
    return "value"
```

- Static methods can be called using the _class reference_.

> Class`.static_method()`

<h3>Class Methods</h3>

> `class attribute:` is a variable that is associated with the class as a whole, rather than with individual instances of that class.

```
class Class:
class_attribute = "value"
```

> `class constant attribute:` attributes whose values ​​must not be changed after initial assignment.

```
class Class:
    CONSTANT_ATTRIBUTE = "value"
```

> `class methods:` to access class attributes, working in one's own class (receiving the class itself as the first argument).

```
class Person:
    list_people = list() # class attribute
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth
        Person.list_people.append(self) # add the current instance to the list of people

    @classmethod
    def show_people(cls): #cls is a convention for the class instance (1st argument)
        return "\n".join(f"{str(person.name)}, str(person.year_of_birth)" for person in cls.list_people)

    @classmethod
    def copy_person(cls, person): 
        return cls(person.name, person.year_of_birth) # calls the class constructor and create a new instance
```
- Class methods can also be called using the _class reference_.

> Class`.class_method()`

<h3>Dunder methods (double underscore methods)</h3>

→ Refers to special (magic) methods in python and are defined like this: `__method__()`.

> `__str__()`: responsible for representing the object for the end user in str format.

```
def __str__(self):
    return 'value'
```

> `__repr__()`: used to show a representation of the object that helps the programmer.

```
def __repr__(self, object):
    return f"Class(attribute1={object.attribute1}, attribute2={object.attribute2)"
```

- It is possible to access the _object_ attributes using `.`

> `__eq__()`: responsible for checking whether two objects are equal.

```
def __eq__(self, object):
    if self is object: return True # if the compared object is the same as the current instance
    if isistance(object, self.__class__): # checks if the object is from the same instance of the class
        return self.attribute1 == object.attribute1 and self.attribute2 == object.attribute2
    return False

object = Class("value1", "value2")
other = Class("value1", "value2")
print(object == other) # True
```

> `__ne__()`: responsible for checking whether two objects are not equal.

```
def __ne__(self, other):
        return not self.__eq__(other)
object = Class("value1", "value2")
other = Class("value2", "value1")
print(object != other) # True
```

> `__lt__()`, `__le__()`, `__gt__()` and `__gt__()`: are comparison operators that allow us to evaluate relationships between values (`l`: less, `g`: greater, `e`: equal, `t`: than).

```
def __gt__(self, object): # the form of comparison is chosen by implementation
    if len(self) > len(object):  
        return True
    elif  len(self) == len(object):
        return self > object
    return False

object = Class("value")
other = Class("other_value")
print(other > object) # True
```

➡️ <a href="https://www.geeksforgeeks.org/dunder-magic-methods-python/" target="_blank">More about dunder methods...</a>

<h2>SOLID</h2>

→ There are some properties or principles that were defined by Robert C. Martin to create a _class_:

- `S:` Single responsibility principle;
- `O:` Open/closed principle;
- `L:` Liskov substitution principle;
- `I:` Interface segregation principle;
- `D:` Dependency inversion principle;

> `S:` just a responsibility per class. <br>
> `O:` classes open for extension but closed for modification. <br>
> `L:` derived classes must be replaceable by their base classes, in other words, if S is a subclass of T, then objects of type T can be replaced by objects of type S without breaking the expected behavior of the program. <br>
> `I:` interfaces must be specific to the clients that use them, promoting code cohesion. <br>
> `D:` high-level modules should not depend on low-level modules, they should both depend on abstractions.

 <h3>🔒 Encapsulation</h3>
 
🔐 Encapsulation in Python is not as strict as it does not use specific keywords.

🧐 It is achieved through ___conventions___.

 - A `_` indicates that the method is "protected", that is, it should not be accessed outside the class or subclass, but it is ___possible___.

```
self._attribute_protected
#_Class_attribute_protected
```

- Two `__` indicates that the attribute or method is "private", python internally renames the name to avoid collisions.

```
self.__attribute_private
#_Class__attribute_private
```

> `protected method:` created to be executed only within the class and its subclasses.

```
def _protected_method(self, var):
    #block of protected code
```

> `private method:` created to be executed only within the class.

```
def __private_method(self, var):
    #block of private code
```

🔏 `__` or `_` → in Python, the underscores "__" are transformed into another variable and this is called ___name mangling___.

<h4>Properties (🔑Getters and Setters🛠️)</h4>

→ Methods that give access are named _properties_, indicating to Python the intention to have access to the attribute or to modify it.

> `@property:` in python it is not common to use getters and setters, however you can use the _property_ to change this behavior.

```
@property #to access
def attribute(self): # object.attribute to access
    return self.__attribute
@attribute.setter #to modify
def attribute(self, new_attribute): # object.attribute = "new value" to modifiy
    object.__attribute = new_attribute
```

<h3>👑 Heritage</h3>

👑 Allows you to create child classes that inherit attributes and methods from a parent class.

```
class Father:
    def __init__(self, var):
        self.__attribute = var.title() #capitalize the first letter
    #@property
    #... father's attributes
class Daughter(Father): #Daughter inherits from father
    def __init__(self, var):
    #... daughter's attributes
```

<img src="https://github.com/Goestoso/Python/assets/132786474/2144a292-4de9-4950-9571-6b878f5768e9" alt="Heritage" align="center">

<br>
<br>

> `super():` function that allows you to call a method in the parent class, helping to avoid code duplication.

```
#class
    #def
        super().__init__(attributes)
```

- Python supports inheritance from more than one class.
- The concept is to ___extend___ the mother class to the subclasses.
- This way it is possible to have _flexibility_ in the code.

```
class Father:
    # father attributes and methods
    pass
class Mother:
    # mother attributes and methods
    pass
class Daugther(Father, Mother): # multiple inheritance
    # Daughter inherits from father and mother
    pass
```

<h3>🔂 Polymorphism</h3>

🔁 Allows objects of different classes to be treated uniformly.

🔃 An object can be referenced through a parent class, but still execute its child class-specific methods.

<img src= "https://github.com/Goestoso/Python/assets/132786474/ba579334-dc12-4a36-9c77-d9881fc5cf42" alt="Polymorphism" align="center">

<br>
<br>

<h4>📝 Overriding</h4>

- In Python, method `overriding` is ___implicit___, just define a method with the same name in the child class that it will replace in the parent class.

> Father → def print_method(self):
> <br>
> Daughter → print_method(self):

- ___Example___:

```
class Animal:
    def make_sound(self):
        return "Animal sound"

class Dog(Animal): 
    def make_sound(self): #Overriding
        return "Woof!"

class Cat(Animal):
    def make_sound(self): #Overriding
        return "Meow!"

# Creating instances of classes
dog = Dog()
cat = Cat()

# Calling the animal_sound function with different instances
print(Dog.make_sound())  # Output: Woof!
print(Cat.make_sound())  # Output: Meow!
```

<h4>🏋️‍♂️ Overload</h4>

- In Python, the method `overload` depends on the number of parameters and their types to form a ___signature___.

> def overhead_method(self, variable=None): # passing the parameter to the method is optional
> <br>
>    return variable

- Python only considers the name in the signature, ___not the types___, therefore, it is not possible to have multiple methods with the same name and different parameter types.

```
class Person:
    @staticmethod
    def show_welcome_message(person="friend"):
        return f"Hello, {person}!"

# Calling the show_welcome_message with different parameters
print(Person.show_welcome_message()) # Output: Hello, friend!
print(Person.show_welcome_message("John")) # Output: Hello, John!
```

<h4>🧩 Generic</h4>

- In Python, all methods are `generic` and allow different ___data types___, as typing is done through the value that their parameter receives.

> def generic_method(self, variable): # the variable can receive different types of data like str, int, float, bool, objects...
> <br>
>    return type(variable)

- However, to facilitate readability and understanding of attributes and methods, it is recommended to use the `typing` built-in module.

```
from typing import TypeVar, List, Tuple
number = TypeVar("number") # indicating the definition of an generic attribute of type number
coordinates: Tuple[float, float] = (10.0, 20.0) # indicating the definition of an attribute of type tuple of two floats
def sum_two_values(self, number1:int|float, number2:int|float) -> number: # indicates that the method must receive two variables of type int or float and that it will return a number
    return number1 + number2
def show_welcome_message(self, person:str="friend") -> str: # indicates that the method must receive a str and that it will return a str
    return f"Hello, {person}!"
def school_average(self, grades:List[float]) -> float: # indicates that the method must receive a list of floats and that it will return a float
    return sum(grades) / len(grades)
```

<details>

<summary>👁️‍🗨️ Curiosity</summary>

- In Python, methods can return an amount of __n__ elements (the return comes in tuple format).

```
from typing import Any, Tuple
def show_properties(self, variable: Any) -> Tuple[str, int]: # indicates that the method must receive any value and that it will return a str and an int
    return repr(variable), len(variable)
```

</details>


<h2>❌ Exceptions</h2>

→ These are events that occur during the execution of a program and can be handled to avoid abrupt interruption.

- `✅ Checked exceptions:` which must be handled by the programmer, such as type errors, which are detected before the program is executed (during `compilation`).
- `✖️ Unchecked exceptions:` which do not need to be handled explicitly (occur during program execution).

⚠️ `Important:` since Python is an `uninterpreted language` (the typing of variables occurs at runtime), ___all exceptions from a `.py` program are unchecked___.

<h3>❌👑 Exception hierarchy</h3>

→ Exceptions are treated as `class objects`.

- `BaseException:` all exceptions inherit from the `BaseException` class.

> Exceptions diagram:

![exceptions](https://github.com/user-attachments/assets/4bb0f6f0-9499-4f4a-bbba-62fb984dcd58)

- The exception names help you understand their context.
- For example `KeyboardInterrupt` occurs when pressing the `Ctrl + C` keys during program execution.
- Another example is the `ArithmeticError`, which occurs when trying to perform invalid mathematical operations (such as division by zero)

> Custom exceptions:

- `Exception:` in addition to built-in exceptions, it is also possible to define custom exceptions by creating classes derived from the `Exception` class.

```
class MyException(Exception):
    def __init__(self, msg:str):
        self.msg = msg
    def __str__(self):
        return f"Error: {self.msg}"
```

<h3>🩺 Exception block</h3>

→ `try-except:` is used to catch and handle specific or generic exceptions.

- It allows monitoring a block of code using `try` and catching possible exceptions using `except`.
- `as:` to assign the textual output of the exception, the keyword as (alias) is used and, by convention, the letter `e`.

```
try:
    # monitoring block
except Exception as e: # catching all exceptions
    print(e)
```
→ `try-finally:` is used to ensure that a given piece of code is executed regardless of what happens inside the `try` block.

```
try:
    # monitoring block
finally: # ensuring that this block of code will be executed
    # finally block
```

- `finally:` is _always executed_, regardless of whether errors have occurred or not.
> `finally` blocks allow the completion of tasks.
<br>

> Optional block:

- `else:` this block is _only executed if no error occurs in the `try` block_.
> ___The `else` block depends on an `except` block to function___

```
try:
    # monitoring block
except Exception as e: # catching all exceptions
    print(e)
else: # if no exception is caught
    print("Worked")
```

> General order of the exception handling block:

```
try:
    # try block
except:
    # except block
else:
    # else block
finally:
    # finnaly block
```

<h3>⤴️ Exception Throwing and Stack 🔋</h3>

- `raise` _Execption(msg:str)_: to explicitly _signal that an exception should be thrown_ and optionally caught within the exception handling block.
> Example without exception handling block:
```
raise RuntimeError("Ooops, an error occurred here...")
```
>  Example with exception handling block:
```
try:
    raise RuntimeError("Ooops, an error occurred here...")
except RuntimeError as e: # catching the thrown error
    print(f"RuntimeError: {e}")
```

- `traceback:` is the _exception stack trace_ module, useful for obtaining the sequence of function or method calls that led to an error.
> Example:
```
from traceback import format_exc

try:
    error_function()
except:
    err = format_exc() # converts the stack trace to a str
    print(err)
```

<h2>🧱 Abstract data types</h2>

→ An `Abstract Data Type (ADT)` is a mathematical model that encapsulates data and functions to manipulate it.

- A TAD has two main parts:
> `Stored Data`: Represents the values ​​that we want to manipulate (can be stored in _variables_, _vectors_, _pointers_, etc.).
> <br>
> `Functions (Operations)`: Implement procedures that act on the encapsulated data. These functions are called _operations_, _methods_, or _services_.

- `Simple (Primitive) Data Types`:
> Simple types (such as `int`, `float`, `str`, and `bool`) represent individual values.
> <br>
> They abstract away underlying implementation details (like the binary representation of an integer) and allow us to work with these values ​​in a convenient way.
> <br>
> For example, when we use an `int`, we ___don't need to worry about how it is stored in memory; we just use their values___.

- `Abstraction`:
> Abstraction is the process of ___simplifying and hiding complex details___, allowing us to focus only on the relevant aspects.
> <br>
> Both `primitives` and `ADTs` use abstraction to make code more readable and manageable.

<h3>🔡🔢 Arrays</h3>

→ Array is a data structure that ___statically___ stores a collection (`vectors` or `arrays`) of elements of the same type, these elements can be _numbers_, _strings_, _objects_ or _any other data type_.

> 🔢 The `NumPy` module is a powerful tool for working with vectors, matrices and numerical calculations in Python.

- To install `NumPy` you can use `pip` package manager:
```
pip install numpy
```
- Then, in your code, import `NumPy`:
```
import numpy as np # using alias to simplify the name 'numpy'
```
<h4>Vectors (One-Dimensional Arrays)</h4> 

> Example of a vector with 5 positions (remembering that ___arrays always start at position 0___):

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|

- Vectors are one-dimensional arrays, that is, they have only one dimension. They are an ordered sequence of elements of the same type.
- Generally, vectors are used to store a collection of related values. For example, a vector might contain a student's grades in different subjects or the prices of products in a catalog.
- Vectors have a single index to access their elements. The first element usually has index 0, the second has index 1, and so on.

```
vector = np.empty(shape=5, dtype=int) # creating an empty int vector with size 5
vector = np.array([1,2,3,4,5]) # creating a vector with given numbers
vector = np.zeros(5) # creating a vector with five zeros
vector = np.ones(5) # creating a vector with five ones
vector[4] = 0 # accessing and changing the value of a specific index of the vector
for element in vector: # iterating the vector
    print(element)
```
<h4>Matrices (Multi-Dimensional Arrays)</h4>

> Example of a matrix with 3 rows and 5 columns (remembering that ___arrays always start at position 0___):

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 |

- Matrices are two-dimensional or multi-dimensional arrays, that is, they have two or more dimensions: rows, columns, depths, etc.
- A matrix is ​​essentially a rectangular table of elements, where each element is located in a specific position defined by indices (in two-dimensional arrays: row and column, three-dimensional arrays: row, column and depth, etc.).
- Matrices are often used to represent tabular data such as spreadsheets, images (where each pixel is an element of the matrix), or systems of linear equations.

```
matrix = np.empty(shape=(3,5), dtype=int) # creating an empty int 3x5 matrix
matrix = np.zeros((3,3)) # creating a 3x3 matrix with zeros
matrix = np.ones((4,4)) # creating a 4x4 matrix with ones
matrix = np.array([[1,2,3],[4,5,6]]) # creating a 2x3 matrix with given numbers
matrix[1,2] = 0 # accessing and changing the value of a specific row and column of the matrix
for row in matrix: # iterating the matrix (simple way)
    for element in row:
        print(element)
squares = matrix ** 2
print(squares) # using vectorization to calculate the square of elements
for element in np.nditer(squares): # iterating the matrix (other simple way)
    print(element)
for (row, column), element in np.ndenumerate(matrix): # iterating the matrix (by indeces)
    print(f"row ({linha}, column {coluna}): {element}")
reshape = np.reshape(squares, (3,2)) # by changing the shape of the matrix, the total number of elements must be the same in both the old (2x3) and new matrix(3x2)!
print(reshape)
print(np.transpose(matrix)) # returns transposed of the matrix
concatenate_matrix = np.concatenate(matrix, squares, 0) # concatenates matrices along the specified axis, 0 for rows and 1 for columns
print(concatenate_matrix)
new_sizes = np.pad(matrix, pad_width=1, mode='constant', constant_values=0) # adding 1 unit padding to all edges of the matrix with constant values
print(new_sizes)
new_sizes = np.pad(matrix, pad_width=2, mode='symmetric') # adding 2-unit symmetrical padding
print(new_sizes)
new_sizes = np.pad(matrix, pad_width=1, mode='edge') # adding replicated padding (repeating edge values) of 1 unit
for i in range(new_sizes.shape[0]): # iterating the matrix (using shape to obtain the rows of the matrix)
    for j in range(new_sizes.shape[1]): # iterating the matrix (using shape to obtain the columns of the matrix)
        print(matrix[i,j])
for index in np.ndindex(concatenate_matrix.shape): # Getting all possible indexes in the array
    row, column = index # index returns a tuple of two values ​​and here its capturing the first in row variable and the second in column variable
    element = concatenate_matrix[row, column]
    print(f"Row ({row}, column {column}): {element}")
```

<h3>🔡↔️🔢 Dynamic Arrays</h3>

→ A `dynamic array` is a _data structure_ that __can grow or shrink__ as needed during program execution.
- The central idea is that, ___unlike static arrays (with a fixed size)___, ___dynamic arrays can be resized___ to accommodate more elements or free up space when necessary.

💡 Type `list` is considered a dynamic array!
> We can add elements using the `append()` method or the concatenation (`+`) operation.
> <br>
> We can remove elements using the `remove()` method or the `del` keyword.
> <br>
> The `list` size can grow or shrink as needed.

- ⚠️ It is possible to create custom dynamic arrays by building classes that implement the functions of the `NumPy` module!

> 👉 Using the ___dunder methods___ `__iter__`, `__next__`, `__getitem__`, `__setitem__`and `__len__` it is possible to create your own dinamic array, like this [custom array example](https://github.com/Goestoso/Python/blob/oop/my_array.py).

<details>

<summary>⏯️ yield and next ➡️</summary>

- `yield` is a _keyword_ in Python that is used in a function to turn that function into a ___generator___.
- Instead of returning a value and ending the function's execution, `yield` returns a value and "pauses" the function's execution, maintaining its state so that it can continue where it left off the next time it is called.

> `return` vs `yield`:
- `return`: when a function reaches a return statement, ___it returns a value and ends execution___.
- `yield`: when a function reaches a yield statement, ___it returns a value and "pauses" execution___. The next time the generator is iterated, execution continues where it left off after the yield.

> `yield` use example:

```
def __init__(self, capacity=None):
        self.__lastPos = -1
        self.__data = np.empty(shape=capacity, dtype=int) if capacity else np.empty(shape=10, dtype=int)

def __iter__(self):
        for i in range(self.__lastPos + 1):
            yield self.__data[i]
```
- `next` is a ___built-in function___ and a ___dunder method___ in Python that retrieves the next item from an iterator.
- When you use next on an iterator, it returns the next item in the sequence until there are no more items, at which point it raises the StopIteration exception.

> `yield` vs `next`:
- `yield`: when you need a simple and efficient iterator. It is ideal for most iteration cases and is easier to implement and understand.
- `next`: when you need finer control over iteration, such as in cases where the state of the iterator needs to be preserved between iterations in a complex way. It is useful in advanced situations where `yield` does not provide the necessary flexibility.

> `next` use example:

```
    def __init__(self, my_array):
            self._my_array = my_array
            self._index = 0

    def __iter__(self):
            return self

    def __next__(self):
        if self._index <= self._my_array.__lastPos:
            result = self._my_array.__data[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration
```

</details>

<h3>🖇️ Linked Lists</h3>

→ It is a linear data structure consisting of a sequence of elements called `nodes`.

> 🪢 Nodes:

```
                 Double Node
+-------+      +-----------+      +-------+
|  Prev |<-----|   Data    |----->|  Next |
+-------+      +-----------+      +-------+
```

- Each `node` contains two main components: ___Data___ and ___Pointer___.
- ___Data___: the information _stored_ in the `node`.
- ___Pointer___: or ___reference___, is a link to the ___next___ or ___previous___ `node` in the sequence.

> Characteristics:

- ___📥 Non-Contiguous in Memory___: unlike _arrays_ or _dynamic arrays_, the elements of a _linked list_ are not stored in contiguous memory locations, each node can be anywhere in memory, and the ___pointer___ connects these `nodes`.
- ___🐛 Dynamic Size___: the size of a _linked list_ can grow or shrink as needed, without the need for reallocation or resizing as occurs in arrays.
- ___🏗️ Ease of Insertion/Removal___: inserting or removing elements at the beginning or in the middle of a _linked list_ can be done efficiently, as it does not require moving the elements, just modifying the pointers.
- ___➕ Benefits___: efficient insertions and removals plus dynamic memory usage.
- ___➖ Disadvantages___: sequential access and memory overhead.

> Types:

- ___➡️ Singly Linked List___: each `node` points only to the ___next___ `node` in the sequence.

```
 ↪ +--------+     +--------+     +--------+     +--------+
    | Node  |      | Node  |      | Node  |      | Node  |
    +-------+      +-------+      +-------+      +-------+
    |  Data |      |  Data |      |  Data |      |  Data |
    +-------+      +-------+      +-------+      +-------+
    |  Next |----->|  Next |----->|  Next |----->|  Next |-----> null
    +-------+      +-------+      +-------+      +-------+
```
- ___↔️ Doubly Linked List___: each `node` contains two pointers, one to the ___next___ `node` and one to the ___previous___ `node`.

```
 ↪ +--------+      +--------+      +--------+      +--------+
    | Node  |       | Node  |       | Node  |       | Node  |
    +-------+       +-------+       +-------+       +-------+
    |  Data |       |  Data |       |  Data |       |  Data |
    +-------+       +-------+       +-------+       +-------+
    |  Next |<----->|  Next |<----->|  Next |<----->|  Next |-----> null
    +-------+       +-------+       +-------+       +-------+
```
- ___🛞 Circular Linked List___: in the circular _linked list_, ___the last `node` points to the first `node`___, forming a __cycle__.

```
   +--------+      +--------+      +--------+      +--------+
    | Node  |       | Node  |       | Node  |       | Node  |
    +-------+       +-------+       +-------+       +-------+
    |  Data |       |  Data |       |  Data |       |  Data |
    +-------+       +-------+       +-------+       +-------+
    |  Next |<----->|  Next |<----->|  Next |<----->|  Next |
    +-------+       +-------+       +-------+       +-------+
       ^                                                 |
       |                                                 v
       +-------------------------------------------------+
```

<h3>👥 FIFO</h3>

→ A `FIFO` (___First In, First Out___), or simply ___queue___, is a data structure where __the first element to be inserted is the first to be removed__.

> Characteristics:

- ___🔢 Processing Order___: Elements are processed in the order in which they were inserted. The first element to be inserted (the "first in") is the first to be removed (the "first out").

- ___🏗️ Insertion and Removal___: Insertion of elements is done at the end of the queue and removal is done at the beginning of the queue.

- ___🔁 No Rollback___: Once an element is removed from the queue, it cannot be reclaimed. The order of elements cannot be reversed within the default queue.

> ↔️ Main Operations:

- ___Enqueue___: Add an element to the end of the queue.
- ___Dequeue___: Remove the element from the front of the queue.
- ___Front___: Access the element at the front of the queue without removing it.
- ___Rear___: Access the element at the rear of the queue without removing it.
- ___Check if it is empty___: Check if the queue contains elements.
- ___Size___: Get the number of elements in the queue.
- ___Sequential Access___: Elements are accessed in sequence, without the possibility of directly accessing an element in the middle of the queue (as in an `array` or `list`).

> ⚙️ Structure:

```
🖇️ Linked List Structure:
    +--------+      +--------+      +--------+      +--------+
    |  Node  | ---->|  Node  | ---->|  Node  | ---->|  Node  |
    +--------+      +--------+      +--------+      +--------+
    |  Data  |      |  Data  |      |  Data  |      |  Data  |
    +--------+      +--------+      +--------+      +--------+
    |  Next  | ---->|  Next  | ---->|  Next  | ---->|  NULL  |
    +--------+      +--------+      +--------+      +--------+
       ^                                                 ^
       |                                                 |
     Front                                              Rear

Enqueue: Add a node at the Rear
Dequeue: Remove a node from the Front

🔢 Array Structure:
   +---------------------+ 
   |[Data|Data|Data|Data]| 
   +---------------------+
      ^               ^            
      |               |                                 
    Front            Rear

Enqueue: Add an element at the Rear
Dequeue: Remove an element from the Front                                
```

- A ___queue___ can be implemented with both `arrays` and `linked lists`, both approaches have their advantages and disadvantages depending on the prevailing context and operations.

<h3>🔋 LIFO</h3>

→ `LIFO` (___Last In, First Out___), or ___stack___, is a data structure where __the last element to be inserted is the first to be removed__.

> Characteristics:

- ___🔢 Processing Order___: The last element added to the stack is the first to be removed (Last In, First Out).
- ___🔐 Restricted Access___: Stack elements can only be added or removed from the top.
- ___🔁 No Rollback___: Once an element is removed from the stack, it cannot be directly recovered except by pushing it back onto the stack.

> Main Operations:

- ___Push___: Add an element to the top of the stack.
- ___Pop___: Remove the top element from the stack.
- ___Peek/Top___: Access the top element of the stack without removing it.
- ___Bottom___: Access the bottom element of the stack without removing it.
- ___Check if it is empty___: Check if the stack is empty.
- ___Size___: Return the number of elements in the stack.
- ___Sequential Access___: Elements are accessed in sequence, without the possibility of directly accessing an element in the middle of the stack (as in an `array` or `list`).

> ⚙️ Structure:

```
🖇️ Linked List Structure:
    +--------+      +--------+      +--------+      +--------+
    |  Node  | ---->|  Node  | ---->|  Node  | ---->|  Node  |
    +--------+      +--------+      +--------+      +--------+
    |  Data  |      |  Data  |      |  Data  |      |  Data  |
    +--------+      +--------+      +--------+      +--------+
    |  Next  | ---->|  Next  | ---->|  Next  | ---->|  NULL  |
    +--------+      +--------+      +--------+      +--------+
       ^                                                 ^
       |                                                 |
      Bottom                                            Top

Push: Add a node at the Top
Pop: Remove a node from the Top

🔢 Array Structure:
   +---------------------+ 
   |[Data|Data|Data|Data]| 
   +---------------------+
      ^               ^            
      |               |                                 
     Bottom          Top

Push: Add an element at the Top
Pop: Remove an element from the Top                                
```

- A ___stack___ can be implemented with both `arrays` and `linked lists`, both approaches have their advantages and disadvantages depending on the prevailing context and operations.

<h3>🔁 Recursion</h3>

→ `Recursion` is a programming technique where ___a function is called repeatedly until it reaches a base condition___, which interrupts the calling cycle.

> ➗ Divide and Conquer ✖️:

→ `Recursion` is a powerful tool that can simplify the solution of complex problems by breaking them down into smaller, more manageable subproblems.

> 🤔 What is Recursion?

→ In simple terms, `recursion` is a function that calls itself. For recursion to work correctly, it is necessary to define two fundamental parts:

- ___🦶 Base Condition___: The condition that stops recursion, preventing the function from being called indefinitely. Without a base condition, the code would result in infinite recursion and eventually a stack overflow error.

- ___🔁 Recursive Call___: The part where the function calls itself, moving towards the base condition.

> ⚙️  How does Recursion Work?

→ When a ___recursive function___ is called, the following happens:

- 🆕 Each recursive call creates a new execution context on the call stack, containing local variables and the current state of the function.
- 🔄️ The function keeps calling itself until the base condition is satisfied.
- 🛑 When the base condition is met, the recursive calls begin to "return" one by one, resolving from the innermost to the outermost call.

> 🔎 When to Apply Recursion?

→ `Recursion` is particularly useful in situations where a problem can be naturally divided into similar subproblems. Common examples include:

- ___🔀 Divide and conquer problems___: As in sorting algorithms (_mergesort_, _quicksort_).
- ___🔢 Problems that can be defined recursively___: How to calculate the _factorial_ of a number, _Fibonacci_, or _sums_ of numbers.
- ___👑 Hierarchical data structures___: Like `trees` and `graphs`, where each _subtree_ is a complete _tree_.
- ___🧩 State Exploration___: As in _maze_ or _puzzle_ solutions.

> ➕ Advantages of Recursion:

- ___👁️ Clarity and Simplicity___: For problems that are naturally recursive, the recursive solution may be more intuitive and easier to understand.
- ___➗ Natural Division of the Problem___: Some problems, such as those involving __hierarchical structures__ (`trees`, `graphs`), are more easily solved with recursion.

> ➖ Disadvantages of Recursion:

- ___💾 Memory Usage___: Each recursive call adds a new entry to the call stack, which can lead to a stack overflow error if the recursion depth is too large.
- ___⏩ Efficiency___: Recursion can be less efficient than iterative solutions, especially if many recursive calls repeat calculations (as in the Fibonacci sequence example without optimizations).

> ❌ When to Avoid Recursion?

- ___⬇️ Deep Recursion___: If the number of recursive calls is very large, it may be more efficient to use an iterative approach to avoid __stack overflow__ (known as the `RecursionError exception`).
- ___➿ Excessive Repetition___: If recursion leads to an excessive number of repeated calculations, it may be necessary to optimize with techniques such as memoization (storing results of previous calculations).

> 🤼 Recursion versus Iteration:

→ `Recursion` and `iteration` are two approaches to solving repetitive problems. Some situations may be more naturally resolved with recursion, while others may be better suited to iteration. Sometimes a recursive solution can be easier to write and understand, but an iterative solution can be more efficient in terms of performance and memory usage.

> 📝 Example:

- 🔋 Call Stack in Recursion:

```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

"""
Case fatorial(5):

factorial(5)
    └── factorial(4)
            └── factorial(3)
                    └── factorial(2)
                            └── factorial(1)
                                    └── factorial(0) = 1
                            ┌── return 1 * 1 = 1
                    ┌── return 2 * 1 = 2
            ┌── return 3 * 2 = 6
    ┌── return 4 * 6 = 24
┌── return 5 * 24 = 120

"""
```

- 🌳 Call Tree in Recursion:

```
def fibonacci(n):
    if n == 0:  # Caso base 1
        return 0
    elif n == 1:  # Caso base 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Chamada recursiva

"""
Case fibonacci(5):

fibonacci(5)
├── fibonacci(4)
│   ├── fibonacci(3)
│   │   ├── fibonacci(2)
│   │   │   ├── fibonacci(1) = 1
│   │   │   └── fibonacci(0) = 0
│   │   └── fibonacci(1) = 1
│   └── fibonacci(2)
│       ├── fibonacci(1) = 1
│       └── fibonacci(0) = 0
└── fibonacci(3)
    ├── fibonacci(2)
    │   ├── fibonacci(1) = 1
    │   └── fibonacci(0) = 0
    └── fibonacci(1) = 1
"""
```


<details>

<summary>👁️‍🗨️ Callback Function ✖️ Recursive Function</summary>

→  `Recursion` and `callback` functions are distinct concepts, but ___they both involve executing functions within other functions___.

> ⬇️ Self-reference versus Delegation ⬆️:

- `Recursion`: The function calls itself.
- `Callback`: A function is passed to and called by another function.

> 💡Purpose:

- `Recursion`: Used to solve problems that can be divided into smaller subproblems of the same type.
- `Callback`: Used to modularize code, create control flow or deal with asynchronous programming.

> ⚙️ Execution Flow:

- `Recursion`: It involves a series of calls on the stack until the base condition is reached.
- `Callback`: The function is called when an event or condition is met.
  
> 🔎 Common Usage:

- `Recursion`: Applied in algorithms such as tree search, sorting, etc.
- `Callback`: Used in events, data manipulation, and asynchronous programming.

</details>

<h3>🌳 Tree</h3>

→ `Tree` is a finite set of one or more `nodes`.

⚠️ Not to be confused with `graphs`, as these consist of a set of nodes (or vertices) and edges that connect pairs of nodes. 

> ___Every tree is a graph, but not every graph is a tree!___

* `Tree:`

```
        [A]
       / | \
     [B] [C] [D]
    / \      / \
  [E] [F]  [G] [H]
```

* `Graph:`

```
     [1] ----- [2]
      | \       |
      |  \      |
      |   \     |
     [3]   \   [4]
      |     \   |
      |      \  |
      |       \ |
     [5] ----- [6]

```
> Characteristics:

___🫚 Degree of a node___: is the number of subtrees of the node. <br>
___🪵 Degree of a tree___: is the maximum degree between the nodes in the tree. <br>
___🍃 Leaves of a node X___: are the roots of the subtrees of that node. In this case _X_ is the __Father__ of his __children__. <br>
___📍 Level of a node___: the root of the tree is said to be at level zero and if a node is at level _k_, its children are at level _k + 1_. <br>
___🏋️‍♂️ Height or depth of a tree___: is the maximum level of the nodes in the tree. <br>
___👴 Ancestors of a node___: are all nodes along the path from the root to the node. <br>
___🏕️ Forest___: set of disjoint trees. <br>
___🚶‍➡️ Path___: a sequence of distinct nodes _v1_,_v2_,...,_vk_, such that it always exists between consecutive nodes (i.e., between _v1_ and _v2_, between _v2_ and _v3_, ..., _v(k-1)_ and _vk_) the relationship "is a child of" or "is a father of" is called a ___path in the tree___. <br>
___📐 Path Length___: a path between _k_ vertices is obtained by the sequence of _k - 1_ pairs of vertices. In this case, _k - 1_ is the ___path length___.

<h4>2️⃣ Binary Tree</h4>

→ Tree in which each `node` has at most two __children__, referred to as ___left child___ and ___right child___.

> ⚙️ Structure:

```
       [1]
      /   \
    [2]   [3]
   /  \   /  \
 [4] [5] [6] [7]
```

> 🪢 Node behavior:

```
              Node
 +-------++-----------++-------+
 |  Left ||   Info    || Right |
 +-------++-----------++-------+
    /                       \
   /                         \
  °                           °

Info(or key): The value stored in the node.
Left: Reference to the subtree to the left of the node.
Right: Reference to the subtree to the right of the node.
```

> Main Operations:

- ___Inseertion___: If the node value is entered by less than the current node value, the new node is placed on the left, or if the value is greater, the new node is placed on the right. This process continues recursively until the correct location for the node is found.
- ___Search___: It starts at the root and compares the value to be searched with the value of the current node, if the value is smaller, the search continues to the left; if it is larger, continue to the right. The process continues until the value is found or there are no more nodes to traverse.
- ___Removal___: Removing a node in a binary tree has three main cases: <br>
1️⃣ - _Leaf node (no children)_: The node is simply removed. <br>
2️⃣ - _Node with one child_: The node to be removed is replaced by its only child. <br>
3️⃣ - _Node with two children_: In this case, the node is replaced by the smallest node in the right subtree (the successor) or the largest node in the left subtree (the predecessor), and the replacement node is removed from its original position.
- ___Find Min/Max___: To find the minimum value in a binary search tree (BST), just follow the pointers to the left until you find the last node, to find the maximum value, just follow the pointers to the right until the end.
- ___Check if it is empty___: Check if the binary tree is empty, if the root is `None`, the tree is empty.

> 🔀 Routes:

* `Pre-order:` <br>
1️⃣ - Visit the root. <br>
2️⃣ - The left subtree is traversed in previous order. <br>
3️⃣ - The right subtree is traversed in previous order.

* `In order:` <br>
1️⃣ - The left subtree is traversed in symmetric order. <br>
2️⃣ - Visit the root. <br>
3️⃣ - The right subtree is traversed in symmetric order.

* `Post-order:` <br>
1️⃣ - Traverse the left subtree in later order. <br>
2️⃣ - Traverse the right subtree in later order. <br>
3️⃣ - Visit the root.

```
# Pre-order example:
def to_string_pre_order(self):
    if self.is_empty():
        return "empty tree"
    return self._to_string_pre_order(self.root)

def _to_string_pre_order(self, current):
    if current is None:
        return ""
    return (str(current) + " " + 
            self._to_string_pre_order(current.get_left()) + 
            self._to_string_pre_order(current.get_right()))

# In order example:
def to_string_in_order(self):
        if self.is_empty():
            return "empty tree"
        return self._to_string_in_order(self.root)

    def _to_string_in_order(self, current):
        if current is None:
            return ""
        return (self._to_string_in_order(current.get_left()) +
                str(current) + " " +
                self._to_string_in_order(current.get_right()))

# Post-order example:
def to_string_post_order(self):
    if self.is_empty():
        return "empty tree"
    return self._to_string_post_order(self.root)

def _to_string_post_order(self, current):
    if current is None:
        return ""
    return (self._to_string_post_order(current.get_left()) + 
            self._to_string_post_order(current.get_right()) + 
            str(current) + " ")
```

> ⏳ Time Complexity (O)

→ In _search_, _insertion_ and _removal_ operations:

* ✅ `Best case:` _O(log₂n)_ <br>
📈 When the tree is balanced, at each step _half of the remaining nodes are eliminated_.

* ⚖️ `Average case:` _O(log₂n)_ <br>
📊 On average, a reasonably balanced tree is assumed, especially with _randomization_ or _readjustment_ techniques.

* ❌ `Worst case:` _O(n)_ <br>
📉 When a tree ___degenerates___, each operation may require time proportional to the number of elements, as in a linked list.

<h3>🧮 Hash Table</h3>

→ `Hash tables` are extremely efficient data structures for storing and searching data in time close to _O(1)_ on average, which makes them ideal for scenarios where fast insertion, search and removal operations are required. <br>

⚠️ ___`Hash table` is not a sequential structure___: unlike structures such as `lists`, `arrays` or `queues`, which are sequential and maintain the insertion order of elements, `hash tables` do not have a defined order for the data. Instead, data is stored in different buckets based on the value generated by a `hash function` applied to the `keys`. <br>

🔢 ___`Hash`___: is a term that refers to the result of a `hash function`, which is a mathematical function used to map arbitrary-sized data to fixed-sized values, usually integers. The value generated by this function is called a hash value or simply a `hash`.

```
# Simple Hash Function:
def simple_hash(key, table_size):
    return sum(ord(c) for c in key) % table_size

# Cryptographic Hash Functions:
import hashlib
def hash_sha256(key):
    return hashlib.sha256(key.encode()).hexdigest()

# Hash Functions for Integers:
def integer_hash(key, table_size):
    return key % table_size

# Python's Default Hash Function:
def optimized_hash(key, table_size):
    return hash(key) % table_size
```

> ⚙️ Structure:

- 🔐 `Key and Value`: The hash table stores `key-value` pairs. The `key` is used to uniquely identify each entry, while the value is the information associated with that `key`.
- 🟰 `Hash function`: To quickly find the index at which a value will be stored, a `hash function` is used. This function transforms the `key` into a number (usually a numeric index) that indicates the position in the table where the value will be stored. The `hash function` must be ___deterministic___, that is, for the same key, it will always return the same value.
- 🛗 `Buckets`: The table is divided into _n_ positions (where n is the size of the array). Each `bucket` can store one value or, in case of `collisions`, multiple values ​​associated with different `keys`.
- 💥 `Collisions`: Even with a good `hash function`, two or more `keys` can result in the same index (called a `collision`). There are techniques for resolving `collisions`, such as: <br>
1️⃣ - ___Chaining___: Each table position stores a list of entries. If two `keys` collide, both are inserted into this list. <br>
2️⃣ - ___Open addressing___: If there is a `collision`, the table searches for another available position to store the value (example: __linear probing__, which sequentially searches for the next free position).

```
+-------+-------------------+
| Index | Data (key, value) |
+-----------+---------------+
|   0   |  [("Alice", 25)]  |
|   1   |   [("Bob", 30)]   |
|   2   | [("Eve", 22), ("Joe", 35) ] <- collision, stored as list
|   3   |       []          |
|   4   | [("Charlie", 40)] |
+-------+-------------------+
            |
           \|/
+-------+-------------------+
| Index | Data (key, value) |
+-----------+---------------+
|   0   |  [("Alice", 25)]  |
|   1   |   [("Bob", 30)]   |
|   2   |   [("Eve", 22)]   | <- collision resolved by moving "Joe" to the next available slot
|   3   |   [("Joe", 35)]   |
|   4   | [("Charlie", 40)] |
+-------+-------------------+
```
> Main Operations:

- ___Insertion___: The key is passed to the hash function, which returns the index of the table where the value will be stored. If there is no collision, the value is stored directly.
- ___Search___: The key is converted into an index by the hash function. The value corresponding to that index is then returned. If there is a collision, the table needs to check the keys stored in that index (in case of chaining, for example).
- ___Removal___: The key is used to locate the index. The value is removed, and any collisions must be adjusted depending on the method used.
- ___Iteration___: To loop through all the values ​​of a hash table, the approach depends on the specific implementation of the hash table and the programming language. However, the general concept is this: you need to access all buckets, and if any bucket contains a linked list (in case there are collisions), you also need to traverse that list to ensure that all elements are visited.

> Use cases:

- 📚 `Dictionaries`: Map keys to values.
- 🕑 `Caches`: Store values ​​that can be quickly accessed through a key.
- 🔢 `Sets`: Structures that store unique items and use hashing for quick existence checks.
