from models import db, Pet
from app import app

db.drop_all()
db.create_all()

# Add pets
fluffy = Pet(
    name='Fluffy',
    species='Flufferson',
    photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyPymeYqn2wOD8j-kLZZFjCHkHOHaOZ0nTFKVXlHQMqgDe8T1a',
    age='10',
    notes='it is a pet',
    available=True)

db.session.add(fluffy)
db.session.commit()