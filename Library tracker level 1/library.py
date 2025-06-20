from tabulate import tabulate
def add_book(book):
    title = input("Title:")
    author = input("Author:")
    genre = input("Genre:")
    status = input("Status:")
    rating = input("Rating:")
    notes = input("Notes:")
    record = {
        "Title":title,
        "Author":author,
        "Genre":genre,
        "Status":status,
        "Rating":rating,
        "Notes":notes
    }
    book.append(record)
def search_book(book):
    find_book = input("Enter the book to search:").lower()
    book_found = [b for b in book if find_book in b["Title"].lower()]
    if book_found:
        rows = [[b["Title"],b["Author"],b["Genre"],b["Status"],b["Rating"],b["Notes"]]for b in book_found]
        print("-------search results-------")
        print(tabulate(rows, headers=["Title","Author","Genre","Status","Rating","Notes"],tablefmt="grid"))
    else:
        print("book not found")
def update_status(book):
    status_update = input("Enter the book to update status:").lower()
    for b in book:
        if b["Title"].lower() == status_update:
            print(f"Current status: {b['Status']}")
            b["Status"] = input("Enter new status:")
            print("Status updated")
            return
    print("book not found!!!")
