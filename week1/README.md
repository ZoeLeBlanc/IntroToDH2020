# Introduction to Command Line and Coding

### Start in the Terminal aka Your Command Line Interface

You've all already opened your terminal to get your computer set up, so find your terminal again and open it up.

The terminal is just a shell that takes code commands and the computer executes them, that's why it's also called the Command Line Interface. If you want to learn more, check out the [resouces](resources.md) 

### What is Command Line?
- Command Line might sounds a bit intimidating
- But ask yourself, how do you find files and manipulate files on your computer? Probably using Windows Explorer or Mac Finder, right?
- Command Line is a text-based way of doing the same thing you do with your files
- Command Line is used a lot in coding because we manipulate our code files and run them all in the terminal 

### Let's do an exercise together
1. Open the [cheatsheet](commandline_cheatsheet.md). Copying is encouraged in coding, so make sure you use the cheatsheet!


1. Create the following directory structure in your `workspace` directory.
    ```sh
    workspace
    +-- cli
        +-- practice
            +-- create
    ```
1. Enter into the `create` directory. Remember to use tab completion.
1. While in this directory, create a new file named `intro2DH`. 
    ```sh
    touch ../../intro2DH
    ```
1. Put some simple content in the file using the `echo` command.
    ```sh
    echo 'Coding is ...' > ../../intro2DH
    ```
1. Now use the `cat` command to read those contents.
    ```sh
    cat ../../intro2DH
    ```
1. Remove the `intro2DH` file you created earlier with the `rm` command.
1. `cd` back up to the `cli` directory.
1. Remove the `practice` directory and all of its contents.


### Any questions??


### First group exercise
[CORN MAZE COMMAND LINE](commandline_exercise.md)

![https://media.giphy.com/media/3osBLvsy3wSPWpx6Vi/giphy.gif](https://media.giphy.com/media/3osBLvsy3wSPWpx6Vi/giphy.gif)