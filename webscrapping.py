Parsing HTML with BeautifulSoup
In this interactive exercise, you'll learn how to use the BeautifulSoup package to parse, prettify and extract information from HTML. You'll scrape the data from the webpage of Guido van Rossum, Python's very own Benevolent Dictator for Life. In the following exercises, you'll prettify the HTML and then extract the text and the hyperlinks.

The URL of interest is url = 'https://www.python.org/~guido/'.

Instructions
100 XP
Import the function BeautifulSoup from the package bs4.
Assign the URL of interest to the variable url.
Package the request to the URL, send the request and catch the response with a single function requests.get(), assigning the response to the variable r.
Use the text attribute of the object r to return the HTML of the webpage as a string; store the result in a variable html_doc.
Create a BeautifulSoup object soup from the resulting HTML using the function BeautifulSoup().
Use the method prettify() on soup and assign the result to pretty_soup.
Hit submit to print to prettified HTML to your shell!


# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url='https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r=requests.get(url)

# Extracts the response as html: html_doc
html_doc=r.text

# Create a BeautifulSoup object from the HTML: soup
soup=BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup=soup.prettify()

# Print the response
print(pretty_soup)




Turning a webpage into data using BeautifulSoup: getting the text
As promised, in the following exercises, you'll learn the basics of extracting information from HTML soup. In this exercise, you'll figure out how to extract the text from the BDFL's webpage, along with printing the webpage's title.

Instructions
100 XP
In the sample code, the HTML response object html_doc has already been created: your first task is to Soupify it using the function BeautifulSoup() and to assign the resulting soup to the variable soup.
Extract the title from the HTML soup soup using the attribute title and assign the result to guido_title.
Print the title of Guido's webpage to the shell using the print() function.
Extract the text from the HTML soup soup using the method get_text() and assign to guido_text.
Hit submit to print the text from Guido's webpage to the shell.

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup=BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title=soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text=soup.get_text()

# Print Guido's text to the shell
print(guido_text)
