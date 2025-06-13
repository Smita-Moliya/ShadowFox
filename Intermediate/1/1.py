import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('div', class_='quote')

print("Top Quotes:\n")

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f"{text} — {author}")
