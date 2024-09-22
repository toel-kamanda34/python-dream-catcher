from database import SessionLocal
from models import Destination, BucketListItem

session = SessionLocal()

#destinations
destination1 = Destination(name="Mount Kenya", location="Central Kenya")
destination2 = Destination(name="Maasai Mara", location="Narok")
destination3 = Destination(name="Diani Beach", location="Mombasa")
destination4 = Destination(name="Lake Naivasha", location="Naivasha")

#creating bucket list items
bucket_item1 = BucketListItem(description="Hike Mount Kenya", destination=destination1)
bucket_item2 = BucketListItem(description="Safari at Maasai Mara", destination=destination2)
bucket_item3 = BucketListItem(description="Relax at Diani Beach", destination=destination3)
bucket_item4 = BucketListItem(description="Boat ride at Lake Naivasha", destination=destination4)

#commit to database 
session.add_all([destination1,destination2, destination3, destination4 , bucket_item1, bucket_item2, bucket_item3, bucket_item4  ])
session.commit()

print("Dtabase seeded successfully")
session.close()