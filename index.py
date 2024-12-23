from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=blockchain&cboWorkExp1=2&txtLocation='
response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')
jobs_cards = soup.find('li', class_='clearfix job-bx wht-shd-bx')

for job_card in jobs_cards: 
    job_company = job_card.find('h2', class_='heading-trun').text
    job_location = job_card.find('ul', class_='list-job-dtl clearfix').find('li').text
    print(job_company, job_location)
