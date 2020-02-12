# Introduction to Python
![python logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

## What is Python?
|![python definition](/week2/python_def.png)|
|:--:|
| [Wikipedia's Definition of Python](https://en.wikipedia.org/wiki/Python_(programming_language))|

In short:
- Programming language, created in 1991 by Guido van Rossum
- Named after Monty Python
- Used for a wide range of programming, from making web apps to data analysis

## Why Python?
|![python twitter](/week2/python_twitter.png)| ![python stack overflow](/week2/python_so.png) |
|:--:|:--:|
| [Jake VanderPlas Tweet](https://twitter.com/jakevdp/status/994934052091318272?lang=en) |[Stack Overflow's Annual Survey](https://insights.stackoverflow.com/survey/2019)|

In short:
- Python is well suited to a number of programming tasks
- Python has become the standard in a number of industries
- BUT many of the concepts covered in Python translate to other programming languages too!

## Python 2 vs Python 3?
While Python was officially founded in 1991, it only became popular after the release of Python 2.0 in 2000 (not to be confused with Python 2) when the language switched to a more public code repository (more on repositories later!) and a more open, community-driven development model.

Python 3 was released in 2008 as a major reformation of the language that made it more consistent and unified redundant mechanisms. Python 3 is not backwards compatible with Python 2; it is, in effect, a **new language**. You should definitely use Python 3 because Python 2 is no longer officially supported since [January 1, 2020](https://pythonclock.org/).

Many computers come with Python 2 already installed by default. Depending on how yours is set up, running `python` may run the Python 2 or Python 3 interpreter. To determine which one, run the command `python --version`. 

### Open your terminal and check your python version
Type:
```sh
python --version
python3 --version
```


Python comes with an interactive interpreter that executes your instructions as you enter them line by line. For beginners, it's an excellent way to sandbox your ideas or check your syntax. Start the interactive interpret using the `python` (or `python3`) command.

You can exit using `exit()`.



### Let's start coding
In your terminal, type `python3`. This will open the interactive python interpreter where you can write your python code and have the computer execute it. 

1. Type `'Hello world'`
Congrats you've just typed your first bit of python and had the computer execute it 🎉!

Let's breakdown what just happened.
1. You entered data into the interpreter
2. That data had a certain format, in this case variable, and the interpreter automatically showed that data again.

```python
print("Hello Cruel World!")
```
"Print" is a function, which is like a command. Functions are called by writing the function name followed by parenthesis. Inside the parenthesis are zero or more parameters, which are extra bits of information that you attach to the function. The "print" function simply writes out the data that's passed to it.

If you're looking for help on the internet and ever see `print "foobar"` instead of `print("foobar")` (without the parenthesis), that's Python 2 code instead of Python 3!

What if we wanted to save our data?

## Python interpreter as calculator
```python
1+1
2**3
```

## Hello World
### Variables, Functions, amd Parameters


## Variables


### String functions (concatenation)
```python
madlibs="Scholars' Lab"
print("I, for one, 'welcome' our new "+madlibs+" overlords!")
```
Variables are little bits of information that are given names so that they can be modified or reused later. In the first line, we are assigning a string (a variable type that contains text) to the variable with the name "madlibs".

In the second line, we use the + operator to concatenate three strings together and pass the result to print.

You can also "multiply" strings.

```python
print("Scholars' L"+"a"*10+"b")
```

### Numbers
```python
a = 7
b = 3
a+b
a/b
```
Integers are whole numbers. Floats (floating point numbers) are prepresentations of real numbers. Integers are simple and easy to use. Floats are mostly easy, but sometimes really weird!

### Weird Numbers

What does this return?

```python
0.1+0.2
```

Huh, weird.

!["There are 10 kinds of people in the world..."](assets/10kinds.jpeg)

(No one really understands binary)

All data in a computer is represented as binary (base 2) numbers, comprising only 1s and 0s. The text you're reading now is represented by individual characters that, under the hood, are stored as binary numbers. The method of translating these information between different forms and contexts (such as between binary numbers and text or numbers) is called encoding.

Integers are easy enough to represent in binary: 0 is 0, 1 is 1, 2 is 10, 3 is 11, 4 is 100, and so on.

But floats are trickier and require a special system to represent. Don't worry about it for now, but consider for a moment that it's impossible to represent exactly 1/3 in finite decimal notation (0.3333...). It's similarly impossible to represent some simple decimal numbers in a binary notation. Which is why you get the weird results above.

[Float to Binary Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html)

[IEEE 754 Standard](https://en.wikipedia.org/wiki/IEEE_754-1985) if you really want to learn more.

### Booleans
```python
print(True)
print(False)
print(True or False)
print(True and False)
print(not True)
```
True in Python is interchangeable with the number 1 and False with 0.

## Comments and Documentation
### Inline Commenting
```python
# Life is suffering...
1+2+3
```

Comments are especially useful--necessary!--for collaboration. Python is open source and its community of millions of coders often share in its permissive approach to intellectual property. Python as a whole is a giant collaborative project of which you are now members.

When you write particularly complicated logic or whenever you write new classes or functions (more on this later!), you should write a comment to explain yourself.

### Documentation

Python, as with virtually all other languages and complex codes, contains extensive documentation that covers all aspects of its use. This documentation is [easily accessible via the Internet](assets/MissionImpossible.m4v?raw=true).

[Python 3 Documentation](https://docs.python.org/3/)

Let's take a look at the specific documentation for strings:

[Python 3 Docs: Built-in Types: Strings](https://docs.python.org/3/library/stdtypes.html#string-methods)

Learning to read documentation is a critical skill for succeeding as a programmer. Happily, most of you, as graduate students, should already be literate.

## Interlude: The Zen of Python
### What's the deal with Python? 
Type this into Python:
```python
import this
```

Here's [one interpretation of Z of P](https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/).

Also, a DH answer: lots of DH projects are written in Python because of its simplicity and robust community and it's especially popular in areas like text analysis and machine learning.

## Saving and running code
The Python interactive interpreter is very useful for experimentation, but if you want to write something less ephemereal, you'll want to save it as a file so that it can be run over again without going through it line by line. The code is exactly the same, just save it as a text file to your disk with the usual Python file format extension, .py.

Now, you can run the resulting file using the command `python code.py` (or `python3 code.py`).

There are some important differences in behavior between running code through the interactive interpreter and as a saved .py file. The way that we've been using the interpreter so far has relied on how it returning values that we reference.

If we run these two lines in the interactive interpreter, we see that the second statement prints 2 because Python assumes that we want to know more about it:

```
>>> a = 1+1
>>> a
2
```

If we ran these lines from a .py file, nothing will print at all because the statement `a` on the second line doesn't actually tell Python to do anything. In a .py file, we have to explicitly tell Python to print using the print() function.

```python
a = 1+1
a
```

## Input
Code that always does the same thing is a little boring. Let's spice up the earlier example a bit with user input.
```python
madlibs=input("What manner of overlords do you, for one, welcome? ")
print("I, for one, welcome our new "+madlibs+" overlords!")
```

## Sequences
### Lists

![Bad Pun Hazel](assets/sleeping_hazel.jpeg)

```python
dogs = ["Toby","Bofur","Hazel","Maple","Henry","Fat Dog","Monty", "Keefa"]
print(dogs[0])
print(dogs[-1])
print(dogs[3:])
print(len(dogs))
dogs.sort()
print(dogs)
dogs.sort(reverse=True)
print(dogs)
```

Lists are one type of sequence, which are ordered collections of variables (including sequences, so you can have lists of lists).

[Python 3 Docs: Built-in Types: Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

Strings are actually sequence types, just like lists! They're sequences of characters and we can address particular characters just like with lists.

```python
gooddog = "Hazel is a good dog"
print("Every dog"+gooddog[5:])
```

## Modules
### Python Standard Library
```python
import random
print(random.randint(0,10))
```

[Python 3 Docs: Standard Library: Numeric and Mathematical: Random](https://docs.python.org/3/library/random.html#module-random)

Of course, you don't always want to write your own code. Programmers are ~~lazy~~ efficient. Python has a famously robust built-in Standard Library so you can reuse the work of thousands of programmers who have contributed to it. This Standard Library is part of the language itself and is included in every Python installation.

For more specialized tasks, it's also easy to use the work of third party developers. But we'll leave that to another week.

## Let's Hope You Paid Attention!
### Work together!
Pair programming is a common practice. We want you to always do pair programming. Let's write some code to assign each of you a partner for this week's homework using what we've just learned!

```python
praxis = ["chloe","connor","janet","lauren","natasha"]
# ???
```

##### Hint: there's a section in the Random library documentation [just for working with sequences](https://docs.python.org/3/library/random.html#functions-for-sequences)!