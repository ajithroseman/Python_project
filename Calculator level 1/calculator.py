from datetime import datetime
def perform_operation(history):
    print("Type 1 for add")
    print("Type 2 for sub")
    print("Type 3 for mul")
    print("Type 4 for div")
    choice = input("Enter your choice:")
    a = float(input("Enter 1st value:"))
    b = float(input("Enter 2nd value:"))
    result = None
    operation = ""
    if choice == '1':
        result = a+b
        operation = "arithmatic"
    elif choice == '2':
        result = a-b
        operation = "subtraction"
    elif choice == '3':
        result = a*b
        operation = "multiplication"
    elif choice == '4':
        if b == 0:
            print("enter 2nd value other than 0")
            return None
        result = a/b
        operation = "division"
    else:
        print("invalid option")
        return None
    print("result", result)
    record = {
        "operation":operation,
        "input":f"{a} and {b}",
        "result":result,
        "Time":datetime.now().strftime("%d-%m-%Y/-%H-%M-%S")
    }
    history.append(record)
    return result


