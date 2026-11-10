# 🌲 Text-Based Adventure Game 🎮

> ### 👨‍🎓 Student Details
>
> | Field | Details | 
> | ----- | ----- | 
> | **Name** | Rama Kant Yadav | 
> | **ERP** | `RU-26-02140` | 
> | **Email** | 📧 `rama.kant.yadav@rungta.org` | 
> | **Section** | 📌 K | 

> ### 📌 Project Details
>
> | Field | Details | 
> | ----- | ----- | 
> | **PS No.** | 38 | 
> | **Project Title** | Text-Based Adventure Game | 
> | **Language** | Python 3 | 
> | **Concepts** | Conditions, Loops, Functions, Random Module | 

## 📖 Problem Statement

Create a text-based adventure game in which the player explores a **forest**, a **cave**, and a **river** by choosing options from a menu, faces a random monster attack, collects score, and ends the game by quitting or losing all health.

> ⚠️ **Game Rules & Notes:**
>
> * 🟢 The player starts with **Health = 100** and **Score = 0** in the Forest.
>
> * 🗺️ **Choices:** **1** ➔ Cave, **2** ➔ River, **3** ➔ Quit.
>
> * 🦇 **Cave:** A monster attacks (random damage from 10 to 40, fixed to 30 for testing). If you survive, a key gives **+20 Score**.
>
> * 💎 **River:** Finding a treasure gives **+50 Score** (No health lost).
>
> * 💀 **Game Over:** The game ends automatically when Health reaches `0`.

## ⚙️ Bare Minimum Requirements

1. 💻 Write the solution in Python 3 (one `.py` file) and run it from the console.

2. 🛠️ Use functions for each place (`forest`, `cave`, `river`) and conditions for choices.

3. 🔄 Use a `while` loop to keep the game running until the player quits or Health reaches `0`.

4. 🎲 Use the `random` module for monster damage, and track Health and Score.

5. ✅ Validate every menu choice and show the final score at the end.

## 📝 Instructions

1. 🔍 Understand the problem statement and define the logic clearly.

2. 💡 Develop the solution using proper programming concepts.

3. 🧪 Implement all required features and pass the given test cases.

4. 🐛 Test and debug the project to ensure correct output.

5. 📂 Prepare documentation and upload the code and report to GitHub.

6. ⏱️ Complete and submit the project within the deadline.

## 🚀 How to Run

1. Install Python 3 from [python.org](https://www.python.org/downloads/).

2. Save the code as `adventure_game.py`.

3. Open your terminal / command prompt in the project folder and run:

   ```bash
   python adventure_game.py
   ```

   *(Note: On some systems, use `python3 adventure_game.py`)*

## 🗺️ Game Rules & Summary

| Choice | Place 📍 | What Happens ⚡ |
| :--- | :--- | :--- |
| **1** | 🦇 Cave | Monster attacks and reduces Health. If you survive, you get a key (**+20 Score**). |
| **2** | 🌊 River | You find a hidden treasure (**+50 Score**). No health lost! |
| **3** | 🚪 Quit | The game ends and your final score and remaining health are shown. |
| **Other** | ❌ Invalid | Prints `"Invalid choice. Enter 1, 2 or 3."` and `"No health lost."` |

## 📊 Program Flow Chart

```text
START
  │
  ▼
Set Health = 100 (or 30 for Test Case 2), Score = 0
  │
  ▼
┌─────────────────────────────┐
│ Is Health greater than 0?   │◄─────────────────────────────┐
└─────────────────────────────┘                              │
   │ Yes                  │ No                               │
   ▼                      ▼                                  │
forest() -> Show menu    END                                 │
   │                                                         │
   ▼                                                         │
Read choice                                                  │
   │                                                         │
   ├──► 1: cave(health, score)  -> update Health & Score ────┤
   │       (prints "Game Over! Final score" if Health == 0)  │
   ├──► 2: river(health, score) -> update Score (+50) ───────┤
   ├──► 3: Print "You left the adventure." -> END            │
   └──► other: Print "Invalid choice." & "No health lost." ──┘
```

## 🧠 Code Explanation

### 🎨 Constants & Terminal Settings

* **`RED`, `GREEN`, `CYAN`, `YELLOW`, `BOLD`, `RESET`**: ANSI escape sequences used to add color to the terminal output without needing external pip packages.
* **`test_mode`**: Set to `True` by default to fix monster damage to `30` for official test case verification. Set to `False` for dynamic random damage (`10` to `40`).

### 🛠️ Core Functions

* **`forest(health, score)`**: Displays the current status in the Forest along with the menu options. Reads input securely as a string.
* **`cave(health, score)`**: Calculates monster damage, subtracts it from health (clamped at `0`), awards `+20` score if alive, or triggers `Game Over`.
* **`river(health, score)`**: Adds `+50` to the score for finding treasure and outputs the updated stats.
* **`main()`**: Controls the main game loop, checks initial health, and processes player choices.

## 🧪 Test Cases & Verification

### Test Case 1: Normal Input
| Input | Expected & Actual Output |
| :--- | :--- |
| Choice: `2` (River) | `You found a treasure!`<br>`Score: 50 \| Health: 100` |

### Test Case 2: Boundary / Minimum Input
| Input | Expected & Actual Output |
| :--- | :--- |
| Starting Health: `30`<br>Choice: `1` (Cave) | `Monster attacks! Damage: 30. Health: 0`<br>`Game Over! Final score: 0` |

### Test Case 3: Invalid Input
| Input | Expected & Actual Output |
| :--- | :--- |
| (a) Choice: `7`<br>(b) Choice: `abc` | (a) `Invalid choice. Enter 1, 2 or 3.`<br>(b) `Invalid choice. Enter 1, 2 or 3.`<br>`No health lost.` |

### Test Case 4: Different Valid Scenario
| Input | Expected & Actual Output |
| :--- | :--- |
| Choices: `1` (Cave), `2` (River), `3` (Quit) | `Monster attacks! Damage: 30. Health: 70`<br>`You found a key! Score: 20`<br>`You found a treasure!`<br>`Score: 70 \| Health: 70`<br>`You left the adventure. Final score: 70 \| Health: 70` |

## 🖥️ Sample Console Run
```text
=== TEXT-BASED ADVENTURE GAME ===
Starting Health (Press Enter for 100, or type 30 for Test Case 2): 

----------------------------------------
Current Status -> Health: 100 | Score: 0
1. Cave  |  2. River  |  3. Quit

Choice: 1
Monster attacks! Damage: 30. Health: 70
You found a key! Score: 20

----------------------------------------
Current Status -> Health: 70 | Score: 20
1. Cave  |  2. River  |  3. Quit

Choice: 2
You found a treasure!
Score: 70 | Health: 70

----------------------------------------
Current Status -> Health: 70 | Score: 70
1. Cave  |  2. River  |  3. Quit

Choice: 3
You left the adventure. Final score: 70 | Health: 70
```

## 📂 Repository Structure
```text
.
├── adventure_game.py
└── README.md
```

---

## ✒️ Author

| Name | ERP | Email | Section |
| :--- | :--- | :--- | :--- |
| **Rama Kant Yadav** | `RU-26-02140` | 📧 `rama.kant.yadav@rungta.org` | 📌 K |