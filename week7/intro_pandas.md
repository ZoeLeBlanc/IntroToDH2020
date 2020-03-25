## Introduction to Pandas and Jupyter Notebooks

So far when we've been writing Python code, we've either been using the Python interpreter in the terminal or saving a Python script. However, there's a third way to write Python code that's very popular in Digital Humanities - that is [Jupyter notebooks](https://jupyter.org/index.html).

*So what is a Jupyter notebook?*

> The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

The popularity of Jupyter notebooks is that it allows you to do *exploratory data analysis* in the browser, letting you manipulate data and see the results without have to rerun an entire script.

---
To be able to use Jupyter, we first need to install it as a Python library.

In your terminal *and* in the folder with your virtual environment, type the following:

```sh
pipenv install jupyter notebook
```

*If you're not using `pipenv`, then feel free to install the library with whatever virtual environment and package manager you prefer to use.*

![install libraries](install.png)

If you've installed successfully, you should see the following message in your terminal.

Now we can open up the Jupyter notebook in our browser with the following command.

```sh
pipenv run jupyter notebook
```

This command immediately opens the Jupyter interface in our browser.

![create notebook](create_notebook.png)

Our first step is to create a new Python 3 notebook using the `new` button.

![empty notebook](empty_notebook.png)

This opens up an empty notebook and we can rename the notebook by clicking on `Untitled`.

![rename notebook](rename_notebook.png)

I renamed my notebook `Introduction to Notebooks`.

Now in a Jupyter notebook, we can still use much of the same Python syntax as our scripts. For example, going back to our DH Tools script, we could still use our functions to store data about various DH tools.

Try pasting the following within the first cell of the Jupyter notebook:
```python
def make_tool_dict(name, value_2015 , value_2016, value_2017,value_2018, value_2019):
    tool = {
        "2015":value_2015,
        "2016":value_2016,
        "2017":value_2017,
        "2018":value_2018,
        "2019":value_2019,
        "name":name,
        "total":value_2015+value_2016+value_2017+value_2018+value_2019
    }
    return tool
```
It should look like the following:
![function](function.png)
Unlike with our scripts where we would need to save our file and then type `pipenv run python script.py`, we can just click on the cell and either press `Shift` + `Return` on a Mac or  `Shift` + `Enter` on Windows to run the cell.

You'll notice that it seems like nothing happened, though now there's a `1` next to the cell. That means that it the first cell run in the notebook, if you run it again, it will show `2`. 

Unlike with scripts, notebooks hold variables in memory, which means that our function now exists in the notebook and we can call in a new cell.

Add a new cell below our function one by pressing the `+` symbol in the tool bar. Then paste the following code and run it.

```python
make_tool_dict("Python",9,22,27,32,35)
```

You should now see output from the function below our code.

![call function](call_function.png)

Just like in a script if we want to save this output, we need to assign it to a variable.

Paste the following in a new cell.

```python
tool1 = make_tool_dict("Python",9,22,27,32,35)
```
Now when you run that cell, you'll see no output because we've stored in a variable. To check that our function worked you can either use the built-in `print()` method or simply type the variable in the cell.

![variable](variable.png)

To learn more of the shortcuts for Jupyter notebooks, go to the [shortcuts file](shortcuts.md).

Jupyter notebooks will autosave your notebook, but it's good to save it before leaving the notebook (you can save pressing the file icon).

To exit the notebook, you can either press the `Quit` button on the main page or type `Ctrl`+`c` in the terminal and selecting `yes` to quitting the notebook.

---

## Data in Jupyter Notebooks

Jupyter notebooks are particularly useful for working with tabular data (that is data in spreadsheets), especially with the Python Library Pandas.

Let's download Pandas and try it out in our Jupyter Notebook.

Type `pipenv install pandas` in the folder with you Pipfile and once it is installed, restart your notebook with `pipenv run jupyter notebook`.

First, let's create a new notebook.

![new notebook](new_notebook.png)

Now let's import Pandas into our notebook! Place the following code into our first cell and run it.

```python
import pandas as pd
```
We can check that this worked, by outputting the version of pandas, with the following:

```python
pd.__version__
```
Notice we used the `as` keyword. This is a built in feature of Python that lets us import libraries and give them shorter nicknames, so that we don't have to type `pandas` each time we want to use a feature of the library.

Now we're going to try reading in a spreadsheet to our notebook. We're going to be using the spreadsheet from "Film Dialogue" by *The Pudding* that is available here [https://docs.google.com/spreadsheets/d/1fbcldxxyRvHjDaaY0EeQnQzvSP7Ub8QYVM2bIs-tKH8/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1fbcldxxyRvHjDaaY0EeQnQzvSP7Ub8QYVM2bIs-tKH8/edit?usp=sharing). I'll post a version of the spreadsheet in Slack so that you can easily download it. **Be sure to put the file within the folder of your Jupyter notebook.**

Once we have this file, we can read it into our notebook so that we can access the data using the built-in method from pandas called `read_csv()`.

Paste the following code into a new cell:
```python
film_scripts = pd.read_csv('pudding_public_scripts.csv')
```
Before we explore the variable `film_scripts`, we can also learn a bit more about `read_csv()`, using Pandas built-in `help()` method.

Below `film_scripts`, paste:

```python
help(pd.read_csv)
```
![help](help.png)

This function prints out the documentation for this method, which is useful in case you have questions. Alternatively, we can always use the Pandas documentation [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

So now let's inspect `film_scripts`.

First, we can test what the variable contains by using `type(film_scripts)`, which tells us that it a `pandas.core.frame.DataFrame`.

Dataframes are the primary data structures in Pandas (think like dictionaries or lists) and are defined as "a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects." You can read more about them here [https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe](https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe)

We can then display the data in the dataframe a few different ways.

First, we can type the variable `film_scripts` into a cell, which shows us the columns and a few rows, though much of the dataframe is truncated.

We can also type `film_scripts.head()`, which prints out the first few rows or `film_scripts.sample()` which prints out a random sample of rows.

![display data](display_data.png)

We might also want to explore the size of our dataset, as well as the types of data it contains.

![size](size.png)

We can use the `shape` and `dtypes` attributes that are built-in on the DataFrame Class. `shape` tells us that we have 2000 rows and 6 columns, while `dtypes` tells us the data types of each of those columns.

Pandas data types build from ones available in Python. This tables compares Pandas to Python and another library called Numpy. 

| Pandas dtype | Python type | NumPy type | Usage|
|:----------:|:----------:|:----------:|:----------:|
|object | str or mixed | string_, unicode_, mixed types	|Text or mixed numeric and non-numeric values |
int64	| int	| int_, int8, int16, int32, int64, uint8, uint16, uint32, uint64 | 	Integer numbers |
float64	| float	| float_, float16, float32, float64	|Floating point numbers |
bool |	bool |	bool_	| True/False values |
datetime64 |	NA|	datetime64[ns]|	Date and time values
timedelta[ns]	|NA |	NA |	Differences between two datetimes |
category|	NA|	NA	|Finite list of text values|

You'll notice that some of the data types are only available in Pandas. It's important to check what data types exist in your columns, since it informs the types of data manipulation you can do with your dataset.

Let's explore the `link` column. To access a particular column in Pandas, we can use a few different syntaxes. Try typing in one cell `film_scripts['link']` and then in the following cell `fiml_scripts[['link]]`. What differences do you notice?

![columns](columns.png)

The difference in the output for each of these syntaxes has to do with how Pandas handles `indexing` (as a refresher, we index in Python using single square brackets).

