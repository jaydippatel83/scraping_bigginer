from bs4 import BeautifulSoup
import requests
import time

print("Enter the job title: ")
job_title = input('>')
print("Enter the location: ")
location = input('>')
print('Searching for jobs...')

def get_jobs():
    
    url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords={job_title}&cboWorkExp1=2&txtLocation={location}'
    response = requests.get(url).text

    soup = BeautifulSoup(response, 'lxml')

    # Find all job listings
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # Loop through each job
    for index, job in enumerate(jobs):
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
            
            if skills is not None:
                 with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Info: {more_info.attrs['href']}\n")

                 # Print the extracted details
            print(f"Job {index + 1} details saved to posts/{index}.txt")
if __name__ == '__main__':
    while True:
        get_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait * 60)
