import os
import json
import csv

data_list = "data/saved_book.json"
def load_book():
    if not os.path.exists(data_list):
        return []
    with open(data_list, "r") as f:
        return json.load(f)
def save_book(book):
    os.makedirs(os.path.dirname(data_list), exist_ok=True)
    with open(data_list, "w") as f:
        json.dump(book, f, indent=2)
def export_to_csv(book):
    os.makedirs("data", exist_ok=True)
    with open("data/saved_csv_book.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title","author","genre","year","rating","country"])
        writer.writeheader()
        writer.writerows(book)