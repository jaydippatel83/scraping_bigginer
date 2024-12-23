from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml') 
print(soup.prettify())

print(soup.find('h1'))
print(soup.find('p'))
print(soup.find('table'))
print(soup.find('table').find('thead'))
print(soup.find('table').find('tbody'))
print(soup.find('table').find('tbody').find('tr'))
print(soup.find('table').find('tbody').find('tr').find('td'))
    