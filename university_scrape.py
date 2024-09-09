import requests
from bs4 import BeautifulSoup
import re

url = "https://college.ai/Colleges/Georgia-Colleges.html"

# Send an HTTP request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <a> tags within <td> tags
    a_tags = soup.find_all('td')
    
    # Extract and print the text from <a> tags
    university_names = []
    for td in a_tags:
        a_tag = td.find('a', style="color: blue;")
        if a_tag:
            university_names.append(a_tag.text.strip())
    
    # Print the list of university names
    print(university_names)
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
