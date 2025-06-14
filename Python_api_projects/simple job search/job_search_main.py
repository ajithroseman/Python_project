from api import fetch_jobs
from utility import print_jobs_table,save_to_file
from resume_maker import generate_resume
def main():
    while True:
        print("\n-----job hunter------")
        print("1. Search jobs")
        print("2. Generate resume")
        print("3. Exit")

        choice = input("Enter your choice")
        if choice == '1':
            role = input("Enter role")
            location = input("Enter location")
            jobs = fetch_jobs(role, location)
            if jobs:
                print_jobs_table(jobs)
                save = input("Save results to file? (y/n):")
                if save.lower() == 'y':
                    save_to_file(jobs, "data/saved_jobs.json")
            else:
                print("No jobs found")
        elif choice == '2':
            generate_resume()
        elif choice =='3':
            print("goodbye")
            break
        else:
            print("Invalid choice. please try again")
if __name__ == '__main__':
    main()
