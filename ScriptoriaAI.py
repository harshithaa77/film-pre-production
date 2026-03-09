import random

# Story elements database
genres = ["Action", "Comedy", "Sci-Fi", "Romance", "Thriller"]

characters = [
    "A brave police officer",
    "A genius scientist",
    "A struggling musician",
    "A fearless journalist",
    "A young detective"
]

locations = [
    "in a futuristic city",
    "in a small village",
    "in outer space",
    "in a haunted mansion",
    "in a crowded metro city"
]

conflicts = [
    "must stop a dangerous criminal",
    "discovers a secret experiment",
    "tries to save the world",
    "uncovers a political conspiracy",
    "searches for a missing person"
]

# Function to generate film idea
def generate_story():
    genre = random.choice(genres)
    character = random.choice(characters)
    location = random.choice(locations)
    conflict = random.choice(conflicts)

    story = f"""
    Film Genre: {genre}

    Story Idea:
    {character} {location} who {conflict}.
    The journey leads to unexpected twists and dramatic moments.
    """

    return story


# Function to generate character profile
def generate_character():
    names = ["Arjun", "Maya", "Rahul", "Anika", "Vikram"]
    traits = ["brave", "intelligent", "mysterious", "kind", "ambitious"]

    name = random.choice(names)
    trait = random.choice(traits)

    profile = f"""
    Character Name: {name}
    Personality: {trait}
    Role: Main character in the story
    """

    return profile


# Function to generate scene ideas
def generate_scene():
    scenes = [
        "Opening scene showing the main character's daily life.",
        "A mysterious event changes everything.",
        "The hero faces a major challenge.",
        "A dramatic confrontation occurs.",
        "Final scene resolving the conflict."
    ]

    return random.choice(scenes)


# Main program
print("---- Scriptoria AI Film Pre-Production System ----")

while True:
    print("\n1. Generate Story Idea")
    print("2. Generate Character")
    print("3. Generate Scene Idea")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(generate_story())

    elif choice == "2":
        print(generate_character())

    elif choice == "3":
        print(generate_scene())

    elif choice == "4":
        print("Exiting Scriptoria System")
        break

    else:
        print("Invalid choice")