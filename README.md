# Text-Based Adventure Game

**Rungta International Skills University**
School of Computer Science and Engineering
Bachelor of Technology Computer Science and Engineering

---

## Student Details

| Field   | Details                      |
|---------|------------------------------|
| Name    | Rama Kant Yadav              |
| ERP     | RU-26-02140                  |
| Email   | rama.kant.yadav@rungta.org   |
| Section | K                            |

## Project Details

| Field         | Details                  |
|---------------|--------------------------|
| PS No.        | 38                       |
| Project Title | Text-Based Adventure Game |
| Language      | Python 3                 |
| Concepts      | Conditions, Loops, Functions, Random |

---

## Problem Statement

Create a text-based adventure game in which the player explores a forest, a cave and a river by choosing options from a menu, faces a random monster attack, collects score and ends the game by quitting or losing all health.

**Note:**
- The player starts with **Health 100** and **Score 0** in the Forest.
- Choices: **1** Cave, **2** River, **3** Quit.
- **Cave:** a monster attacks (random damage from 10 to 40, fixed to 30 for testing). If the player survives, a key gives **+20 score**.
- **River:** a treasure gives **+50 score**.
- The game ends when Health reaches 0.

---

## Bare Minimum Requirements

1. Write the solution in Python 3 (one `.py` file) and run it from the console.
2. Use functions for each place (forest, cave, river) and conditions for the player's choices.
3. Use a loop to keep the game running until the player quits or Health reaches 0.
4. Use the `random` module for the monster damage, and track Health and Score.
5. Validate every menu choice and show the final score at the end.

## Instructions

1. Understand the problem statement and define the problem clearly.
2. Develop the solution using proper logic and programming concepts.
3. Implement all required features and pass the given test cases.
4. Test and debug the project to ensure correct output.
5. Prepare the documentation/report and upload the code and report to GitHub.
6. Complete and submit the project within the given deadline.

---

## How to Run

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Save the code as `adventure_game.py`.
3. Open a terminal in the same folder and run:

```
python adventure_game.py
```

(On some systems use `python3 adventure_game.py`.)

---

## Game Rules

| Choice | Place  | What happens                                                        |
|--------|--------|---------------------------------------------------------------------|
| 1      | Cave   | A monster attacks and reduces Health. If you survive, you get a key (+20 score). |
| 2      | River  | You find a treasure (+50 score). No health is lost.                 |
| 3      | Quit   | The game ends and your final score is shown.                        |
| Other  | -      | "Invalid choice. Enter 1, 2 or 3." No health is lost.               |

The game also ends automatically when Health reaches 0.

---

## Program Flow

```
START
  |
  v
Set Health = 100, Score = 0
  |
  v
+-----------------------------+
| Is Health greater than 0?   |<-----------------------------+
+-----------------------------+                              |
   | Yes                  | No                               |
   v                      v                                  |
Show menu           Print "Game Over! Final score"           |
   |                      |                                  |
   v                      v                                  |
Read choice              END                                 |
   |                                                         |
   +--> 1: explore_cave()  -> update Health and Score -------+
   +--> 2: explore_river() -> update Score -----------------+
   +--> 3: Print "You left the adventure." -> END            |
   +--> other: Print "Invalid choice." ----------------------+
```

---

## Code

```python
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
```

---

## Code Explanation

### Constants (top of the file)

| Name           | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `START_HEALTH` | The health the player begins with (100). Change it to 30 for Test Case 2. |
| `FIXED_DAMAGE` | `None` means the monster does random damage. Set it to `30` to get the fixed damage used in the test cases. |

### Functions

**`get_damage()`**
Returns the damage the monster deals. If `FIXED_DAMAGE` has a value (testing), that value is returned. Otherwise `random.randint(10, 40)` picks a random whole number between 10 and 40.

**`show_menu()`**
Prints the Forest menu with the three options: Cave, River and Quit. It takes no input and returns nothing.

