from tabulate import tabulate
def filter_book(book):
    if not book:
        print("No book to filter")
    print("\nFilter by")
    print("1.Genre")
    print("2.Rating")
    print("3.Year")
    choice = input("Enter your choice:").strip()
    key_map = {"1":"genre","2":"rating","3":"year"}
    key = key_map.get(choice)
    if not key:
        print("Invalid choice")
        return
    value = input(f"Enter {key} to filter by: ").strip()
    filtered = [b for b in book if b.get(key, "").lower() == value.lower()]
    if not filtered:
        print("\nNo matching books found.\n")
        return
    headers = ["title","author","genre","year","rating","country"]
    rows = [[b.get(h, "") or "" for h in headers] for b in filtered]
    print("\n" + tabulate(rows, headers=headers, tablefmt="grid") + "\n")
def sort_book(book):
    if not book:
        print("No book to sort")
        return
    print("\nSort by")
    print("1.Title")
    print("2.Rating")
    print("3.Year")
    choice = input("Enter your choice:").strip()
    key_map = {"1":"title","2":"rating","3":"year"}
    key = key_map.get(choice)
    if not key:
        print("Invalid choice")
        return
    sorted_book = sorted(book, key=lambda x: x.get(key) or "")
    headers = ["title","author","genre","year","rating","country"]
    rows = [[b.get(h,"") or "" for h in headers] for b in sorted_book]
    print("\n" + tabulate(rows, headers=headers, tablefmt="grid") + "\n")