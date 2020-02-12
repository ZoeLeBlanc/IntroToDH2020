# Introduction to Python
![python logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

## What is Python?
|![python definition](/IntroToDH2020/week2/images/python_def.png)|
|:--:|
| [Wikipedia's Definition of Python](https://en.wikipedia.org/wiki/Python_(programming_language))|

In short:
- Programming language, created in 1991 by Guido van Rossum
- Named after Monty Python
- Used for a wide range of programming, from making web apps to data analysis

## Why Python?
|![python twitter](/IntroToDH2020/week2/images/python_twitter.png)| ![python stack overflow](/IntroToDH2020/week2/images/python_so.png) |
|:--:|:--:|
| [Jake VanderPlas Tweet](https://twitter.com/jakevdp/status/994934052091318272?lang=en) |[Stack Overflow's Annual Survey](https://insights.stackoverflow.com/survey/2019)|

In short:
- Python is well suited to a wide range of programming tasks
- Python has become the standard in a number of industries and academic disciplines
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
You're results should look something like the following.
![python_version](/IntroToDH2020/week2/images/python_version.png)

If you are getting errors, try looking at the [Python Installation Instructions](/week1/installation_instructions.md) and contact Zoe for help troubleshooting.

---

### Let's start coding
In your terminal, type `python3`. This will open the interactive python interpreter where you can write your python code and have the computer execute it. The python interpreter is an excellent way to sandbox your ideas or check your syntax. You can exit using `exit()`.

1. Type `'Hello world'` in the interpreter and press enter.

![hello world](/IntroToDH2020/week2/images/python_hw.png)

Congrats you've just typed your first bit of python and had the computer execute it 🎉!

Let's breakdown what just happened.
1. You entered data into the interpreter.
2. That data had a certain format, in this case variable, and the interpreter automatically showed that data again.

We can also use the interpreter as a calculator. Try out these examples.
```python
1+1
2**3
```
You'll notice that though the interpreter *prints* out when you press enter, the results of our calculations aren't saved any where. What if we wanted to save our data?

### Variables
We can save our hello world data into a *variable* and keep using it again and again.

```python
var = 'Hello world'
```
Now try typing `var` again. What happens?

The `var` variable now has 'Hello world' stored inside. Python understands that our variable contains a *string*. You can type any string and store it into a variable.
```python
one = 'one'
two = 'two'
three = 'three'
```
Python knows that these variables contain strings because of the use of either single('') or double quotes("").

---

### Data Types
Strings are just one of many data types accepted in Python.

There's also numbers, called *integers*. We can take our variables that we assigned before and assign them their actual numbers.
```python
one = 1
two = 2
```
Once we do this though, our strings that were stored in these variables will be **erased!**

What happens if you try and use a number for your variable?
```python
1 = 1
```
You'll get a syntax error! That's because Python has rules for how to name variables.

- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume)
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)

So our previous example could work if we changed the variable name to:
```python
one_1 = 1
```

Python also has a special name for floating point numbers, called *floats*.
```python
one = 1.0
```
Integers are simple and easy to use. Floats are mostly easy, but sometimes really weird!

*Weird Numbers*

What does this return?

```python
0.1+0.2
```

Huh, weird.

All data in a computer is represented as binary (base 2) numbers, comprising only 1s and 0s. The text you're reading now is represented by individual characters that, under the hood, are stored as binary numbers. The method of translating these information between different forms and contexts (such as between binary numbers and text or numbers) is called **encoding**.

Integers are easy enough to represent in binary: 0 is 0, 1 is 1, 2 is 10, 3 is 11, 4 is 100, and so on.

But floats are trickier and require a special system to represent. Don't worry about it for now, but consider for a moment that it's impossible to represent exactly 1/3 in finite decimal notation (0.3333...). It's similarly impossible to represent some simple decimal numbers in a binary notation. Which is why you get the weird results above.

For more information check out [Float to Binary Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html) and [IEEE 754 Standard](https://en.wikipedia.org/wiki/IEEE_754-1985).

---
### Methods

What if we decided that we wanted to combine variable `one` and `two`? We could use a **built-in Python method** for manipulating variables and data.

1. To join variables together use the `+` symbol, this is called concatenation.
```python
one + two
```
You should see `3.0` as your answer. We just added the data in variable `one` and `two` together. 


What would happend if we added variables `var` and `three` togther?
```python
var + three
```

Python strings are "immutable" which means they cannot be changed after they are created (Java strings also use this immutable style). Since strings can't be changed, we construct *new* strings as we go to represent computed values. So in this example we concatenate `var` and `three`, which builds a new string 'Hello Worldthree'.

1. Other methods that you can use on integers and floats:

division:
```python
one / two
```

multiplication:
```python
one * two
```

We can also assign a truth value to a variable, called a *boolean*.
```python
var_true = True
var_false = False
```
We can then check if these two variables contain the same truth value.
```python
var_true == var_false
```

In Python `=` is used to assign values to a variable, and `==` is used to check if two variables contain the same value. `True` in Python is interchangeable with the number `1` and `False` with `0`.



### Quick Assignment
In your Python interpreter complete the following prompts:
```
1. Look up Susan Hockey and Father Robert Busa on Wikipedia.
2. Assign to variables their names and birth years.
3. Try testing if their names are equal or if they were born in the same year.
4. Try joining their names together.
5. Try adding/multiply/dividing their birth years.
6. Try joining your names and years together.
```

---
### Data Structures
Typing the information of two or three historical figures is doable, but what if we wanted to do every member of the Alliance of Digital Humanities Organization (ADHO)? Typing a new variable each time to assign their value is really tedious!

That's where data structures come in! In Python, we can store data types in various data structures that are optimized for different problems.

#### Lists
If we wanted to take the first names of everyone in the ADHO, we could store them in a data structure called a *list*.

```python
names = ['Susan Hockey', 'Father Robert Busa', 'Louis Milic']
```

A list is an unordered, comma-separated collection of any values. So we can store any combination of values in our list.

```python
names = ['Susan Hockey', 'Father Robert Busa', 'Louis Milic', 42]
```

We can also store a list inside of another list.
```python
names = ['Susan Hockey', 'Father Robert Busa', 'Louis Milic', 42, ['Princeton', 'CDH']]
```

What if you want to just print out 'Susan Hockey' from the list? We can do that by *indexing* the list. 
```python3
names[0]
```
Each list in Python is a sequence, and we can access the position of an item in that sequence through indexing. **In Python, indexes always start at zero!**

We can use indexing in all sorts of ways.

1. We can take the final item by using negative one, which tells Python to get the last item from the list
```python3
names[-1]
```
2. We can take a range of items by using a colon to specify when we want to start and stop
```python3
names[1:3]
```
3. If we try to index longer than the list, we'll get an error that tells us we're out of range of the list
```python3
names[8]
```

Now what if we wanted to add DH projects to our list? We could create a new list that contained the projects and then use concatenation to join them.
```python3
projects = ['Valley of the Shadow', 'Orlando Project']
names + projects
```
We can see in the interpreter that we now have a list containing both lists, but what happens if you type names again?

Remember to store values, we need to *assign* them to variables.
```python3
projects = ['Valley of the Shadow', 'Orlando Project']
new_list = names + projects
```

We can also add items and remove them from the list. Let's take a look at some of these methods [https://www.w3schools.com/python/python_ref_list.asp](https://www.w3schools.com/python/python_ref_list.asp). You can read more about them in the python documentation [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

#### Quick Assignment
```
Try out the methods in the documentation for manipulating lists
1. Find a way to add 'American Panorama' to the end of our `new_list` (hint: there's multiple ways to do this)
2. Try reversing and sorting our `new_list`, what happens? Try doing the same on `projects`
```

Lists are great. But what if we wanted to store information not just in a sequence, but in a way that let's us keep certain values together?

#### Dictionaries
We can use a *dictionary*, which is a collection of key/value pairs to store this information. Keys and values are always separated by a colon.

```python3
professor = { 'name': 'Susan Hockey', 'birth_year': 1946}
```
To access our values in dictionaries, we don't use indexing. Instead, we use the keys of dictionary. Keys are always the values that come before the colon.
```python3
professor['name']
```
We write the key inside of brackets and quotations, called *bracket notation*. 

What happens if we add another name to the dictionary?
```python
professor = { 'name': 'Susan Hockey', 'birth_year': 1946, 'name':'Father Robert Busa'}
```
Where's Susan Hockey??

Susan Hockey was overwritten in our dictionary because our new value shared the same key. In a dictionary, keys must be unique!

Just like lists though we can store a dictionary inside of a dictionary
```python
professors = {
    'professor_1': {
        'name':'Father Robert Busa'
    },
    'professor_2': {
        'name': 'Susan Hockey',
        'birth_year': 1946
    },
}
```
Now we can get Susan Hockey's name if we type `professors['professor_2']['name']`. What's happening here is that we're using the keys to find our value that's nested inside a dictionary within a dictionary.

We can add Susan Hockey's age by using a similar notation:
```python3
`professors['professor_2']['age'] = 74
```

Just like lists there are many ways to manipulate dictionaries
[https://www.w3schools.com/python/python_ref_dictionary.asp](https://www.w3schools.com/python/python_ref_dictionary.asp)

#### Quick Assignment
```
Try out the methods for manipulating dictionaries.
1. Remove Susan Hockey's age from the `professor_2` dictionary
2. Get all the keys for the `professors` dictionary
3. Get all the values for the `professor_1` dictionary
```

You can also get even crazier and store lists in dictionaries:
```python
professors = {
    'professor_1': {
        'name':'Father Robert Busa',
        'projects': ['Index Thomisticus', 'Index Thomisticus Treebank']
    },
    'professor_2': {
        'name': 'Susan Hockey',
        'birth_year': 1946
    },
}
```
Notice that the list is a value of a key, in this case `projects`. You can only insert a list into a dictionary as a value.

You can also put dictionaries inside of lists:
```python
professors = [
    {
        'name':'Father Robert Busa',
        'projects': ['Index Thomisticus', 'Index Thomisticus Treebank']
    },{
        'name': 'Susan Hockey',
        'birth_year': 1946
    }
]
```
Notice that we now don't have keys for our top-most dictionaries. In lists, items don't have keys so each of your dictionaries is without an explicit key.

Python defaults to indexing each dictionary with numbers, just like in our list of strings. So to get the first value, you would type:
```python
professors[0]
```

Congratulations 🎉🎉🎉! You've now completed the introduction to Python.

If anything is unclear, please bring questions you have to class and we'll being doing an overview of these concepts. Also checkout the [Python Cheatsheet](/week2/python_cheatsheet.md)!

If you want to continue with learning and exercises, check out the additional materials [here](/week2/more_python.md) but otherwise we'll cover this in class together.