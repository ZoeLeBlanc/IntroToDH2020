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
