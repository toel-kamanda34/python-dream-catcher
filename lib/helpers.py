from db.models import Quest, Category
from db.database import SessionLocal
from sqlalchemy.orm import joinedload
from datetime import datetime


def add_quest():
    session = SessionLocal()
    title = input("Enter quest title: ")
    description = input("Enter quest description: ")
    

    user_id = int(input("Enter user ID (1-10): "))  
    deadline_input = input("Enter deadline (YYYY-MM-DD): ")  


    
    try:
        deadline = datetime.strptime(deadline_input, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter a valid date.")
        session.close()
        return

    user_quest = Quest(title=title, description=description, user_id=user_id, deadline=deadline)  # Updated

    session.add(user_quest)
    session.commit()
    print("Quest added successfully!")
    session.close()


def edit_quest():
    session = SessionLocal()
    quest_id = input("Enter quest ID to edit: ")
    quest = session.get(Quest, quest_id)  # Updated
    if quest:
        new_title = input(f"Enter new title (current: {quest.title}): ")
        new_description = input(f"Enter new description (current: {quest.description}): ")
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
    quest_id = int(input("Enter quest ID to complete: "))
    quest = session.get(Quest, quest_id)  # Updated
    if quest:
        quest.completed = True
        session.commit()
        print("Quest marked as completed!")
    else:
        print("Quest not found!")
    session.close()

def delete_quest():
    session = SessionLocal()
    quest_id = input("Enter quest ID to delete: ")
    quest = session.get(Quest, quest_id)  # Updated
    if quest:
        session.delete(quest)
        session.commit()
        print("Quest deleted successfully!")
    else:
        print("Quest not found!")
    session.close()

def list_quest():
    session = SessionLocal()
    completed_filter = input("Show completed quests? (yes/no): ").strip().lower() == 'yes'
    category_filter = input("Enter category ID to filter by (or leave blank for all): ").strip()
    
    quests = session.query(Quest).options(joinedload(Quest.categories))
    
    if completed_filter:
        quests = quests.filter(Quest.completed.is_(True))
    if category_filter:
        quests = quests.join(Quest.categories).filter(Category.id == int(category_filter))
    
    quests = quests.all()
    for quest in quests:
        categories = ",".join([c.name for c in quest.categories])
        print(f"{quest.id}: {quest.title} (Completed: {quest.completed}) - Categories: {categories}")
    session.close()

def search_quests():
    session = SessionLocal()
    search_term = input("Enter a search term: ")
    quests = session.query(Quest).filter(Quest.title.ilike(f"%{search_term}%")).all()
    
    if quests:
        for quest in quests:
            print(f"{quest.id}: {quest.title} (Completed: {quest.completed})")
    else:
        print("No quests found with that search term.")
    
    session.close()

def check_deadlines():
    session = SessionLocal()
    now = datetime.utcnow()
    quests = session.query(Quest).filter(Quest.deadline < now, Quest.completed.is_(False)).all()
    
    for quest in quests:
        print(f"Reminder: The deadline for '{quest.title}' has passed!")
    
    session.close()

def manage_categories():
    while True:
        print("\nManage Categories")
        print("1. Add Category")
        print("2. Edit Category")
        print("3. Delete Category")
        print("4. View All Categories")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            add_category()
        elif choice == '2':
            edit_category()
        elif choice == '3':
            delete_category()
        elif choice == '4':
            list_categories()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_category():
    session = SessionLocal()
    category_name = input("Enter category name: ")
    new_category = Category(name=category_name)
    
    session.add(new_category)
    session.commit()
    print("Category added successfully!")
    session.close()

def edit_category():
    session = SessionLocal()
    category_id = input("Enter category ID to edit: ")
    category = session.get(Category, category_id)
    
    if category:
        new_name = input(f"Enter new name (current: {category.name}): ")
        if new_name:
            category.name = new_name
            session.commit()
            print("Category updated successfully!")
    else:
        print("Category not found")
    session.close()

def delete_category():
    session = SessionLocal()
    category_id = input("Enter category ID to delete: ")
    category = session.get(Category, category_id)
    
    if category:
        session.delete(category)
        session.commit()
        print("Category deleted successfully!")
    else:
        print("Category not found!")
    session.close()

def list_categories():
    session = SessionLocal()
    categories = session.query(Category).all()
    for category in categories:
        print(f"{category.id}: {category.name}")
    session.close()

