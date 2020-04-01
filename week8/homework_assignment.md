#### Week 8 Homework Assignment

In class, we worked on getting the text from the *Humanist* listserv through web scraping (check out the [Jupyter notebook from our class](Pandas%20Web%20Scraping%20Humanist.ipynb)).

The final piece of this assignment is to take the data from the plain text files and save it to a dataframe in Pandas. Going forward we'll be using this dataset to do some initial text analysis.

If you feel comfortable with assignment, feel free to go ahead and use either scripts, notebooks, or a combination of both.

---
For those looking for my guidance, let's break down the assignment into finite steps.

1. With the existing code in the notebook, we have access to each of the html and text from each of the plain text volumes. Do we want to keep the html? Or do we just want the text? (*hint* try googling for the `get_text()` method in Beautiful Soup)
2. Now that we have the data from the webpage, we need to decide what other metadata we want to include with it. What information can we get from the `url` variable? How would you get the years for each volume? (*hint* checkout the `split()` method in Python)
3. Finally we have all the data we want to store, so now we have to decide how to persist it? If we have metadata and data for each volume what data structure would be best suited? A list or a dictionary? What about a list of dictionaries? How would we add data from each volume to a variable that lived outside of the two for loops?
4. Say we got our metadata and data saved to a new variable, the final piece is to save this to a new dataframe. Read this Stack Overflow answer for how to save our variable to a dataframe [https://stackoverflow.com/questions/20638006/convert-list-of-dictionaries-to-a-pandas-dataframe/53831756#53831756](https://stackoverflow.com/questions/20638006/convert-list-of-dictionaries-to-a-pandas-dataframe/53831756#53831756). Try and find the reference to `from_records()`, `from_dict()`, and `orient=columns` in the answer, and try to save our variable to new a dataframe called `humanist_vols`.
5. Finally, so we don't have to web scrape every time, try using the following code:

```python
humanist_vols.to_csv('web_scraped_humanist_listserv.csv')
```

What does this do to our data? You can read about the `to_csv()` method here [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv#pandas.DataFrame.to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv#pandas.DataFrame.to_csv).

If you get stuck don't worry we'll go over the code in class, but feel to Slack the instructor for help too!