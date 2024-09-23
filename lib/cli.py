from db.models import Quest, User
from db.database import SessionLocal

def main():
    print("Welcome to the My Bucket List CLI!")
    print("1. Add Quest")
    print("2. Mark Quest as Completed")
    print("3. View All Quests")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_quest()
    elif choice == '2':
        complete_quest()
    elif choice == '3':
        list_quests()
    else:
        print("Goodbye!")
        exit()

def add_quest():
    session = SessionLocal()
    title = input("Enter quest titlle: ")
    description = input("Enter quest description: ")
    new_quest = Quest(title=title, description=description)

    session.add(new_quest)
    session.commit()
    print("Quest added successfully!")

def complete_quest():
    session = SessionLocal()
    quest_id = input("Enter quest ID to complete: ")
    quest = session.quesry(Quest).get(quest_id)
    if quest:
        quest.completed = True
        session.commit()
        print("Quest marked as completed!")
    else:
        print("Quest not found!")

def list_quests():
    session = SessionLocal()
    quests = session.quesry(Quest).all()
    for quest in quests:
        print(f"{quest.id}: {quest.title} (Completed: {quest.completed})")


if __name__ == '__main__':
    main()
