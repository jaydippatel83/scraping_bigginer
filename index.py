from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=blockchain&cboWorkExp1=2&txtLocation='
response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')

# Find all job listings
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# Loop through each job
for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text

    # Filter jobs posted a few days ago
    if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills_element = job.find('span', class_='srp-skills')
        if skills_element:
            skills = skills_element.text.replace(' ', '')
        else:
            skills = None  # Handle the case where the element is not found
        more_info = job.header.h2.a

        # Print the extracted details
        print(f"Company Name: {company_name}")
        print(f"Required Skills: {skills}")
        print(f"More Info: {more_info.attrs['href']}")