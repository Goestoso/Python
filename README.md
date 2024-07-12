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
    self.name = name #atribute
    self.age = age #atribute
```

> `None:` used to dereference an object.
> <br>
>object = None

<h3>Instance Methods</h3>

→ They are functions associated with objects.

```
object.method() #acessing the instance method
```

- When creating instance methods in a class, the first parameter must be `self`;
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

> `class constant attribute:` variables whose values ​​must not be changed after initial assignment.

```
class Class:
CONSTANT_ATTRIBUTE = "value"
```

> `class methods:` to access attributes, working in one's own class (receiving the class itself as the first argument).

```
class Person:
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    @classmethod
    def copy_person(cls, person): #cls is a convention for the class instance (1st argument)
        return cls(person.name, person.year_of_birth) # calls the class constructor
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
    if self == object: return True # if the compared object is the same as the current instance
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

- 👁️ __Curiosity:__ in Python, methods can return an amount of __n__ elements (the return comes in tuple format).

```
from typing import Any, Tuple
def show_properties(self, variable: Any) -> Tuple[str, int]: # indicates that the method must receive any value and that it will return a str and an int
    return repr(variable), len(variable)
```

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

→ `try-except:` is used to catch and handle exceptions.

- It allows monitoring a block of code using `try` and catching possible exceptions using `except`.
- `as:` to assign the textual output of the exception, the keyword as (alias) is used and, by convention, the letter `e`.

```
try:
    # monitoring block
except Exception as e: # catching all exceptions
    print(e)
```
> Optional blocks:

- `else:` this block is _only executed if no error occurs in the `try` block_.
- `finally:` is _always executed_, regardless of whether errors have occurred or not.
> `finally` blocks allow the completion of tasks.
<br>

> General order of the exception handling block:

```
try:
    # try block
except:
    # except block
else:
    # else block
finnaly:
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