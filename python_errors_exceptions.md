# Errors and Exceptions
## Errors
### SyntaxError
When Python is unable to understand the code it results in a <b>SyntaxError</b>. 

The most common reasons of <b>SyntaxError</b>:
- typos, such as misspelled keywords,
- a keyword in the wrong place,
- leaving out symbols, such as colons and brackets,
- incomplete statements.
- when a string is mistakenly used as a variable name - SyntaxError: can't assign to literal

Syntax errors are returned before Python attempts to run the code.

A logic error occurs when there is no error or exception, but our code does not work correctly.


### IndentationError
Incorrect or missing indentation, extra blank spaces will result in an <b>IndentationError</b>, which is a specific type of SyntaxError.

^ symbol - a caret, indicates in the console where the error has been found in the code. 

### Exceptions
Python will raise an exception when it cannot perform an operation. The text shown in the console when an exception is raised is called the <b>traceback</b>. It helps us <b>debug</b> our code, which means finding errors. Examples of exceptions <b>ZeroDivisionError</b>,<b>NameError</b>,<b>TypeError</b>. 

<b>ZeroDivisionError</b> occurs in Python when a number is attempted to be divided by zero.

<b>ModuleNotFoundError</b> - when Python cannot find a module.

<b>IndexError</b> - if an index is out of range.

## Raising Exceptions
### raise
 Sometimes we want to <b>raise</b> an exception when a condition we have defined is not met. We can use exceptions to highlight when something cannot be working as it should be.
 ```
slices = 18 
diners = 0
if diners < 1:
  raise Exception("There must be at least one diner")
else:
slices_each = slices / diners
 ```
 The <b>raise</b> keyword is used to raise an exception. We can define both the kind of error, and the error message.
 ```
 age = -3
 if not age >= 0:
   raise ValueError('age cannot be negative')
 ```
We can use conditions to <b>validate</b> inputs, and raise an exception when the conditions are not met.
```
scores = [125, 60, 189, 88, 16]
if min(scores) < 0 or max(scores) > 180:
  raise ValueError('Error in scores')
```
### try: and except:
We often don't want a program to terminate when an exception is encountered. A <b>try</b> abd <b>except</b> block can be used for <b>exception handling</b>.
```
try:
  login(user)
except:
  print('User not known, please try again')

  # Output
  User not know, please try again
```
<b>try</b> abd <b>except</b> blocks tend to be used where we know there is a chance of the operation not being possible.
```
hours = []
try:
  average = sum(hours) / len(hours)
except:
  average = 0
print(average)
```
<b>try:</b> abd <b>except:</b> are followed by an indented block of code. 
### pass
We can use <b>pass</b> if we want nothing to be executed after <b>except:</b>.
```
try:
  print("Hello, " + user)
except:
  pass
```
The <b>raise</b> keyword is used along with a valid type of error and an optional message. It is usually used within en <b>except</b> code block.
```
try:
  10 + score
except:
    raise ValueError("Invalid score")
```
### else
We can use an <b>else</b> statement at the end if we want to execute some code only when no error has been raised.
```
details = {"name": Helena, 
           "occupation": "carpenter"
           "age" : 35}
try:
  age = details["age"]
except:
  raise NameError("No age value in record")
else:
  print(f"Maximum heart rate is {220 - age}")
```
### finally
We can use a <b>finally</b> statement at the end if we want to execute some related code regardless of whether en error was raised.
```
entry = 50

try:
  result = entry * 1.5
except:
  raise ValueError("result cannot be calculated")
else:
  print(result)
finally:
  print("Try another value?")
```