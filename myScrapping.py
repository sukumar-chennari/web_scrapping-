import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

# Configure WebDriver
chrome_opts = Options()
chrome_opts.add_argument("--headless")  # Run in headless mode
chrome_opts.add_argument("--no-sandbox")
chrome_opts.add_argument("--disable-dev-shm-usage")

# Path to WebDriver executable
#path_to_driver = 'C:/Program Files/chromedriver-win64/chromedriver.exe'
path_to_driver = "C:/chromedriver-win64/chromedriver.exe"
service = Service(path_to_driver)
browser = webdriver.Chrome(service=service, options=chrome_opts)

# List of LinkedIn job search URLs
job_urls = [
    "https://www.linkedin.com/jobs/search?location=India&geoId=102713980&f_C=1035&position=1&pageNum=0",
    "https://www.linkedin.com/jobs/search?keywords=&location=India&geoId=102713980&f_C=1441",
    "https://www.linkedin.com/jobs/search?keywords=&location=India&geoId=102713980&f_TPR=r86400&f_C=1586&position=1&pageNum=0"
]

# Utility function to parse posted date
def convert_posted_date(posted_text):
    """Converts the relative posted date to an absolute date."""
    current_date = datetime.now()
    lower_text = posted_text.lower()

    if 'today' in lower_text:
        return current_date.strftime("%d-%m-%Y")
    elif 'week' in lower_text:
        try:
            num_days = int(lower_text.split(' ')[0])
            return (current_date - timedelta(days=num_days)).strftime("%d-%m-%Y")
        except ValueError:
            return None
    elif 'month' in lower_text:
        try:
            num_months = int(lower_text.split(' ')[0])
            return (current_date - timedelta(days=num_months * 30)).strftime("%d-%m-%Y")
        except ValueError:
            return None
    elif 'day' in lower_text:
        try:
            num_days = int(lower_text.split(' ')[0])
            return (current_date - timedelta(days=num_days)).strftime("%d-%m-%Y")
        except ValueError:
            return None
    return None

# Function to extract job details
def extract_job_details(job_card):
    """Extracts the job details from the job card element."""
    job_info = {}

    # Extract company name
    try:
        company = job_card.find("h4", class_="base-search-card__subtitle").find("a").get_text(strip=True)
    except AttributeError:
        company = None
    job_info["company_name"] = company

    # Extract job title
    try:
        title = job_card.find("h3", class_="base-search-card__title").get_text(strip=True)
    except AttributeError:
        title = None
    job_info["job_title"] = title

    # Extract LinkedIn job ID
    try:
        job_id = job_card.find("a", {"data-tracking-control-name": "public_jobs_jserp-result_search-card"})["href"].split("/")[-2]
    except (AttributeError, IndexError):
        job_id = None
    job_info["linkedin_id"] = job_id

    # Extract location
    try:
        job_location = job_card.find("span", class_="job-search-card__location").get_text(strip=True)
    except AttributeError:
        job_location = None
    job_info["job_location"] = job_location

    # Extract posted date
    try:
        post_date = job_card.find("time", class_="job-search-card__listdate--new").get_text(strip=True)
        formatted_date = convert_posted_date(post_date)
    except AttributeError:
        post_date = None
        formatted_date = None
    job_info["posted_date_text"] = post_date
    job_info["posted_date"] = formatted_date

    # Placeholder for employment type
    emp_type = None  # Could be updated with the correct class if available
    job_info["employment_type"] = emp_type

    # Placeholder for seniority level
    seniority = None  # Could be updated with the correct class if available
    job_info["seniority_level"] = seniority

    return job_info

# Function to scrape jobs from a LinkedIn URL
def scrape_linkedin_jobs(search_url):
    """Scrapes job postings from a given LinkedIn URL."""
    browser.get(search_url)
    time.sleep(5)  # Wait for the page to load
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    job_cards = soup.find_all("div", {"class": "job-search-card"})

    job_list = []
    for card in job_cards:
        job_details = extract_job_details(card)
        if job_details:
            job_list.append(job_details)

    return job_list

# Main execution
all_job_listings = []
for job_url in job_urls:
    job_list = scrape_linkedin_jobs(job_url)
    all_job_listings.extend(job_list)

# Save scraped data to JSON
with open('linkedinJobsData.json', 'w') as json_outfile:
    json.dump(all_job_listings, json_outfile, indent=4)

# Save scraped data to CSV
job_df = pd.DataFrame(all_job_listings)
job_df.to_csv('linkedinJobsData.csv', index=False)

# Cleanup
browser.quit()

print("Job scraping completed successfully. Data saved to linkedinJobsData.json and linkedinJobsData.csv.")