**`explore_cave(health, score)`**
1. Gets the monster's damage from `get_damage()`.
2. Subtracts the damage from health. `max(0, ...)` makes sure health never goes below 0.
3. Prints the monster attack message.
4. If health is still above 0, adds 20 to the score and prints the key message.
5. Returns the new `health` and `score`.

**`explore_river(health, score)`**
Adds 50 to the score, prints the treasure message with the current score and health, and returns `health` and `score`. Health does not change at the river.

**`play_game()`**
The main function that controls the whole game:
1. Sets `health` to `START_HEALTH` and `score` to 0, then prints a welcome message.
2. Runs a `while health > 0` loop so the game continues until health reaches 0.
3. Shows the menu and reads the player's choice (`.strip()` removes extra spaces).
4. Uses `if / elif / else` to run the cave, run the river, quit, or print an invalid choice message.
5. When the loop ends because health is 0, prints "Game Over!" with the final score.

### Key Concepts Used

- **Conditions:** `if / elif / else` handles the menu choice and checks whether the player survived.
- **Loops:** the `while` loop keeps the game running until the player quits or loses all health.
- **Functions:** each place and the damage calculation is a separate function, so the code is easy to read and change.
- **Random:** `random.randint(10, 40)` gives the monster's random damage.
- **Input validation:** the choice is read as text, so anything that is not `1`, `2` or `3` (like `7` or `abc`) is rejected without crashing or losing health.

---

## Test Cases

### Test Case 1: Normal Input

| Input | Expected Output |
|-------|-----------------|
| Choice: 2 (River) | `You found a treasure!`<br>`Score: 50 \| Health: 100` |

### Test Case 2: Boundary / Minimum Input

**Setup:** set `START_HEALTH = 30` and `FIXED_DAMAGE = 30`.

| Input | Expected Output |
|-------|-----------------|
| Starting Health set to 30<br>Choice: 1 (Cave)<br>Monster damage fixed to 30 | `Monster attacks! Damage: 30. Health: 0`<br>`Game Over! Final score: 0` |

### Test Case 3: Invalid Input

| Input | Expected Output |
|-------|-----------------|
| (a) Choice: 7 | `Invalid choice. Enter 1, 2 or 3.` |
| (b) Choice: abc | `Invalid choice. Enter 1, 2 or 3.`<br>No health lost. |

### Test Case 4: Different Valid Scenario

**Setup:** set `FIXED_DAMAGE = 30` (keep `START_HEALTH = 100`).

| Input | Expected Output |
|-------|-----------------|
| Monster damage fixed to 30<br>Choices: 1 (Cave), 2 (River), 3 (Quit) | Cave: `Monster attacks! Damage: 30. Health: 70`<br>`You found a key! Score: 20`<br>River: `You found a treasure!`<br>`Score: 70 \| Health: 70`<br>`You left the adventure. Final score: 70 \| Health: 70` |

> After testing, set `START_HEALTH = 100` and `FIXED_DAMAGE = None` again for normal random gameplay.

---

## Sample Run (Test Case 4)

```
Welcome to the Text-Based Adventure Game!
Health: 100 | Score: 0

You are in the Forest. What do you want to do?
1. Go to the Cave
2. Go to the River
3. Quit
Enter your choice: 1
Monster attacks! Damage: 30. Health: 70
You found a key! Score: 20

You are in the Forest. What do you want to do?
1. Go to the Cave
2. Go to the River
3. Quit
Enter your choice: 2
You found a treasure!
Score: 70 | Health: 70

You are in the Forest. What do you want to do?
1. Go to the Cave
2. Go to the River
3. Quit
Enter your choice: 3
You left the adventure. Final score: 70 | Health: 70
```

---

## Repository Structure

```
.
├── adventure_game.py
└── README.md
```

---

## Author

**Rama Kant Yadav**
ERP: RU-26-02140 | Section: K
Email: rama.kant.yadav@rungta.org
