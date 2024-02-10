# Modules and Libraries
Classes are a way to organize data and functionality together. We can add more organization to our code with something called a <b>module</b>.
```
import math

print("The value of pi is")
print(math.pi)
```
Modules group related classes and data and make them accessible from one place.
```
import math

print("The value of pi is")
print(math.pi)

print("The square root of 16 is")
print(math.sqrt(16))
```
Some modules are available online for people to use in their code. Python has some built-in modules too. The math module provides data like the value of pi and methods for different math operations. 

## How to use a module
1. We import it with the keyword <b>import</b> followed by the module's name.
2. To use the module, we add its name, followed by the method or data we want.
```
import math
square = math.sqrt(16)
print(square)
```
3. We can find out the functionality a module has by using the <b>help()</b> instruction with the name of the module between the parentheses.
```
import math
square = math.sqrt(16)
help(math)
```
4. We are able to use multiple different modules in the same file by adding a coma between the modules we're importing.
```
import statistics, math
```
5. We can use only a part of a module and not the whole functionality. In that case we can use the keyword <b>from</b> to extract only the functionality we want. When we use<b>from</b>, we don't need to add the name of the module anymore.
```
import math

print("The value of pi is")
print(math.pi) # We use the value for pi from math

from math import pi
print("Value of pi is:")
print(pi) # we didn't have to use math anymore
```
## Aliasing
We can modify the name of the module we're importing. We first code the <b>import</b> keyword and module name, then, we use the <b>as</b> keyword to set a new name. <b>Aliasing</b> is used to make longer module names shorter or so they don't interfere with variables in our code.
```
import statistics as state
```
# Libraries
Libraries are collections of modules that help us save time when coding. 
- The Python Standard Library - authomatically installed when we first install Python
- The Documentation - to get more information about the library

To install a library (or a package), we use the keyword <b>pip</b>. It stands for the <b>Preferred Installer Program</b>.
```
pip install matplotlib
```
To install a module from a library:
```
from matplotlib import pyplot # from <library> import <module>
```

## Introduction to NumPy
<b>NumPy</b> - Numerical Python, a library that provides a set of tools that make working with large amounts of data easy and fast.

### import
To import it:
```
import numpy as np # <import> <package name>
```

### array()
Numpy allows us to store data in <b>arrays</b>, which are like lists, but faster to operate with, and with extra features. 

To transform a list into array:
```
import numpy as np
stock = np.array([10, 12, 25])
print(stock)
```
<b>array()</b> can be used with lists of strings or any other type, as long as the entire list has the same type.
```
import numpy as np
stock = np.array(["10", "12", "25"])
print(stock)
```
Trying to create an array from a list of mixed data types, will cast all the list values to the same type:
```
import numpy as np
stock = np.array([10, 12, "25"])
print(stock)

#Output
['10' '12' '25']
```
Indexing can be used to access elements in the array:
```
import numpy as np
stock = np.array([10, 12, 25])
print(stock[0])
```

### size()
Every array has a <b>size</b> representing the number of elements it contains. To obtain the size of a NumPy array, we use the <b>size</b> method:
```
import numpy as np
stock = np.array([10, 12, 25])
print(np.size(stock))
```

### zeros()
NumPy provides the <b>zeros</b> method that creates a <i>float</i> array filled with O's:
```
import numpy as np
scores = np.zeros(3)
print(scores)

# Output
[0. 0. 0.]
```
To use <b>zeros</b>, we need to specify the size of the array we want to create:
```
import numpy as np
scores = np.zeros(5) #size of 5 zeros
print(scores)

# Output
[0. 0. 0. 0. 0.]
```
### ones()
Method <b>ones</b> creates a float array filled with <b>1.</b>'s.

### arange()
If we want to create an array with different numbers, we use <b>arange</b> method, that returns an array of numbers in ascending order:
```
import numpy as np
indices = np.arange(5)
print(indices)

# Output
[ 0 1 2 3 4]
```
Array created that way, starts with 0. Because of that, we often use it when looping over arrays or lists to obtain all the indices.
```
import numpy as np
indices = np.arange(3)
stock = np.array([10, 12, 25])
for index in indices:
  element = stock[index]
  print(f'Index:{index}, element: {element'})
```
With <b>arange</b> we can create a range:
```
import numpy as np
indices = arrange(3, 6)
print(indices)

# Output
[3 4 5] # we needed to use 6, as the the end of the range is not included
```
With <b>arange</b> we can specify the step size:
```
import numpy as np
even_betwen = np.arange(4,11,2)
print(even_betwen)

# Output
[ 4 6 8 10]
```
To round up numbers with math module:
```
import math
print(math.ceil(65.9))
```