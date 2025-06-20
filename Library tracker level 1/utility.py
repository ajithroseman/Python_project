import os
import json
from tabulate import tabulate
data_list = "data/saved_library.json"
def load_book():
    if not os.path.exists(data_list):
        return []
    with open(data_list,"r") as f:
        return json.load(f)
def save_book(book):
    os.makedirs(os.path.dirname(data_list),exist_ok=True)
    with open(data_list,"w") as f:
        json.dump(book, f ,indent=2)
def show_book(book):
    if not book:
        print("no books found")
        return
    rows = [[b["Title"],b["Author"],b["Genre"],b["Status"],b["Rating"],b["Notes"]] for b in book]
    print("--------library----------")
    print(tabulate(rows, headers=["Title","Author","Genre","Status","Rating","Notes"],tablefmt="grid"))
