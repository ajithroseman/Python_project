from tabulate import tabulate
import os
import json
def print_jobs_table(jobs):
    if not jobs:
        print("\nNo matching jobs found.\n")
        return
    headers = ["job title","company","location"]
    rows = [[job["title"],job["company"],job["location"]] for job in jobs]
    print("\n" + tabulate(rows, headers = headers, tablefmt="grid")+"\n")
def save_to_file(jobs, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(jobs, f, indent=2)
    print(f"\nSaved {len(jobs)} job(s) to {filepath}\n")