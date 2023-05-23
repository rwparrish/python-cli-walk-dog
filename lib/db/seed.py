from faker import Faker
import random

fake = Faker()

owners = []
dogs = []

# Generate 4 owners
for _ in range(4):
    owner = {
        'name': fake.name(),
        'age': random.randint(18, 60)
    }
    owners.append(owner)

# Generate 3 dogs
dog_breeds = ['Labrador', 'Golden Retriever', 'Poodle', 'Bulldog', 'German Shorthaired Pointer', 'Siberian Husky']
dog_sexes = ['Male', 'Female']
for _ in range(3):
    dog = {
        'name': fake.name(),
        'breed': random.choice(dog_breeds),
        'age': random.randint(1, 10),
        'sex': random.choice(dog_sexes)
    }
    dogs.append(dog)

# Generate 15 walks with varying owners and dogs
walks = []
for _ in range(15):
    walk = {
        'owner_id': random.choice(owners)['id'],
        'dog_id': random.choice(dogs)['id'],
        'date': fake.date(),
        'time': fake.time(),
        'duration': random.randint(30, 120),
        'location': fake.address()
    }
    walks.append(walk)

# Print the generated data (you can modify this to write to a file or insert into a database)
print("Owners:")
for owner in owners:
    print(owner)

print("\nDogs:")
for dog in dogs:
    print(dog)

print("\nWalks:")
for walk in walks:
    print(walk)