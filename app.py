from datetime import datetime

transactions = []


def AddTransactions():
    print("\n")
    amount = input("Enter Amount:")
    category = input("Category: Food, other:").lower()
    transactionType = input("Type: income/expense:").lower()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transactions.append({
        "date": date,
        "amount": amount,
        "category": category,
        "type": transactionType
    })
    print(transactions)
    Menu()


def ViewTransactions():
    print("\n")
    Menu()


def ViewSummary():
    print("\n")
    print("Viewing Summary...")
    print("\n")
    Menu()


def Menu():
    print("=== Personal Budget Tracker ===")
    print("1. Add Transactions")
    print("2. View Transactions")
    print("3. View Summary")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        AddTransactions()
    elif choice == '2':
        ViewTransactions()
    elif choice == '3':
        ViewSummary()
    elif choice == '4':
        print("Exiting the app")
        return
    else:
        print("Invalid choice. Please try again.")
        Menu()


Menu()
