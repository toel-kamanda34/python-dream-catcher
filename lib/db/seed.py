import random
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from models import User, Quest, Category, item_category
from database import SessionLocal

def seed_users():
    session = SessionLocal()
    users = [
        User(username=f"user{i}", email=f"user{i}@example.com")
        for i in range(1, 17)
    ]
    session.add_all(users)
    session.commit()

def seed_categories():
    session = SessionLocal()
    categories = [
        Category(name=name)
        for name in ["Travel", "Fitness", "Education", "Career", "Personal", "Adventure", "Financial", "Relationship", "Hobby", "Spiritual"]
    ]
    session.add_all(categories)
    session.commit()

def seed_quests():
    session = SessionLocal()
    for i in range(1, 101):
        quest = Quest(
            title=f"Quest {i}",
            description=f"Description for Quest {i}",
            completed=random.choice([True, False]),
            created_at=datetime.utcnow() - timedelta(days=random.randint(1, 365)),
            deadline=datetime.utcnow() + timedelta(days=random.randint(1, 365)),
            user_id=random.randint(1, 10)
        )
        session.add(quest)
    session.commit()

def seed_item_categories():
    session = SessionLocal()
    quests = session.query(Quest).all()
    categories = session.query(Category).all()
    
    for quest in quests:
        num_categories = random.randint(1, 7)
        selected_categories = random.sample(categories, num_categories)
        for category in selected_categories:
            try:
                quest.categories.append(category)
                session.commit()
            except IntegrityError:
                session.rollback()  #  just roll back and continue if r/ship exists
    
    session.commit()

def clear_database():
    session = SessionLocal()
    
    # Delete all relationships from the association table 
    session.execute(item_category.delete())
    
    # Then, delete from all other tables
    session.query(Quest).delete()
    session.query(Category).delete()
    session.query(User).delete()
    
    session.commit()
    print("Database cleared.")

if __name__ == "__main__":
    clear_database()
    seed_users()
    seed_categories()
    seed_quests()
    seed_item_categories()
    print("Seeding completed successfully!")