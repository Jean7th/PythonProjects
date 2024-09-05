import itertools

print("Welcome To The Expense Tracker Application!!! ✍️\n")

# * Increment Counter for ID
count = 0

def increment():
    global count
    count = count + 1
    return

def add_expense():
    try:
        id_count = int()
        amount = float(input("Enter The Amount: £"))
        if not amount:
            raise TypeError ("Cannot enter empty input.")
        increment()
        id_count = count
        expense[id_count] = {}
        expense[id_count]['amount'] = amount
        print("\n--- Expense Category ---\n"
        "[1] 🍔Food\n"
        "[2] 🚆Transportation\n"
        "[3] 🎥Entertainment\n"
        "[4] 👕Lifestyle\n"
        "[5] 🤷Other\n")
        cat_choice = int(input("\nEnter the menu number between 1 and 5: "))
        match cat_choice:
            case 1:
                expense[id_count]['category'] = 'Food'
            case 2:
                expense[id_count]['category'] = 'Transportation'
            case 3:
                expense[id_count]['category'] = 'Entertainment'
            case 4:
                expense[id_count]['category'] = 'Lifestyle'
            case 5:
                expense[id_count]['category'] = 'Other'
            case _:
                print("Invalid input. Try Again.")
        description = input("Description For The Expense: ")
        expense[id_count]['description'] = description
        print(f"Your expense of £{amount} has been registered.")
    except Exception as e:
        print(f"An error occurred: {e}")
    main_menu()

# Sum the total expenses
def total_spent():
    sum_amount = float()
    try:
        if not expense:
            raise EmptyListException
        else:
            i = 0
            while i < len(expense):
                i += 1
                sum_amount += float(expense[i]["amount"])
            print(f"The Total Amount Spent So Far Is: £{sum_amount}")
    except EmptyListException:
        print("The Expense is Empty.")
    main_menu()

# ! Need to be implement
def spent_in_cat():
    print("A function to be implement.")

# ! Need to be implement
def all_expense():
    print(expense)
    main_menu()

def main_menu():
    print("\n----- Menu -----\n"
        "[1] 📒Add New Expense\n"
        "[2] 💸Show Total Amount Spent\n"
        "[3] 📚Show Total Amount Spent In Category\n"
        "[4] 📜Show All Expenses\n"
        "[5] 🔴Exit The Application\n")
    choice = int(input("\nEnter the menu number between 1 and 5: "))
    match choice:
        case 1:
            add_expense()
        case 2:
            total_spent()
        case 3:
            spent_in_cat()
            
        case 4:
            all_expense()
            
        case 5:
            print("Thank You for using The Expense Tracker Application!")
        case _:
            print("Invalid input. Try Again.")

class EmptyListException(Exception):
    pass

# Initiate a dictionary
expense = {}
# Start the main menu
main_menu()