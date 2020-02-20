## Python Fundamentals 1

**Data Flow**

Computers read code line by line, top to bottom of a script. But what if you want to have code run not in sequential order, or you want your code to do something depending on a value, or you want to reuse your code and run it multiple times?

We can solve all those problems with data flow structures.

#### 1. Looping
In `code_review_week2.py` you had to print out multiple values from the tools dictionary. While typing each value out is tedious, it was still possible to do. However, what would happen if you had hundreds or thousands of values? 

There's a much faster way to traverse data structures and types in Python, called `Looping`. With various types of loops in Python, you can travel through a sequence (i.e. a list, dictionary, string, etc...) to be able to manipulate items within the sequence.

**For Loops** are one of the most common ways in python to loop over a sequence. But what does looping mean exactly?

Let's go back to our script from week 2, and find our list of names. Add these lines to the script:
```python
names=["Sara", "Kevin", "Shiva", "Anna", "Meher", "Maia"]
for name in names:
    print(name)
```
![https://www.oreilly.com/library/view/head-first-python/9781449397524/httpatomoreillycomsourceoreillyimages1368346.png.jpg](https://www.oreilly.com/library/view/head-first-python/9781449397524/httpatomoreillycomsourceoreillyimages1368346.png.jpg)

We can also use For Loops on dictionaries. The syntax is slightly different because dictionaries are not one long sequence, but rather a sequence of key/value pairs.
```python
tools = {"Python":{"2015":9, "2016":22, "2017":27, "2018":32, "2019":35}, "Javascript":{"2015":8, "2016":18, "2017":12, "2018":6, "2019":15}, "Twitter":{"2015":10, "2016":18, "2017":26, "2018":16, "2019":12}, "Github":{"2015":2, "2016":6, "2017":17, "2018":5, "2019":10}, "Gephi":{"2015":11, "2016":16, "2017":14, "2018":10, "2019":9}, "Geonames":{"2015":2, "2016":4, "2017":3, "2018":1, "2019":8}, "Transkribus":{"2015":0, "2016":1, "2017":2, "2018":1, "2019":8}, "Excel":{"2015":5, "2016":9, "2017":3, "2018":6, "2019":7}, "MySQL":{"2015":0, "2016":6, "2017":9, "2018":5, "2019":7}}

for key, value in tools.items():
    print('key', key)
    print('value', value)
```

Or even strings.
```python
for letter in 'Digital Humanities':
    print(letter)
```

For more about looping in Python checkout [https://wiki.python.org/moin/ForLoop](https://wiki.python.org/moin/ForLoop) and [https://www.learnpython.org/en/Loops](https://www.learnpython.org/en/Loops).

#### Functions
Looping is very powerful, but if we want to loop through a second list of names or a different variable, we would have to repeat our code later in the script. An alternative is to create a function.

A function is a way to organize code by packaging many lines of code together into a single bundle. At the most basic level, this makes it easy to reuse code: it's easier to write out and read a single line rather than many lines and easier to change code in one place rather than in many places.

**Function Syntax**
![https://cdn.askpython.com/wp-content/uploads/2019/06/python-functions.png](https://cdn.askpython.com/wp-content/uploads/2019/06/python-functions.png)

To create a function, we define using `def` and a unique name and finally parentheses, followed by colon. Then we can pass *arguments* (also called parameters) in the parentheses, that we can that use *inside* of the functions. Those arguments will be *variables* and so we can do anything you would normally do to a value. Finally we can *return* the result of our manipulation.

For example try:
```python
def get_fundamentals():
    fundamentals = 'Having fun'
    print(fundamentals)
    return fundamentals

get_fundamentals()
```

What would happen if you try to access the variable `fundamentals` after the line `get_fundamentals()`?

Spoiler alert you'll get this message:
```sh
NameError: name 'fundamentals' is not defined
```

We get that error because `fundamentals` is only defined in the **local scope** of the function. That is the variable `fundamentals` only exists within the function and can only be accessed within it. This is why when writing functions we either use two or four spaces (or tabs) to indent our code. 

This is called "white space", and indicates to Python that everything that's indented is part of the function definition. As soon as we stop indenting, the function definition is over. We can use any number of spaces or tabs, but they have to be consistent. Notice we also used white space in the For Loops. Similar to in our function, variables defined within the for loop are only available within the local scope of the loop.

We also use something called a **return statement**.

```python
def get_fundamentals():
    fundamentals = 'Having fun'
    print(fundamentals)
    return fundamentals

new_fundamentals = get_fundamentals()
```

If you printed out `new_fundamentals` what would this variable contain? You might expect it to print out the function, but it will actually print out the local variable `fundamentals`.

Return is used to pass data back from the function, which can then be assigned to a new variable that's accessible in the rest of the script, also known as the **global scope**.

```python
def get_fundamentals(code_concept):
    fundamentals = 'Having fun, ' + code_concept
    return fundamentals

new_fundamentals = get_fundamentals('for loops')
```
We can also pass in data to our functions through the parentheses when we call and define our functions. This is called passing **arguments** into our functions. In this example, what does `new_fundamentals` contain?

Arguments can have any name (so our example above could have named `code_concept` as `data` or `x`) and can contain any data type or structure. 

Using functions and for loops we can reuse our code whenever we want within our script. 

For example, try and understand this code from week 2 exercise:

```python
def make_tool_dict(name, value_2015 , value_2016, value_2017,value_2018, value_2019):
    return {
        "2015":value_2015 ,
        "2016":value_2016,
        "2017":value_2017,
        "2018":value_2018,
        "2019":value_2019,
        "name":name,
        "total":value_2015+value_2016+value_2017+value_2018+value_2019
    }

dh_tools=[make_tool_dict("Python",9,22,27,32,35),
          make_tool_dict("JavaScript",8,18,12,6,15),
          make_tool_dict("Twitter",10,18,26,16,12),
          make_tool_dict("GitHub",2,6,17,5,10),
          make_tool_dict("Gephi",11,16,14,10,9),
          make_tool_dict("GeoNames",2,4,3,1,8),
          make_tool_dict("Transkribus",0,1,2,1,8),
          make_tool_dict("Excel",5,9,3,6,7),
          make_tool_dict("MySQL",0,6,9,5,7)]

print("\nPrinting tools...\n")
for tool in dh_tools:
    for prop in ["name","2015","2019","total"]:
        print(prop+": "+str(tool[prop]))
    print("")
```

What arguments does the `make_tool_dict` function take and what value does it return?

What does `dh_tools` variable contain?

What is the for loop iterating through? What does `str(tool[prop])` do?

For more on functions, checkout this tutorial [https://www.datacamp.com/community/tutorials/functions-python-tutorial](https://www.datacamp.com/community/tutorials/functions-python-tutorial)

#### Control flow
So far, the code that we've written has flowed forward, line by line. Even the function definition: the contents of the `def` block are read in order by the interpreter. The order of instructions through which a computer program runs is known as "control flow". We can affect the flow with conditionals and loops which allow us more interesting modes.

#### Conditionals
Earlier we learned about *booleans* (`True or False`). In Python, we can test the truth value of code to decide how we want our code to run.
![https://automatetheboringstuff.com/images/000019.jpg](https://automatetheboringstuff.com/images/000019.jpg)

A conditional is a way for a computer program to make a choice. The basic syntax of the conditional in many programming languages is the `if` statement. In Python, it looks like this:

```python
x = 5
if x>0:
    print("Positive")
```

If statements are essentially expressions that follow `if` and end with a `:`. We indent whatever code we want to run if that expression is successful within that code block, just like with functions or for loops. In this case, when whatever value we assign to `x` is *greater than* zero our script will run the print statement. What happens if we assign `x` to `-1`?

```python
x = 5
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("Zero")
```
We an also use additional conditional keywords `elif` (else if) and `else` to add more complexity to our code. Each of the conditional blocks (the three `print()` statements) are only run if the associated conditional statement is `True` (in the boolean logic sense). We can have multiple `elif` blocks if we want. We can also omit `elif` and `else` blocks altogether.

We can also test more complicated comparisons using various comparison operators:
![https://introcs.cs.princeton.edu/python/appendix_cheatsheet/images/ComparisonOperators.png](https://introcs.cs.princeton.edu/python/appendix_cheatsheet/images/ComparisonOperators.png)

For numbers, we can use `>`, `>=`, `==`, `<`, and `<=` to make numeric comparisons. If we want to modify or chain together boolean statements, we can use `and`, `or`, and `not`:

```python
x = 5
y = -1
if x>0 and y<0:
    print("both expressions true")
```

For strings, we can use use `==` for comparison and some special operators like `in` to see if one string exists inside of another.

```python
if 'I' in 'TEAM':
    print('at least one')
else:
    print('no')
```

If a variable is the special `None` object, an empty string (""), or the numeric value zero, it evaluates as boolean `False`. Otherwise, it is `True`.

```python
fundamentals = ''
if fundamentals:
    print('Yay!')
else:
    print('Nooo...')
```

We can also test the equality of two variables in an if statement:
```python
top_tool2015 = 'Gephi'
top_tool2019 = 'Python'
if top_tool2015 != top_tool2019:
    print('Change over time')
else:
    print('More they stay the same')
```

For more information about control flow, read the [Python documentation on the topic](https://docs.python.org/3/tutorial/controlflow.html).

We'll go over all of this in class with exercises, but bring additional questions too!!