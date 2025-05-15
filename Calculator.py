while True:
    x =input("Type 1 for add \n"
          "Type 2 for sub \n"
          "Type 3 for mul \n"
          "Type 4 for div \n"
          "Type -exit- to stop :")

    if x.lower() == 'exit':
        break
    if x not in ['1','2','3','4']:
        print("Please type 1 to 4")
        continue

    a = int(input("Enter 1st value :"))
    b = int(input("Enter 2nd value "))
    if x == '1':
        print("result :",a+b)
    elif x == '2':
        print("Result :",a-b)
    elif x == '2':
        print("Result :",a*b)
    elif x == '4':
        print("Result :",a/b)


