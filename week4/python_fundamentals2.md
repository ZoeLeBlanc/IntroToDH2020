## Python Fundamentals 2

#### Classes
Python classes are great for storing complex data structures, but they can also be simple.

Here's how you define a simple class that does nothing.

```python
# Define a class
class noop:
    pass  # Pass means "Move along, please. Nothing to see here."

# Create an instance of the class and invoke it
noop()
```

What exactly gets invoked in this case since the class has no actual logic in it. For any class, when you invoke it, it executes the `__init__` method. Since our simplistic example above didn't define any logic for the built-in `__init__` method, nothing happened.

## Simple Class

Let's define a class that actually does something when it's initialized.

```python
class Zoo:
    def __init__(self, name):
        self.zoo_name = name

a_zoo = Zoo("Zoolandia")
a_zoo.zoo_name
```

The class instance is the first argument to **_any_** function defined in a class.

```python

class Zoo:
    """Contains methods for maintaining a Zoo

    Methods:
    --------
    build_habitat
    sell_family_ticket
    purchase_animal
    """
    def __init__(self, name):
        self.zoo_name = name
        self.animals = dict()
        self.habitats = set()
        self.visitors = list()


    def build_habitat(self, name, type):
        """Adds tuples to the habitats set in the format (name, type)

        Method arguments:
        -----------------
        name(string) -- The marketing name of the habitat
        type(string) -- The type of habitat (e.g. Saltwater, Savanna, Swamp, etc.)
        """

        self.habitats.add((name, type))


    def sell_family_ticket(self, family):
        """Adds an entire family to the list of visitors

        Method argument:
        -----------------
        family(list) -- A list of people in a family of visitors
        """

        self.visitors.extend(family)


    def purchase_animal(self, type, name):
        """Add an animal to the zoo

        Method arguments:
        -----------------
        type(string) -- The type of animal to add
        name(string) -- The given name of the animal
        """

        self.animals[name] = type


    def list_animals(self):
        """Lists all animals in the zoo

        Method arguments:
        n/a
        """

        [print(k + ' the ' + v) for k, v in self.animals.items()]


a_zoo = Zoo("Zoolandia")
a_zoo.purchase_animal("Tortoise", "Tommy")
a_zoo.list_animals()

print(a_zoo.list_animals.__doc__) # To view the docstring for the method
```

## Subclassing

In the previous example, we used strings to define an animal. Let's be more detailed in what an animal is by defining an `Animal` class.

```python
class Animal:
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species
        self.speed = 0
        self.legs = 0

    def get_name(self):
        return self.name

    def walk(self):
        print("Parent class walk method")
        self.speed = self.speed + (0.1 * self.legs)

    def set_species(self, species):
        self.species = species

    def get_species(self):
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(name, "Dog")

    def walk(self):
        self.speed = self.speed + (0.2 * self.legs)
```

A class is really useful to encapsulate both data and functions in a single cohesive unit.

# Additional Reading

1. [An Introduction to Python Classes and Inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
2. [Here is a very helpful video series on class inheritance](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)

#### Python Libraries

#### Importing Modules
Let's model a dog class that includes some simple logic to track mood.

```python
class Dog:

    def __init__(self, name, owner, breed, likes, dislikes):
        self.name = name
        self.owner = owner
        self.breed = breed
        self.likes = likes
        self.dislikes = dislikes
        
        # default mood value, range 0-5
        self.mood = 2

    def speak(self):
        if self.mood > 3:
            print("*nuzzle* *happy bark!*")
        elif self.mood > 1:
            print("*regular bark*")
        else:
            print("*grrrrr!*") 
    
    def stimulate(self, stimulus):
        if stimulus in self.likes and self.mood<5:
            self.mood += 1
        elif stimulus in self.dislikes and self.mood>0:
            self.mood -= 1

hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
hazel.stimulate("thunder")
hazel.stimulate("thunder")
hazel.speak()
hazel.stimulate("treats")
hazel.stimulate("treats")
hazel.speak()
hazel.stimulate("naps")
hazel.stimulate("raccoons")
hazel.speak()
```

When we call the constructor (`hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])`), we create a new dog object with the parameters we pass in and have the variable `hazel` point to it. We say that the object we created is an *instance* of the class Dog. The variable `hazel` is a *reference* to that instance. Two different variables can point to the same object. Two different objects that contain identical data are not the same.

For example:

```python
hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
hazel_clone = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])

print(hazel is hazel_clone)
hazel.likes.append("smells")
print("smells" in hazel_clone.likes)

hazel_clone = hazel
print(hazel is hazel_clone)
print("smells" in hazel_clone.likes)
```

The `is` operator returns True if the object is literally the same (that is, they have the same memory address) and false if they aren't. If we don't do anything special, printing an object will actually print its type and memory address.


One important thing to understand is that we already use classes even when we're not defining them. The class is the primary way that Python organizes its standard library and the wider ecosystem of external libraries. So when we do `file_input = open("text.txt","r")`, we get back a File Object that is defined as a class in the Python Standard Library. 

We can see why the properties of classes are so useful there: each File Object contains distinct data (the filename and the mode and all sorts of things under the hood) and methods that operate on that data.

## Imports are Important

We can easily bring classes into other code using the `import` keyword, which does some voodoo to allow us to use classes defined in other files. This is how we can use parts of the Python Standard Library that aren't directly built into the base language ([Random](https://docs.python.org/3/library/random.html) is an example that we've encountered before). It's also how we use modules written by other programmers from the larger Python community. More on that next week!

