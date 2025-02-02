import random

facts = [
    "Honey never spoils. Archaeologists found pots of honey in ancient tombs that are over 3000 years old!",
    "Octopuses have three hearts and blue blood due to copper-based hemocyanin.",
    "Bananas are berries, but strawberries are not!",
    "A day on Venus is longer than a year on Venus.",
    "Wombat poop is cube-shaped to prevent it from rolling away."
]

def get_random_fact():
    return random.choice(facts)

if __name__ == "__main__":
    print(get_random_fact())
