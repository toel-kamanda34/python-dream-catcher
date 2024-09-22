from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class BucketListItem(Base):
    __tablename__ = 'bucket_list_items'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    completed = Column(Integer, default=0)
    destination_id = Column(Integer, ForeignKey('destinations.id'))

    destination = relationship("Destination", back_populates="bucket_list_items")

    def __repr__(self):
        return f"<BucketListItem(description={self.description}, completed={self.completed})>"
    
    def show_bucket_list(session):
        items = session.query(BucketListItem).all()
        for item in items:
            print(f"Item: {item.description}, Destination: {item.description.name}, Completed: {item.completed}")
    
class Destination(Base):
    __tablename__ = 'destinations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    bucket_list_items = relationship("BucketListItem", back_populates="destination")

    def __repr__(self):
        return f"<Destination(name={self.name}, location={self.location})>"