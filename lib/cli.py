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
import os
from colorama import init, Fore, Style

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(Fore.CYAN + Style.BRIGHT + """
╔══════════════════════════════════════╗
║     🌟 My Bucket List CLI 🌟         ║
╚══════════════════════════════════════╝
""" + Style.RESET_ALL)

def print_menu():
    print(Fore.YELLOW + """
1. 📝 Add Quest
2. ✏️  Edit Quest
3. ✅ Complete Quest
4. 🗑️  Delete Quest
5. 📋 View All Quests
6. 🔍 Search Quests
7. 🏷️  Manage Categories
8. 👋 Exit
""" + Style.RESET_ALL)

def main():
    check_deadlines()
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        choice = input(Fore.GREEN + "Choose an option: " + Style.RESET_ALL)
        
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
            print(Fore.MAGENTA + "\nThank you for using My Bucket List CLI! Goodbye! 👋" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please try again." + Style.RESET_ALL)
        
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    main()