from helpers import (
    check_deadlines,
    add_quest,
    edit_quest,
    complete_quest,
    delete_quest,
    list_quest,
    search_quests,
    manage_categories,
)

def main():
    check_deadlines()
    while True:
        print("\nWelcome to the My Bucket List CLI!")
        print("1. Add Quest")
        print("2. Edit Quest")
        print("3. Complete Quest")
        print("4. Delete Quest")
        print("5. View All Quests")
        print("6. Search Quests")
        print("7. Manage Categories")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_quest()
        elif choice == '2':
            edit_quest()
        elif choice == '3':
            complete_quest()
        elif choice == '4':
            delete_quest()
        elif choice == '5':
            list_quest()
        elif choice == '6':
            search_quests()
        elif choice == '7':
            manage_categories()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            


if __name__ == '__main__':
    main()
