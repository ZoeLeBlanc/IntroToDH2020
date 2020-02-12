


```python
print("Hello Cruel World!")
```
"Print" is a function, which is like a command. Functions are called by writing the function name followed by parenthesis. Inside the parenthesis are zero or more parameters, which are extra bits of information that you attach to the function. The "print" function simply writes out the data that's passed to it.

If you're looking for help on the internet and ever see `print "foobar"` instead of `print("foobar")` (without the parenthesis), that's Python 2 code instead of Python 3!






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