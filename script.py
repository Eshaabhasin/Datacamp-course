Importing Data in Python Intermediate



Now that you know the basics behind HTTP GET requests, it's time to perform some of your own. In this interactive exercise, you will ping our very own DataCamp servers to perform a GET request to extract information from the first coding exercise of this course, "https://campus.datacamp.com/courses/1606/4135?ex=2".

In the next exercise, you'll extract the HTML itself. Right now, however, you are going to package and send the request and then catch the response.

# Import packages
from urllib.request import urlopen,Request
# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request: request
request=Request(url)

# Sends the request and catches the response: response
response=urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()
