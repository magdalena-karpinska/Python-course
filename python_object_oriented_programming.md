# Object-oriented programming
## Encapsulating Objects
Different styles of coding are known as <b>paradigms</b>. A common style is called <b>functional programming</b>(<b>FP</b>). <br>
In functional programming, we use a lot of functions and variables.
```
def getTotal(a, b):
  return a + b

num1 = 2
num2 = 3
total = getTotal(num1, num2)
print(total)
```

In FP style, we keep data and functionality seperate. We pass data into functions whenever we want something.
```
def getDistance(mph, h):
  return mph * h

mph = 60
h = 2

distance = getDistance(mph, h)
```
In FP, functions <b>return</b> new values and then use those values somewhere else in the code: 
```
def getDistance(mph, h):
  return mph * h

mph = 60
h = 2

distance = getDistance(mph, h)
print(distance)
```
In <b>object-oriented_programming (OOP)</b>, we group data and functionality as properties and methods inside objects, which is called <b>encapsulation</b>:
```
class Virtual_Pet:  #Virtual_Pet is and object
  def __init__ (self, color, name):
    sel.color = color
    self.name = name

rocky = Virtual_Pet("brown", "rocky")

print(rocky.color)
print(rocky.name)
```
OOP is useful for modeling objects, real-life or not. Objects have properties and methods that we treat as one thing.<br>

In OOP, we use methods to update existing values of an object:
```
class Dog:
  hungry = True

  def eat(self):
    self.hungry = False
```
## Applying Inheritance in OOP
We use <b>inheritance</b> to make our code efficient. Through inheritance, classes receive methods from other classes.<br>

Inheritance lets us create classes that have different properties and behaviours without coding each one from scratch. 
```
class Parent:
  def __init__(self):
    self.eyes = "green"

class Child(Parent):  # Child class is inheriting the Parent class
  def __init__(self):
    super().__init__()
    self.age = 7

child = Child()
print(child.eyes)
pint(child.age)
```
### How a class inherits methods from another
1. When defining the class we add parentheses with the class that we're inheriting:
```
class Greetings:
  def greet(self):
    print("Hi!")

class Person(Greetings):
  name = "George"

  p = Person()
  p.greet()
```
The Person class can now use the Greeting's methods like its own.

2. In:
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hi!")

class Student(Person):
  def __init__(self, name, age, major):
    super().__init__(name, age)
    self.major = major
```
- <b>super</b> refers to Studen't parent class - Person. <br>
- <b>__init__</b> refers to Person's constructor. This allows us to use the existing constructor to set the name and age properties.

