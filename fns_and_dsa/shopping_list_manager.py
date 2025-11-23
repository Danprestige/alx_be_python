def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Core requirement: start with an empty list named shopping_list
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue
        if choice == 1:
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        elif choice == 2:
=======

    # Keep showing the menu until the user chooses to exit
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # Add item
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item == "":
                print("No item entered. Nothing added.")
            else:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")

        # Remove item
        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue

            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
<
        elif choice == 3:

        # View list
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Your Shopping List:")

                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
        elif choice == 4:
            print("Goodbye!")
            break
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")

        # Exit
        elif choice == '4':
            print("Goodbye!")
            break

        # Handle invalid menu choices gracefully

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
