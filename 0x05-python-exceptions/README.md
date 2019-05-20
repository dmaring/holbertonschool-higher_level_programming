# 0x05. Python - Exceptions
## About this project

* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception


## Requirements
- Ubuntu 14.04
- gcc 4.8.4

## File Descriptions
### Mandatory
**[0-safe_print_list.py](0-safe_print_list.py)** - a function that prints x elements of a list

**[1-safe_print_integer.py](1-safe_print_integer.py)** - a function that prints an integer with "{:d}".format().

**[2-safe_print_list_integers.py](2-safe_print_list_integers.py)** - a function that prints the first x elements of a list and only integers.

**[3-safe_print_division.py](3-safe_print_division.py)** - a function that divides 2 integers and prints the result.

**[4-list_division.py](4-list_division.py)** - a function that divides element by element 2 lists.

**[5-raise_exception.py](5-raise_exception.py)** - a function that raises a type exception.

**[6-raise_exception_msg.py](6-raise_exception_msg.py)** - a function that raises a name exception with a message.



### Advanced
**[100-safe_print_integer_err.py](100-safe_print_integer_err.py)** - Write a function that prints an integer.

* Prototype: def safe_print_integer_err(value):
* value can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns True if value has been correctly printed (it means the value is an integer)
* Otherwise, returns False and prints in stderr the error precede by Exception:
* You have to use try: / except:
* You have to use "{:d}".format() to print as integer
* You are not allowed to use type()

**[101-safe_function.py](101-safe_function.py)** - Write a function that prints an integer.

* Prototype: def safe_function(fct, *args):
* You can assume fct will be always a pointer to a function
* Returns the result of the function,
* Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
* You have to use try: / except:

**[102-magic_calculation.py](102-magic_calculation.py)** - Write the Python function def magic_calculation(a, b): that does exactly the same as the given Python bytecode.

**[103-python.c](103-python.c)** - Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.