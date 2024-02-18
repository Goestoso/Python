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

- `__init__:` special method called ___constructor___(executed automatically when a new object is created);
- `(self):` the _self_ attribute is used to refer to the current object;

```
def __init__(self, name, age):
    self.name = name #atribute
    self.age = age #atribute
```

<h2>Python UML</h2>

<img src="https://github.com/Goestoso/Python/assets/132786474/da1961ac-9e68-4f7d-bdb5-d53760519d40" alt="UML Python" width="1000" height="500">

> `None:` used to dereference an object.
> <br>
>object = None

- It is possible to access the _object_ attributes using `.`

```
object.attribute1 #acessing the attribute
```

<h3>SOLID</h3>

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

<h3>Class Methods</h3>

→ They are functions associated with objects.

```
object.method() #acessing the class method
```

- When creating methods in a class, the first parameter must be `self`;
- Python automatically ___passes the instance___ as the method's first argument;

 <h3>Encapsulation</h3>
 
🔐 Encapsulation in Python is not as strict as it does not use specific keywords.

🧐 It is achieved through ___conventions___.

 - A `_` indicates that the method is "protected",that is, it should not be accessed outside the class or subclass, but it is ___possible___.

```
self._attribute_protected
#_Class_attribute_protected
```

- Two `__` indicates that the attribute or method is "private", python internally renames the name to avoid collisions.

```
self.__attribute_private
#_Class__attribute_private
```

> `@property:` in python it is not common to use getters and setters, however you can use the _property_ to change this behavior.

