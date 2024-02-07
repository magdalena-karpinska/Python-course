# Classes

## Using classes
A class is a template that we use to create many similar but distinct things. That way we can create different configurations without having to create individual variables each time.
```
class Computer:
  def __init__(self, size, storage):
    self.size = size
    self.storage = storage

  def print_spects(self):
    print("Display size: " + seld.size)
    print("Storage size: " + self.storage)

low_spec = Computer("13", "256GB")
mid_spec = Computer("15", "512GB")
high_spec = Computer("17", "2TB")
```
### How to use a class
1. To start a class, we add the keyword <b>class</b> followed by a name and a colon.
```
class Person:
```
2. To add code to the class, we indent from the keyword <b>class</b>
```
class Person:
  print("inside the class")
```
3. Creating a variable inside class works just like creating normal variables. It needs to be properly indented and assigned a value.
```
class Person:
  nationality = "French"
```
4. We can add as many variables as we'd like inside a class.
```
ass Person:
  nationality = "French"
  hobby = "Cooking"
```
## Creating Instances
When we create variables from class template, we're creating <b>instances</b>.

1. We start by creating a variable:
```
class VirtualPet:
  color = "brown"

fluffy = 
```
2. We add the class name and parentheses to create it:
```
class VirtualPet:
  color = "brown"

fluffy = VirtualPet()
```
The class VirtualPet is <b>a definition</b> and fluffy variable is <b>an instance </b>.

### How to access a class variable

We add the instance name, a <b>.</b> and the name of the variable we want.
```
class VirtualPet:
  wagging_tail = True
  color = "brown"

skippy = VirtualPet()
print(skippy.wagging_tail) #instance name . variable name
```

## Classes with Methods


## Constructors

<b> constructor method</b> - a method that is more flexible when creating different instances from a class, it looks like:
```
__init__()
```
...and allows to set unique values for the class variables when we create an instance.

```
class Virtual_Pet:
  def __init__(self, color):
    self.color = color

rocky = Virtual_Pet("red")
```
Instead of class definition that will always have the same color, a constructor method allows us to specify what we want when creating it. 
<br>

When we create an instance from the class definition, we're able to pass unique values inside the parentheses.

```
class Virtual_Pet:
  def __init__(self, color):
    self.color = color

rocky = Virtual_Pet("yellow") #unique value inside parentheses
```

### How to add flexibility to our classes

1) We start by adding the construction function.
```
class Virtual_Pet:
  def__init__(): #__init__()
```


2) Just like with regular methods, we need to add <b>self</b> as the first parameter to the construction method.

```
class Virtual_Pet:
  def__init__(self):
```
3. We add the parameters for the custom values we want to set when we create the instance.
```
class Virtual_Pet:
  def __init__(self, color): #color is a parameter for the custom value
```
4. We set a value

```
class Virtual_Pet:
  def __init__(self, color):
    self.color = color
```
5. When we create an instance from the class definition, we add the values we want to set inside parentheses, like here with "red".
```
class Virtual_Pet:
  def__init__(self, color):
    self.color = color

rocky = Virtual_Pet("red") # "red" is a value
print(rocky.color)
```
The constructor method allows to add as many parameters as we want.
```
class Virtual_Pet:
  def__init__(self, color, legs):
    self.color = color
    self.legs = legs

rocky = Virtual_Pet("red", 4)
print(rocky.color)
print(rocky.legs)
```
We can access the parameters from other places in the class definition by using <b>self</b>:
```
class Flower:
  def__init__(self, kind, color):
    self.kind = kind
    self.color = color

  def display_color(self):
    print(self.color)

rose_flower = Flower("rose", "red")
print(rose_flower.kind)
rose_flower.display_color()
```
## Understanding classes

Classes names usually have the first letter capitalized and the lowercase:

```
class Person:
def__init__(self, name, age):
    self.name = name
    self.age = age
```
We try to name classes descriptively:
```
class Book:
  def__init__(self, author, title)
    self.author = author
    self.title = title
```

