import os
import json
from tabulate import tabulate
data_list = "data/history.json"
def load_history():
    if not os.path.exists(data_list):
        return []
    with open(data_list, "r") as f:
        return json.load(f)
def save_history(history):
    os.makedirs(os.path.dirname(data_list), exist_ok=True)
    with open(data_list, "w") as f:
        json.dump(history ,f, indent=2)
def show_history(history):
    if not history:
        print("no history found")
        return
    rows = [[h["operation"],h["input"],h["result"],h["Time"]] for  h in history]
    print("\ncalculation history")
    print(tabulate(rows, headers=["operation","input","result","time"],tablefmt="grid"))
