jane="The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 *** START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE *** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
jane_cleaned=jane.split("Produced by Anonymous Volunteers")
jane_cleaned=jane_cleaned[1]
print(jane_cleaned)
jane_cleaned=jane_cleaned.replace("man","person")
jane_cleaned=jane_cleaned.replace("wife","partner")
print(jane_cleaned)
old_word=input("Replace old word: ")
new_word=input("Word to replace it with: ")
jane_cleaned=jane_cleaned.replace(old_word,new_word)
print(jane_cleaned)


