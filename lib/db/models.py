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
    

    user = relationship("User", back_populates="quests")

    
