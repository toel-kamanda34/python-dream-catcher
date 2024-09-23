from db.models import Quest, User, Category
from db.database import SessionLocal
from sqlalchemy.orm import joinedload

def main():
    while True:
        print("\nWelcome to the My Bucket List CLI!")
        print("1. Add Quest")
        print("2. Edit Quest")
        print("3. Complete Quest")
        print("4. Delete Quest")
        print("5. View All Quests")
        print("6. Manage Categories")
        print("7. Exit")

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
            manage_categories() 
        elif choice == '7':
            print("Goodbye!")
            break                      
        else:
            print("Invalid choice.Please try again.")
            

def add_quest():
    session = SessionLocal()
    title = input("Enter quest title: ")
    description = input("Enter quest description: ")
    user_quest = Quest(title=title, description=description)

    session.add(user_quest)
    session.commit()
    print("Quest added successfully!")
    session.close()

def edit_quest():
    session = SessionLocal()
    quest_id = input("Enter quest ID to edit: ")
    quest = session.query(Quest).get(quest_id)
    if quest:
        new_title = input(f"Enter new title(current: {quest.title}): ")
        new_description = input (f"Enter new description (current: {quest.description}): ")
        if new_title:
            quest.title = new_title
        if new_description:
            quest.description = new_description
        session.commit()
        print("Quest updated successfully!")
    else:
        print("Quest not found")
    session.close()

def complete_quest():
    session = SessionLocal()
    quest_id = input("Enter quest ID to complete: ")
    try:
        quest = session.query(Quest).get(int(quest_id))  # Convert input to int
        if quest:
            quest.completed = True
            session.commit()
            print("Quest marked as completed!")
        else:
            print("Quest not found!")
        session.close()
    except ValueError:
        print("Invalid quest ID. Please enter a number.")

def delete_quest():
    session = SessionLocal()
    quest_id = input("Enter quest ID to delete: ")
    quest = session.quesry(Quest).get(quest_id)
    if quest:
        session.delete(quest)
        session.commit()
        print("Quest deleted successfully!")
    else:
        print("Quest not found!")
    session.close()


def list_quest():
    session = SessionLocal()
    quests = session.query(Quest).options(joinedload(Quest.categories)).all()
    for quest in quests:
        categories = ",".join([c.name for c in quest.categories])
        print(f"{quest.id}: {quest.title} (Completed: {quest.completed}) - Categories: {categories}")
    session.close()


if __name__ == '__main__':
    main()