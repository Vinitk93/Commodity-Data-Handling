# Commodity data, filtering and visualization

# Dataset (produce_csv.csv)

The data file consists of seven columns. The column headers are in the first row of the data file: Commodity followed by Date followed by Farm followed by the names of four American cities. In each data row, Commodity is the name of a fruit or vegetable, followed by the Date associated with the row which is followed by five prices in dollars.The dataset is named as 'produce_csv'.

# Filtering

For prices (formatted with $) it is necessary to remove the dollar sign character from the string and convert to float. This is easily done using the replace() method and converting to float: price = float(price.replace(‘$’,’’)) . This code simply replaces the ‘$’ with a null string (‘’).

The datetime module provides methods to convert date strings into datetime objects that can be used for sorting and filtering. The dates in our file are formatted with either one or two characters for the month and day. The year contains four characters. We can convert a string containing a date like this:
date = datetime.strptime(dateString,"%m/%d/%Y")

Here, the date variable is a datetime object. The method strptime stands for string parse time. The date format is given by the string “%m/%d/%Y” . The year format string (“%Y”) is upper-case because it is four digits. If the year were given as only two digits, the format string would have been lower-case (“%y”). Month and day are represented by lower case because, in our data, these numbers may be one or two digits.
To print a date, it must be converted from a datetime object back to a string. Passing a datetime object to the str() function yields both date and time in standard ISO format (yyyy-mm-dd hh:mm:ss). To obtain the original date format, we pass the datetime object and a format string into the strftime() method.

Converting the data: It ought to be clear that we need to traverse the data list to obtain each row and then traverse each row to access each item. This indicates the need for
nested for loops. 
Once all of the prices have been converted to float and the calendar dates have been converted to datetime objects, our data still needs to be converted from tabular format to be truly useful. If we were to convert the values in this table to data records, each record would have four attributes: commodity, date, location, and price. Every line of input data will generate five data records. After the data records have been created, the data is finally in a format we can use for analysis. 

# Data Selection

Each record in my data list is organized in this format: commodity, date, location, price. The values can be accessed using indices 0 through 3, respectively. Knowing this organization is important because the index of the data represents the type of data it is. Python’s built-in filter() function can be used to select the data records we want when we provide an appropriate lambda function. Alternatively, we could convert each data record to a dictionary and access each item in a data record with a key string: commodity, date, location, and price. In the source code line below, the lambda function identifies the records for a specific commodity and location. So, the list select will contain the prices recorded for the retail sale of Oranges in Chicago across all available dates. The filter function returns a filter object, so the source code line below
converts the filter object to a list.

Now we can collect the dates and prices for Oranges in Chicago from the select list using simple list comprehensions. These two lists can be used to visualize how the price of oranges in Chicago changed over time. 

Before we move on to plotting, we need to find out the maximum and minimum price because I will need to scale the prices so the so the maximum fits within 40 columns to get meaningful results. So I’ll multiply the price by 25 to get a nice graph in a maximum of 40 columns. 

At this point, we have gone through the process of reading a data file, converting the values to meaningful data types, transforming the format from tabular to individual data records, selecting individual data records for analysis, sorting them and generating a crude graph.

# Data Visualization

The matplotlib package contains several modules. The module that we will use to generate graphs is called pyplot. So we can import matplotlib.pyplot and give it a shorter name to work with (plt): import matplotlib.pyplot as plt. Now we can use the pyplot module to draw a graph showing the price of oranges in Chicago over time. 

Still, the y-axis should be formatted in currency with a dollar sign. To do this, we need to import another module called the matplotlib ticker.




