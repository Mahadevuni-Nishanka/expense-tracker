expenses = []

print("Welcome to Expense Tracker!")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        print("\nYour Expenses:")

        for expense in expenses:
            print(expense["category"], "-", expense["amount"])

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
