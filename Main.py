import random
print("Hello reader")

readername = input("What is your name? ")

print("Hello " + readername)

names = ["Zara", "Ben", "Andrew", "Aisha", "Naisha"]
places = ["computopia", "Turingville", "Babbageland", "Digitopolis"]
quests = ["seek the holy grail", "return the ring", "slay the dragon"]
roles = ["knight", "Amazon warrior", "ogre", "witch"]

randomname = random.choice(names)
randomplace = random.choice(places)
randomquest = random.choice(quests)
randomrole = random.choice(roles)

story = "Once upon a time there was a " + randomrole + " called " + randomname + "."

print(story)