import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Fawad_Khan'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    content = soup.find('div', {'class': 'mw-parser-output'})

    paragraphs = content.find_all('p')

    article_text = "\n".join([para.get_text() for para in paragraphs])

    with open('wikipedia.txt', 'w') as f:
        f.write(article_text.strip())

    word_count = len(article_text.split())
    print(f"The article contains {word_count} words.")

    if word_count >= 500:
        print("The article meets the minimum requirement of 500 words.")
    else:
        print("The article does not meet the minimum requirement of 500 words.")
else:
    print(f"Failed to retrieve the Wikipedia page. Status code: {response.status_code}")
