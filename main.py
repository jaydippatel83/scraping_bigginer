from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml') 
print(soup.prettify())
cards = soup.find_all('div', class_='card')

for card in cards:
    print(card.find('h2').text)
    print(card.find('p').text)
    print(card.find('a').text)