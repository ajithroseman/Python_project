from calculator import perform_operation
from utility import load_history, save_history, show_history
def main():
    history = load_history()
    while True:
        print("1. for calculation ")
        print("2. for history")
        print("3. for exit")
        choice = input("Enter your choice:")
        if choice == '1':
            output = perform_operation(history)
            if output is not None:
                save_history(history)
        elif choice == '2':
            show_history(history)
        elif choice == '3':
            save_history(history)
            print("goodbye")
            break
        else:
            print("invalid choice")
if __name__ == '__main__':
    main()


