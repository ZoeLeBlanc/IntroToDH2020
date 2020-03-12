## Introduction to Python (Continued)

### FIRST EXERCISE (in class)

Work together to figure how to use the data types, structures, and methods we discussed to solve these prompts:
1. Get everyone's first names. Create a data structure to hold one name and then add each person's name to the data structure. Whose name comes first? How would we change the order? How could we access an individual's name? How could we access the first two names?
2. Get everyone's favorite number (or age). Calculate the average number for the group (hint: average is sum of all numbers divided by number of people in the group. You might check if Python has a built )
3. Create a data structure to store each a set of movies (maybe your favorite techno-themed one? Think Blade Runner or Hackers). Update the structure to keep a count for each movie depending on how many people in the group have seen the movie. Make sure that you don't keep any movie that only has a count of one.


---

Python interpreter is great, but why might we not want to write all our code in the interpreter? What happens every time you quit?

SOLUTION:
1. Open Visual Studio Code
- Visual Studio Code is a Code Editor, for writing code. (Think like Microsoft Office for writing...)

2. Open your directory in Visual Studio Code and create a new file

```sh
touch first_script.py
```

You should see this file in Visual Studio Code. We're going to write your first code script! Feel free to enter some of what you wrote for the exercise, or copy this below:

```python
projects = ['Valley of the Shadow', 'American Panorama', 'Orlando Project']
digital_humanities = {
    'people': ['Susan Hockey', 'Father Robert Busa'],
    'tools': ['Python', 'Gephi', 'JavaScript', 'Mallet']
}
```

1. Now try running the file from your terminal
Make sure you are not in the python interpreter. Type:

```sh
python3 first_script.py
```
What happens?

![https://media.giphy.com/media/3KCOFfdqmptLi/giphy.gif](https://media.giphy.com/media/3KCOFfdqmptLi/giphy.gif)

Because we aren't in the interpreter any more, unless we tell the computer to output a value it won't show us any message (unless there's an error.)

One solution is the **print** method.

In first_script.py, add the line to the bottom of the script:
```python
print(projects)
```
This time you should see the list of projects.

Now try moving that line to the top of first_script.py and running the script again.

![https://media.giphy.com/media/qQI16x8tgp7nW/giphy.gif](https://media.giphy.com/media/qQI16x8tgp7nW/giphy.gif)

We've hit a problem. Let's break down what happened here. If the print statement was at the bottom of the script it worked, but if it was at the top it didn't. 

That's because the print statement within it's parentheses references the variable `digital humanities`, but we haven't defined that variable yet.

**Computers read code from top to bottom**


#### So what's the print statement?

Print is a *built-in Python method*, which means it comes installed with Python and we can use it whenever we are writing Python.

Print is used to literally print out values to the terminal, and it's one of many ways to find out the output of a Python script.

#### Built-In Methods

Print is one of many methods. Let's take a look at a few more.

1. Len()
In first_script.py, move the print statement back to the bottom of the script. Then above the print statement type:
```python
projects_numbers = len(projects)
print('how many DH projects do we have?', projects_numbers)
```
Then try running the code. You should first see our question followed by a number and then the list of projects.

The **len** method can return the length of any list, dictionary, or string in Python.

1. Type()
You might also want to know the **type** of your variable, whether it's a data type or a data structure. In first_script.py, add to the bottom of the script:
```python
print(type(projects), type(digital_humanities))
```
Once you run the script you should see that we have both a list and a dictionary. With print statements you can add multiple items as long as they are separated by commas, and you can use built-in methods inside the print statement, instead of assigning them to a variable first.

1. Input()
You can also get input from the terminal using the **input** method. In first_script.py, type the following at the bottom of the script:
```python
print('Enter your name:')
name = input()
print('Hello, ' + name)
```
![https://media.giphy.com/media/3o7buirYcmV5nSwIRW/giphy.gif](https://media.giphy.com/media/3o7buirYcmV5nSwIRW/giphy.gif)

*What did we just do?*
First we printed out a prompt. Then we assigned the input method to a variable, and then we printed out hello concatenated with the value of name. 

You've now used built-in methods before for both dictionaries and lists. But they exist for data types too.

#### Built-In Methods for Strings

1. Split()
The **split** method lets us split up a string and turn it into a list. In first_script.py, add the following:

```python
definition_of_dh = 'DH is 1) using new digital tools to do humanistic research and 2) using humanistic methods to analyze new digital tools.'
print(definition_of_dh)
print(definition_of_dh.split(''))
```
![dh definition](/week2/images/def_dh.png)

1. Join()
The **join** method lets us take a list and join all the values together.
```python
all_projects = ' '.join(projects)
print(all_projects)
```

1. Replace()
The **replace** method lets us find a string and replace it with another string. You can also specify how many times you want to replace a string.
```python
edited_definition_of_dh = definition_of_dh.replace('tools', 'people') 
print(edited_definition_of_dh)
```

1. Upper() and Lower()
The **upper** and **lower** methods return the entire string capitalized or lowercased respectively.
```python
print(definition_of_dh.upper(), definition_of_dh.lower())
```

You can find more information about string methods here
[https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp)


### Inline Commenting
Comments are especially useful--necessary!--for collaboration. Python is open source and its community of millions of coders often share in its permissive approach to intellectual property. Python as a whole is a giant collaborative project of which you are now members.

When you write particularly complicated logic or whenever you write new classes or functions (more on this later!), you should write a comment to explain yourself.

### Documentation

Python, as with virtually all other languages and complex codes, contains extensive documentation that covers all aspects of its use. This documentation is [easily accessible via the Internet](assets/MissionImpossible.m4v?raw=true).

[Python 3 Documentation](https://docs.python.org/3/)

Let's take a look at the specific documentation for strings:

[Python 3 Docs: Built-in Types: Strings](https://docs.python.org/3/library/stdtypes.html#string-methods)

Learning to read documentation is a critical skill for succeeding as a programmer. Happily, most of you, as graduate students, should already be literate.

## The Zen of Python
### What's the deal with Python? 
Type this into the Python interpreter:
```python
import this
```

Here's [one interpretation of Z of P](https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/).

Also, a DH answer: lots of DH projects are written in Python because of its simplicity and robust community and it's especially popular in areas like text analysis and machine learning.
