import random

START_HEALTH = 100
FIXED_DAMAGE = None


def get_damage():
    if FIXED_DAMAGE is not None:
        return FIXED_DAMAGE
    return random.randint(10, 40)


def show_menu():
    print("\nYou are in the Forest. What do you want to do?")
    print("1. Go to the Cave")
    print("2. Go to the River")
    print("3. Quit")


def explore_cave(health, score):
    damage = get_damage()
    health = max(0, health - damage)
    print(f"Monster attacks! Damage: {damage}. Health: {health}")

    if health > 0:
        score += 20
        print(f"You found a key! Score: {score}")

    return health, score


def explore_river(health, score):
    score += 50
    print("You found a treasure!")
    print(f"Score: {score} | Health: {health}")
    return health, score


def play_game():
    health = START_HEALTH
    score = 0

    print("Welcome to the Text-Based Adventure Game!")
    print(f"Health: {health} | Score: {score}")

    while health > 0:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            health, score = explore_cave(health, score)
        elif choice == "2":
            health, score = explore_river(health, score)
        elif choice == "3":
            print(f"You left the adventure. Final score: {score} | Health: {health}")
            return
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

    print(f"Game Over! Final score: {score}")


play_game()