We can also use `import` to import our own classes. It gets complicated if we have to specify the path, so for now it's easier to open the Python interpreter inside the same directory to import.

We can try it out by going into the examples directory, where we have defined the Dog class inside of the file Dog.py.

```python
import Dog
hazel = Dog.Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
```

`import Dog` finds the Dog.py file and then we can create a new Dog object as above.

Alternatively, we can use the `from` convention to import the class Dog directly from the file Dog:

```python
from Dog import Dog
hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
```

#### Input and Output

## File Input

File IO is easy in Python using the [`open` built-in function](https://docs.python.org/3/library/functions.html#open).

To open a file for reading (input), we just do:

```python
input_file = open("text.txt","r")
text = input_file.read()
print(text)
input_file.close()
```

Here, we use the `open` function to open a file in mode "r" (read). `open` returns a [File Object](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) that provides methods for reading and writing. In this case, the `read` method reads in data from the `input_file` file object and stores it as a string in `text`.

At the end, we can close the file to save some memory, but even if we don't do it explicitly, Python will eventually catch on to the fact that it isn't being used anymore and do it for us. This isn't a huge concern unless you're opening thousands of files or the files you're opening are very, very large.

One convenient way to read files is to combine the file object with a for loop to read text files line by line.

```python
input_file = open("text.txt","r")
for line in input_file:
    print(line.upper())
input_file.close()
```
This will loop through the file, line by line, until it's closed.

Often, you'll see file handling used with the `with` keyword:

```python
with open("text.txt","r") as input_file:
    for line in input_file:
        print(line.upper())
```

This is functionally the same as our last example. The only difference is that the file is automatically closed at the end of the block. You can use whichever convention you like, but keep both in mind because they're both pretty common in the wild.

## File Output

File output is very similar. We just use mode 'w', which overwrites the file specified. We can also use 'x' (which only works for new files) or 'a' (which appends data at the end of the file). Read the [`open` docs](https://docs.python.org/3/library/functions.html#open) for all the details.

```python
f = open("text.txt","w")
for i in range(0,100):
    f.write(str(i**2)+"\n")
```

Here, there's something just a little tricky. `i` and `i**2` are  integers, but the file object in this case expects a string. If we try to use `f.write(i**2)` instead, we'll get an error: `TypeError: write() argument must be str, not int`.

To get around this, we can convert from int to string using the built-in `str` class constructor `str()` to create a new string that's the *string representation* of the integer we pass in. So even though the inteher 4 and the string "4" look the same, they're different objects and different ways to represent data.

For the same reason that we can't do `f.write(4)`, we also can't do `"4"+4` (or, for that matter, `4+"4"`). We have to explicitly tell python whether we want it to treat each value as an integer or a string. `"4"+str(4)` produces "44" while `int("4")+4` returns 8.

The second new thing here is the newline character "\n", which is technically called a LF or Line Feed. This inserts a line break between characters in a string.

## Putting it Together

Here's part of Emily and Eleanore's solution to one of last week's assignments. Let's ignore the part where we chop off the front matter and focus on just the word replacement.

```python
jane = 'The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 *** START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE *** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.'
jane = jane.replace("man","person").replace("wife","partner")
print(jane)
```

Let's say that we want to "modernize" every classic book on Project Guttenberg. The first step is to write a program to read a single book in, replace the words, and then write it back out to a file.

I've pushed the Guttenberg version of Pride and Prejudice as a text to this repository, under the `Week07/examples` directory and the skeleton of the code needed to convert the text:

```python
filename = "pg42671.txt"

### input code goes here

jane = jane.replace("man","person").replace("wife","partner")

### output code goes here
```
