# class DHTool:
#     """Contains methods for maintaining data related to a dh tool
#     Methods:
#     --------
#     add_authors
#     add_year_popularity
#     calculate_total_popularity
#     """
#     def __init__(self, name):
#         self.tool_name = name
#         self.authors = list()
#         self.year_values = dict()
#         self.total_value = 0


#     def add_authors(self, authors):
#         """Adds a list of authors of the DH Tool
#         Method argument:
#         -----------------
#         authors(list) -- A list of people who built the dh tool
#         """
#         if isinstance(authors, list) is False:
#             authors = [authors]

#         self.authors.extend(authors)


#     def add_year_popularity(self, year, value):
#         """Adds the popularity value for each year of the DH tool
#         Method argument:
#         -----------------
#         year(integer or string) -- A year 
#         value(integer) - Popularity value
#         """

#         self.year_values[str(year)] = value


#     def calculate_total_popularity(self):
#         """Calculate the total popularity for a tool
#         """

#         self.total_popularity = sum(self.year_values.values())
#         print(self.total_popularity)

#     def get_tool_info(self):
#         self.total_popularity = sum(self.year_values.values())
#         return [self.tool_name,self.authors,self.year_values,self.total_value]

# tools={}

# tools["python"]=DHTool("Python")
# tools["python"].add_authors("Guido van Rossum")
# tools["python"].add_year_popularity(2015, 9)
# print(tools["python"].add_year_popularity.__doc__) # To view the docstring for the method
# tools["java"]=DHTool("Java")
# tools["java"].add_authors("Guido van GUIDO")
# tools["java"].add_year_popularity(2015, 8)
# print(tools["java"].add_year_popularity.__doc__) # To view the docstring for the method

# print("\n\n")
# print(tools.keys())

# for key in tools.keys():
#     print(tools[key].get_tool_info())

class DHTool:
    """Contains methods for maintaining data related to a dh tool
    Methods:
    --------
    add_authors
    add_year_popularity
    calculate_total_popularity
    """
    def __init__(self, name):
        self.tool_name = name
        self.authors = list()
        self.year_values = dict()
        self.total_value = 0


    def add_authors(self, authors):
        """Adds a list of authors of the DH Tool
        Method argument:
        -----------------
        authors(list) -- A list of people who built the dh tool
        """
        if isinstance(authors, list) is False:
            authors = [authors]

        self.authors.extend(authors)


    def add_year_popularity(self, year, value):
        """Adds the popularity value for each year of the DH tool
        Method argument:
        -----------------
        year(integer or string) -- A year 
        value(integer) - Popularity value
        """

        self.year_values[str(year)] = value


    def calculate_total_popularity(self):
        """Calculate the total popularity for a tool
        """

        self.total_popularity = sum(self.year_values.values())
        print(self.total_popularity)

    def get_tool_info(self):
        self.calculate_total_popularity()
        hasTotal = True
        if len(vars(self)) == 4:
            self.total_popularity = 0
        print(vars(self))
            

    


a_tool = DHTool("Python")
a_tool.add_authors("Guido van Rossum")
a_tool.add_year_popularity(2015, 9)
a_tool.calculate_total_popularity()
a_tool.get_tool_info()

b_tool = DHTool("Javascript")
b_tool.add_authors("Brendan Eich")
b_tool.add_year_popularity(2015, 8)
b_tool.add_year_popularity(2016, 18)
b_tool.add_year_popularity(2017, 12)
b_tool.add_year_popularity(2018, 6)
b_tool.add_year_popularity(2019, 15)
b_tool.get_tool_info()
