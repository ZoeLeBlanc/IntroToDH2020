##### Assignment 1
This is the first few lines from Project Gutenberg version of Jane Austen, which you can find [here](https://www.gutenberg.org/files/1342/1342-0.txt).

"The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever.  You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 *** START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE *** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."


We want to use this text, but we need to get rid of some of the metadata at the beginning and we want to replace some of the data. Create a script called `jane_austen_data_munging.py`

1. First save this text into a variable called `jane`

1. Figure out how to get rid of everything before `Produced by Anonymous Volunteers` and save everything after in a variable called `jane_cleaned` (**hint: check out the string method [split()](https://www.w3schools.com/python/ref_string_split.asp), it splits strings on certain characters and returns a list *** )

1. Replace all instances of `man` with `person`, and `wife` with `parther` in `jane_cleaned` (**hint: check out the string method [replace()](https://www.w3schools.com/python/ref_string_replace.asp)**)

BONUS:
4. Change your script so that you can give an input, and replace any word in the text with any other word. Output the changed text. 

##### Assignment 2

Using the DH Tools data from last week, rewrite your code so that we could add a few more entries.

1. Download and open the [`tools_dh_proceedings.csv`](https://github.com/ZoeLeBlanc/IntroToDH2020/blob/gh-pages/week3/tools_dh_proceedings.csv) file and get the next top ten tools, based on 2019 ratings.
   
2. Remember to add functionality to calculate the total field for each new tool.

3. Figure out a way to output all the information for a tool if you input their name. Remember to use for loops and conditions!

**BONUS**
1. Create a way to input any year and return the top tool.