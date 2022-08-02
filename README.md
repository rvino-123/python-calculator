# (Yet Another) Python Calculator Project!

## Description

A Command Line Interface Calculator that accepts a mathematical statement in infix notation, converts it into postfix notation and then calculates the result. This cacluator uses _no 3rd party libraries_ and includes an own implementation of a Stack Datastructure.

- standard library modules used:

  - dequeue - a list like structure optimised for insertion/removal at both ends of the list. Used to form the Stack datastructure.
  - decimal - a library used for more accurate float arithmatic. Because float values are converted to binary, there is a loss in accuracy when performing calculations with float. the decimal library corrects that loss and makes the result interpretable to humans.

- Project was written in Python 3.10

## Setup

- To get the repository in your local machine, clone the repo at

`git clone https://github.com/rvino-123/python-calculator.git`

- You can run the program from `main.py`
  - e.g. run `python3.10 Calculator/calculator/main.py`

## Examples

- Basic Arithmetic

```
python3.10 Calculator/calculator/main.py
# Enter your statement/command here
calculator> 3 + 9 - 5
7.0
```

- Parantheses

```
python3.10 Calculator/calculator/main.py
# Enter your statement/command here
calculator> (2 * 5) + (8 * 9)
82.0
```

- Handles Float Values

```
python3.10 Calculator/calculator/main.py
# Enter your statement/command here
calculator> 3.98 * 3.55
14.129
```

## Other Options

- Entering "H, h, help" will return with a usage guide

```
python3.10 Calculator/calculator/main.py
# Enter your statement/command here
calculator> help
Usage:

6 * 5 + 10

Options:

q Q quit  Quits Program
```

- Entering q Q quit will exit the program.

```
python3.10 Calculator/calculator/main.py
# Enter your statement/command here
calculator> quit
Program Exited Succesfully.
```

### **NEW FEATURES 02/08/22**

- Power functions

```
python3.10 Calculator/calculator/main.py
# Enter your statement/command here
calculator> 2 ^ 10
1024.0
```

- Trigonometric functions

```
python3.10 Calculator/calculator/main.py
# Enter your statement/command here
calculator> cos(45)
0.5253219888177297
```

# What I learned from this project

- I learned to appreciate the signifiance between how humans interpret a statement and how machines would. I convert the provided statement into postfix notation (two numbers preceding an operator) because, although not as understandble to humans, it is more clear to the machine what operation and inputs are used.
- I learned how float arithmetic in Python works, as well as it's limitation that required the use of the decimal library.
- The difference between a Queue and a Stack and the situations where both are appropriate. i.e. when I need to prioritise values more recently inserted into the Stack or I want the first inserted element to come out first.
- Using class methods to conditionally instantiate class objects.
- Usage of static methods that don't require an instance of a Class in order to run.

## Future Work

- ~~Ability to raise a number to a certain power~~ ✅ 02/08/22
- ~~offer functions such as trigonometric, log, exponential, root etc..~~ ✅ 02/08/22
- allow user to specify how many significant figures they'd like the output to return.
- store the previous result in memory so that it can be used in a subsequent calculation i.e. `ans + 5` where ans is the result of the previous calculation

## Contributing as Open Source

- I am currently not open to contributions. Please feel free to fork/clone the project and use it as you wish.
