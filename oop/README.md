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

<summary>👁️ Curiosity</summary>

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

> Nodes:

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
- ___Check if it is empty (is_empty)___: Check if the queue contains elements.
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
- ___Check if it is empty (is_empty)___: Check if the stack is empty.
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
