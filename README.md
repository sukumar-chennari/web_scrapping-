# web_scrapping-

**Steps to run file**:
---------------------
1. Install the required libraries if needed with command
    pip install selenium pandas beautifulsoup4
2. Run the python file
   python myScrapping.py
3. You can observe the cvs and json files creatd in the working directoy or folder .


**Task:**

1. Scrape a minimum of 50 job postings from Microsoft, Google, Amazon 's LinkedIn  jobs, for the last one week from the following links: (
https://www.linkedin.com/jobs/search?location=India&geoId=102713980&f_C=1035&position=1&pageNum=0,
https://www.linkedin.com/jobs/search?keywords=&location=India&geoId=102713980&f_C=1441,  
https://www.linkedin.com/jobs/search?keywords=&location=India&geoId=102713980&f_TPR=r86400&f_C=1586&position=1&pageNum=0).
2. For each job, extract the following information:
    - Company_name
    - linkedin Job ID (you'll get in the URL)
    - Job title
    - Company
    - Location
    - Posted on (e.g., "Reposted 2 weeks ago")
    - Posted date (DD-MM-YYYY format) (e.g: today - 2 weeks ago)
    - Seniority level (eg:Entry level
    - Employment type (e.g., full-time)
    - **Note:** If any field is not available for a job, keep it as `null`.
3. Store the collected data in a JSON format, with each job represented as a separate JSON object and also in CSV.
4. Develop Python code to execute the scraping and data extraction process.
5. Host the code on a GitHub repository and share the link for code reivew.

**Additional Requirements:**

- Ensure the code is well-structured, commented, and adheres to Python coding best practices.
- Handle potential errors and exceptions gracefully.
- Consider using libraries like `selenium`, `Beautiful Soup`, `pandas`, and `requests` for efficient data handling.
- Respect LinkedIn's terms of service and rate limits.
- Use LinkedIn without logging in to avoid potential bans or impacts on your account.





here is a sample data:

{
  "company": "Microsoft",
  "job_title": "SDE II (Full Stack Engineer)",
  "linkedin_job_id": 3915786444,
  "location": "Noida, Uttar Pradesh, India",
  "posted_on": "Reposted 2 weeks ago",
  "posted_date": "26-07-2024",
  "Employment type":"Full-time",
  "Seniority level" :"Entry level"
}​
