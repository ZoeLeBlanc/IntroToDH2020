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
        # if isinstance(authors, list) is False:
        #     authors = [authors]

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
        """Return a tool's info"""
        return print(self.__dict__)


a_tool = DHTool("Python")
a_tool.add_authors(["Guido van Rossum"])
print(a_tool.authors)
a_tool.add_authors(["Joannah Nanjekye"])
print(a_tool.authors)
# a_tool.add_year_popularity(2015, 9)
# a_tool.calculate_total_popularity()
# print(a_tool.total_popularity)

# a_tool.get_tool_info()

# print(a_tool.add_year_popularity.__doc__) # To view the docstring for the method