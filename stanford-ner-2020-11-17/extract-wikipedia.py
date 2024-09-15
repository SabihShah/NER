import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page for Fawad Khan
url = 'https://en.wikipedia.org/wiki/Fawad_Khan'

# Make a request to fetch the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the main content area where the text is stored
    content = soup.find('div', {'class': 'mw-parser-output'})

    # Extract text from paragraph tags within the main content
    paragraphs = content.find_all('p')

    # Join all the paragraphs into a single block of text
    article_text = "\n".join([para.get_text() for para in paragraphs])

    # Save the article text to a file
    with open('wikipedia.txt', 'w') as f:
        f.write(article_text.strip())
    
    # Count the number of words in the extracted text
    word_count = len(article_text.split())
    print(f"The article contains {word_count} words.")

    # Check if the word count is at least 500
    if word_count >= 500:
        print("The article meets the minimum requirement of 500 words.")
    else:
        print("The article does not meet the minimum requirement of 500 words.")
else:
    print(f"Failed to retrieve the Wikipedia page. Status code: {response.status_code}")
