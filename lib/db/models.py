from sqlalchemy import Column, Integer, String,Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Quest(Base):
    __tablename__ = 'quests'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)
    deadline = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    

    categories = relationship("Category", secondary='item_categories', backref="quests")

    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True )
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    quests = relationship('Quest', back_populates='user')


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, Unique=True, nullable=False)

class ItemCategory(Base):
    __tablename__ = 'item_categories'

    item_id = Column(Integer, ForeignKey('quests.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'),primary_key=True)
