@title[Python Fundamentals and Code Complexity]

#### Today's agenda

- Brief intro to Python Classes
- Python Libraries, Modules, and Virtual Environments
- What is code debugging??

---
#### Last week's code
```python
def make_tool_dict(name, value_2015):
    return {
        "2015":value_2015 ,
        "name":name,
    }

dh_tools= {
    "tool1": make_tool_dict("Python",9),
    "creator1": "Guido van Rossum"
}
```
---

*What if we wanted to add more metadata to each tool? Also what if we wanted to reuse our code in other scripts?*

---
#### Python Classes
```sh
>>> a = [1,2,3]
>>> type(a)
<class 'list'>
>>> b = "123"
>>> type(b)
<class 'str'>
```
---
#### Python Classes
```python
# Define a class
class noop:
    pass  # Pass means "Move along, please. Nothing to see here."

# Create an instance of the class and invoke it
noop()
```
---
#### Python Classes

*How could we rewrite our code into a Class?*

---
#### Python Classes
```python
class DHTool:
    def __init__(self, name):
        self.tool_name = name

a_tool = DHTool("Python")
a_tool.tool_name
```
---
#### Python Classes

Time to test this out! Copy the code from [`intro_classes.py`](https://github.com/ZoeLeBlanc/IntroToDH2020/blob/gh-pages/week4/intro_classes.py)

---
#### Python Classes

What's happening in the constructor `__init__` method?

```python

def make_dh_tool(name):
    dh_tool = dict() #Could also write {}
    dh_tool.tool_name = name
    dh_tool.authors = alist()
    dh_tool.year_values = dict()
    dh_tool.total_value = 0
```
---
#### Python Classes

What are the Class' methods? What is `add_authors`? 

What would happen if we decided to add an additional author of Python from the [list of core contributors](https://devguide.python.org/developers/)?

---
#### Python Classes

What does the `calculate_total_popularity` and `add_year_popularity` methods do?

What if we wanted to add a method for printing out an entire tool's information? (**hint** [stack overflow question about printing out classes](https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a/192207#192207))

---
### Quick Assignment
1. Try adding the `get_tool_info` method to our `DHTool` class and then call it in your script.
2. Try adding a second tool with all the relevant information, and then calculate it's total popularity and print out it's full information.
---
#### Python Libraries

🚨🚨This is just a *very* light intro to Classes🚨🚨

*So why do you need to know about them? Because of Python Libraries!!*

---
#### Python Libraries

Let's dig into the Python documentation to understand more! [Here's the Python Standard Library](https://docs.python.org/3/library/). We've already been using this documentation, but let's scroll down to the [Pathlib module](https://docs.python.org/3/library/pathlib.html). 
---
#### Python Libraries

Let's first take a look at the [source code!](https://github.com/python/cpython/blob/3.8/Lib/pathlib.py) Notice how it's organized, and try and find the documentation for the `class Path` (*hint* use control F)

---
#### Python Libraries

Let's take a look at the methods in the `class Path` [https://docs.python.org/3/library/pathlib.html#methods](https://docs.python.org/3/library/pathlib.html#methods). How would we would print out the current working directory using pathlib?

---
#### Import Modules

Up to now we've used built-in methods for Python, but now we're going to use 

---
#### Quick Assignment

1. Download Jane Austen's *Pride and Prejudice* from Project Gutenberg
2. Write out a script using Pathlib that prints out all the files in your current directory
3. Add logic so that the script only prints out the text files

---
#### File Input and Output

Up to now we've copy and pasted any data we need into our scripts, but what if we wanted to use the data from these text files? Python has a few different ways to do this, but let's use the Pathlib module!

---
#### Quick Assignment

1. Using the code we've written earlier to just print out text files, try using Pathlib to read in the text and assign it to a variable.
2. Using the code from last week, write a function that will replace all instances of `man` with `person`, and `wife` with `parther` 
3. Using Pathlib, assign this new text back to the textfile.

---
#### Virtual Environment

1. Check if you have pip installed [https://stackoverflow.com/questions/40868345/checking-whether-the-pip-is-installed](https://stackoverflow.com/questions/40868345/checking-whether-the-pip-is-installed)
2. Install Pipenv [https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv](https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv)

---
#### Setting up a virtual environment

[https://pipenv-fork.readthedocs.io/en/latest/basics.html](https://pipenv-fork.readthedocs.io/en/latest/basics.html)
```sh
pipenv shell
```
```sh
pipenv install <package>
```
---
#### Assignment for next week

1. Choose one of the packages we'll be looking at later in the class
2. Install it into your virtual environment
3. Post a short description of the package and a method you're interested in testing out onto our channel on Slack by Thursday

---
#### Sample packages

1. Pandas
2. Altair
3. Spacy
4. Scikit-Learn


---
#### Final thoughts

We've now encountered some relatively complex code concepts and you're starting to get a sense of what code ecosystems look like. What do you make of Dale Markowitz's article? What does debugging mean to you? 