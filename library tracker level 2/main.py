from book_manager import add_book,view_book
from storage import load_book,save_book,export_to_csv
from filters import filter_book,sort_book
from stats import show_stat
def main():
    book = load_book()
    while True:
        print("----------Personal library------------")
        print("1.Add book")
        print("2.View All Book")
        print("3.Filter Books")
        print("4.Sort Books")
        print("5.View Stats")
        print("6.Export to csv")
        print("7.Exit")
        choice = input("Enter your choice:").strip()
        if choice == '1':
            add_book(book)
            save_book(book)
        elif choice == '2':
            view_book(book)
        elif choice == '3':
            filter_book(book)
        elif choice == '4':
            sort_book(book)
        elif choice == '5':
            show_stat(book)
        elif choice == '6':
            export_to_csv(book)
            print("Exported as csv file")
        elif choice == '7':
            save_book(book)
            print("Goodbye!!!")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
