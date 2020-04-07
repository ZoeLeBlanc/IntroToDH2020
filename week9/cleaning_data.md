# Cleaning and Preparing (Text) Data for Analyses

Before undertaking any type of data analysis ( whether humanities or exploratory), we need to both understand our data (think producing a data biography) and often *clean* it.

*So what does it mean to clean data?*

The term cleaning data refers to a whole set of transformations that you may or may not decide to undertake. So why would someone clean data? Remember in the "Data Biographies" article by Heather Krause, she discussed subsetting the data to just the data from Rwanda since it was the most consistent across the time period and in its collection - this is a type of data cleaning, in this case selecting a subset of data. Krause made this selection because otherwise there was too much variability in the *data quality* to perform their analyses.

Cleaning data can also mean normalizing distributions, removing null values, and even transforming some of the data to standardize it. But regardless of what you choose to do, the reason to undertake this step is because of the concept of **GIGO**.

![gigo](https://www.harrised.com/150/images/gigo.jpeg)

GIGO stands for "Garbage In, Garbage Out" (to read more about the origins of GIGO, read this article [https://www.atlasobscura.com/articles/is-this-the-first-time-anyone-printed-garbage-in-garbage-out](https://www.atlasobscura.com/articles/is-this-the-first-time-anyone-printed-garbage-in-garbage-out)). GIGO is important because it essentially means that the quality of your data analysis is always dependent on the quality of your data.

One thing to remember with datasets is that the act of collecting data is in of itself an interpretation. And so cleaning data adds another layer of interpretation (sometimes many layers) to the dataset, which is why its crucial to keep a record of how you transform your data.

However, it is also important to realize that even with cleaning you will never have a *perfect* dataset. In humanities data analysis, data cleaning is somewhat controversial because it means distorting the original source material (you can read more about this controversy in [Katie Rawson and Trevor Muñoz, “Against Cleaning”, *Debates in DH* 2019](https://dhdebates.gc.cuny.edu/read/untitled-f2acf72c-a469-49d8-be35-67f9ac1e3a60/section/07154de9-4903-428e-9c61-7a92a6f22e51)). So one of the considerations for any humanities data analysis is not only *how* to data clean, but *why* and to *what* degree.

---
### Exploratory Data Analysis with Pandas and Python

The first step in data cleaning is to not actual clean the data, but instead perform initial exploratory data analysis (EDA). We briefly discussed EDA in class, but here's the image from the class slides.

![eda](../week8/images/eda.png)


- summary statistics and finding out what's missing

- cover missing and null data in Pandas
- subsetting data
- removing duplicates

---
### Cleaning (Text) Data with Pandas and Python

- spelling normalization
- removing digits and characters
- punctuation
- stemming and lemmatization
- regular expression
  
- tokenizing data
- unigrams versus bigrams

- normalize data
