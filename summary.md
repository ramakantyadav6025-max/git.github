# Project Summary: Text-Based Adventure Game

**Name:** Rama Kant Yadav | **ERP:** RU-26-02140 | **Section:** K
**PS No.:** 38 | **Language:** Python 3

---

## 1. Overview

This project is a console game where the player starts in a forest with **100 Health** and **0 Score**, then chooses to explore a cave, explore a river, or quit. The cave has a monster that causes random damage but gives a key (+20 score) if the player survives. The river gives a treasure (+50 score). The game ends when the player quits or Health reaches 0.

The program is a single file, `adventure_game.py`, and uses only four concepts: **conditions, loops, functions and the random module**.

---

## 2. How the Logic Was Implemented

### Step 1: Break the problem into small parts

Instead of writing everything in one block, the game was split into small jobs, and each job became one function:

| Job | Function |
|-----|----------|
| Decide how much damage the monster does | `get_damage()` |
| Show the choices to the player | `show_menu()` |
| Handle everything that happens in the cave | `explore_cave()` |
| Handle everything that happens at the river | `explore_river()` |
| Run the game from start to finish | `play_game()` |

This keeps each function short and easy to understand, test and change.

### Step 2: Track the game state

The game needs to remember two values: `health` and `score`. They are created inside `play_game()` and passed into the place functions. Each place function returns the updated values, which are saved back using:

```python
health, score = explore_cave(health, score)
```

This avoids global variables, so it is always clear where a value changes.

### Step 3: Keep the game running with a loop

The main loop is:

```python
while health > 0:
```

It repeats the menu again and again. Two things can end it:
- Health reaches 0, so the loop condition becomes false and "Game Over!" is printed.
- The player picks 3, which uses `return` to leave the function straight away with a goodbye message.

### Step 4: Handle choices with conditions

The player's input is checked with `if / elif / else`:

- `"1"` runs the cave
- `"2"` runs the river
- `"3"` quits
- anything else prints `Invalid choice. Enter 1, 2 or 3.`

The input is read as **text** and compared with `"1"`, `"2"` and `"3"`. This means typing `abc` or `7` never crashes the program and never costs the player any health.

### Step 5: Add the random monster

`random.randint(10, 40)` picks the monster damage. To make testing possible, the constant `FIXED_DAMAGE` can be set to `30`. When it is `None`, the damage is random. When it has a value, that value is always used.

### Step 6: Handle the cave result

In `explore_cave()` the order matters:

1. Take damage off the health.
2. Print the attack message.
3. Only if health is still above 0, add 20 score and print the key message.

This matches the expected output: a player who dies in the cave does not get the key.

---

## 3. Difficulty in Creation

**Overall difficulty: Easy to Moderate (beginner level).**
The logic is simple, but a few small details need care to match every test case exactly.

| Part | Difficulty | Why |
|------|------------|-----|
| Menu and loop | Easy | Standard `while` loop with `if / elif / else`. |
| Input validation | Easy | Comparing text instead of converting to a number avoids crashes on input like `abc`. |
| River logic | Easy | Only adds score. |
| Cave logic | Moderate | Needs the right order: damage first, then the survival check, then the key. |
| Keeping health from going below 0 | Moderate | A 30 damage hit on 30 health must show `Health: 0`, not a negative number. Solved with `max(0, health - damage)`. |
| Testing random behavior | Moderate | Random damage gives different results each run, so test cases cannot be repeated. Solved with the `FIXED_DAMAGE` setting. |
| Updating two values from a function | Moderate | A function cannot change a number outside itself, so the functions return `health, score` and the caller stores them. |
| Matching exact output text | Moderate | Messages like `Score: 70 | Health: 70` must match the expected output exactly, including spacing and punctuation. |

### Main challenges and how they were solved

1. **Random damage made testing hard.**
   *Solution:* a `FIXED_DAMAGE` constant at the top of the file, set to `30` for Test Cases 2 and 4 and `None` for normal play.

2. **Health could drop below zero.**
   *Solution:* `max(0, health - damage)` keeps the lowest possible health at 0.

3. **Invalid input could crash or punish the player.**
   *Solution:* the choice is kept as text, and the `else` branch only prints a message, so health and score stay unchanged.

4. **Functions needed to change both health and score.**
   *Solution:* return both values and unpack them in the loop, which is simple and avoids global variables.

5. **The Game Over and Quit messages are different.**
   *Solution:* quitting uses `return` right away with its own message, while the "Game Over!" message sits after the loop and only runs when health reaches 0.

---

## 4. Conclusion

The project was solved by splitting the game into small functions, tracking health and score with returned values, and using a single `while` loop with `if / elif / else` for the choices. The trickiest parts were the cave logic, keeping health from going negative, and testing random behavior, and each was solved with a small, simple change. The result is a short, readable program that meets every requirement and passes all four test cases.
