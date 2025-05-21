import requests
import pandas as pd

# ------------------------
# 🔑 Replace with your actual API key from RapidAPI
API_KEY = "your-api-key-here"  # Be sure to replace this with your own API key
# ------------------------

# 🌍 The URL of the API endpoint
url = "https://jsearch.p.rapidapi.com/search"

# ✍️ Input: Ask user for job title and location
job_title = input("Enter job title (e.g., Data Scientist): ")
location = input("Enter location (e.g., Toronto): ")

# 👨‍💻 Headers for API request
headers = {
    "X-RapidAPI-Key": API_KEY,  # Replace with your RapidAPI key
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"  # JSearch API host
}

# 🔎 Parameters for the job search request
params = {
    "query": f"{job_title} in {location}",  # Combine job title and location for query
    "page": 1,           # Start from page 1 for job listings
    "num_pages": 20      # Fetch up to 20 pages of job results (you can adjust this, the lower the faster)
}

# 🔍 Sending a GET request to the JSearch API with the specified headers and params
response = requests.get(url, headers=headers, params=params)

# ✅ If the request is successful (status code 200), process the data
if response.status_code == 200:
    data = response.json()["data"]  # Extract the list of jobs from the API response
    job_list = []  # Create an empty list to store the job information

    # 👩‍💻 Loop through each job listing and extract relevant data
    for job in data:
        job_list.append({
            "Job Title": job.get("job_title"),                # Job title
            "Company": job.get("employer_name"),               # Company name
            "Location": job.get("job_city"),                   # Job location (city)
            "Employment Type": job.get("job_employment_type"), # Employment type (full-time, part-time, etc.)
            "Posted": job.get("job_posted_at_datetime_utc"),   # Date the job was posted
            "Link to Apply": job.get("job_apply_link")         # URL to apply for the job
        })

    # 🔄 Convert the job list into a pandas DataFrame for easy handling
    df = pd.DataFrame(job_list)

    # 💾 Save the DataFrame to a CSV file
    df.to_csv("toronto_jobs.csv", index=False)  # Save the results to 'toronto_jobs.csv'
    print("✅ Jobs saved to 'toronto_jobs.csv'. Open the file to view the listings.")

else:
    # If the request was not successful, print the status code
    print("❌ Failed to fetch jobs. Status code:", response.status_code)
