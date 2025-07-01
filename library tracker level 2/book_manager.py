from tabulate import tabulate
def add_book(book):
    print("----Give Book Details To Add----")
    title = input("Title:").strip()
    author = input("Author:").strip()
    genre = input("Genre:").strip()
    year = input("Year:").strip()
    rating = input("Rating:").strip()
    country = input("Country:").strip()

    record = {
        "title":title,
        "author":author,
        "genre":genre,
        "year":year,
        "rating":rating,
        "country":country
    }
    book.append(record)
    print(f"\nBook {title} added")
def view_book(book):
    if not book:
        print("\n No book found")
        return
    headers = ["title","author","genre","year","rating","country"]
    rows = [[b.get(h, '') or "" for h in headers] for b in book]
    print("\n"+ tabulate(rows, headers = headers, tablefmt= "grid") + "\n")

