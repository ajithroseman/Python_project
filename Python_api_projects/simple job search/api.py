def fetch_jobs(role, location):
    print(f"searching for role {role} in location {location}")
    mock_jobs = [
        {"title":"python developer","company":"TCS","location":"chennai"},
        {"title":"backend developer","company":"INFOSYS","location":"bangalore"},
        {"title":"system engineer","company":"WIPRO","location":"hyderabad"},
        {"title":"web developer","company":"HCL","location":"chennai"}
    ]
    results = [job for job in mock_jobs if role.lower() in job["title"].lower() and location.lower() in job["location"].lower()]
    return results