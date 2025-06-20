from library import add_book,search_book,update_status
from utility import load_book,show_book,save_book
def main():
    book = load_book()
    while True:
        print("Press '1' to Add a new book")
        print("Press '2' to View all book")
        print("Press '3' to Search book")
        print("Press '4' to Update reading status")
        print("Press '5' to Exit")
        choice = input("Enter your choice:")
        if choice == '1':
            print("Add a new book")
            add_book(book)
            save_book(book)
        elif choice == '2':
            print("View book")
            show_book(book)
        elif choice == '3':
            print("Search book")
            search_book(book)
        elif choice == '4':
            print("Update reading status")
            update_status(book)
            save_book(book)
        elif choice == '5':
            show_book(book)
            print("Goodbye!")
            break
        else:
            print("Invalid Entry")
            return None
if __name__ == "__main__":
    main()
