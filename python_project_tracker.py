import os

FILENAME = 'expenses.txt'

def initialize_file():
    
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w') as file:
            file.write("Description,Amount\n")
        print(f"Created {FILENAME} to store your expenses.\n")

def add_expense():
    description = input("Enter expense description: ").strip()
    amount = input("Enter amount: ").strip()
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return
    
    with open(FILENAME, 'a') as file:
        file.write(f"{description},{amount}\n")
    print("Expense added successfully!\n")

def view_expenses():
    print("\n--- All Expenses ---")
    with open(FILENAME, 'r') as file:
        lines = file.readlines()
        

        if len(lines) <= 1:
            print("No expenses recorded yet.\n")
            return
        
        print("No.\tDescription\tAmount")
        print("-------------------------------")
        
       
        for index, line in enumerate(lines[1:], start=1):
            description, amount = line.strip().split(',')
            print(f"{index}\t{description}\t\t${float(amount):.2f}")
    print()

def display_menu():
    print("===== Simple Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Exit")

def main():
    initialize_file()
    print("Welcome to the Simple Expense Tracker!\n")
    for _ in range(1000):  
        display_menu()
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()