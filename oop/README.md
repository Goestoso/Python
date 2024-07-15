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

<h3>Dunder methods (double underscore methods)</h3>

→ Refers to special methods in python and are defined like this: `__method__()`.

> `__str__():` responsible for representing the object in textual form (string).

```
def __str__(self):
    return 'str'
```

> `__repr__():` used to show a representation that helps in debugging or logging a code.

```
list = [1, 2, 3, 4, 5]
print(repr(list)) # [1,2,3,4,5]
#print how the object is represented
```

➡️ <a href="https://www.geeksforgeeks.org/dunder-magic-methods-python/" target="_blank">More about dunder methods...</a>


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

<h4>Properties</h4>

→ Methods that give access are named _properties_, indicating to Python the intention to have access to the object.

```
@property
def attribute(self): #console object.attribute, it doesn't need of ()
    return self.__attribute
@attribute.setter
def attribute(self, new_attribute):
    object.__attribute = new_attribute
```

> `private method:` created to be executed only within the class.

```
def __private_method(self, var):
    #block of private code
```

> `static method (class):` are methods that do not depend on a reference, generally aimed at generalization.

```
@staticmethod
def static_method():
    return "value"
```

> `class attribute:` is a variable that is associated with the class as a whole, rather than with individual instances of that class.

```
class Class:
static_attribute = "value"
```

<h3>Heritage</h3>

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

> `__` or `_` → in Python, the underscores "__" are transformed into another variable and this is called ___name mangling___.

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

> `class methods:` `@classmethod` to access class attributes, within instance methods, using `__class__`.

```
#class
    @classmethod
        def info(cls): #cls is a convention for the class instance (1st argument)
            #return
```

<h3>Polymorphism</h3>

🔁 Allows objects of different classes to be treated uniformly.

🔃 An object can be referenced through a parent class, but still execute its child class-specific methods.

```
#example in python is the list
son_and_daughter = [obj1, obj2]
```

<img src= "https://github.com/Goestoso/Python/assets/132786474/ba579334-dc12-4a36-9c77-d9881fc5cf42" alt="Polymorphism" align="center">

<br>
<br>

- In Python, method overriding is ___implicit___, just define a method with the same name in the child class that it will replace in the parent class.

> Father → def print_method(self):
> <br>
> Daughter → print_method(self):

- ___Example___:

```
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Function to make an animal make a sound
def animal_sound(animal):
    return animal.make_sound()

# Creating instances of classes
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the animal_sound function with different instances
print(animal_sound(dog))  # Saída: Woof!
print(animal_sound(cat))  # Saída: Meow!
print(animal_sound(cow))  # Saída: Moo!

```
