## 🎯 1. Project Overview & Objective

This project is a console-based **Text-Based Adventure Game** developed in Python 3 for the School of Computer Science and Engineering at **Rungta International Skills University**. The primary objective is to simulate an immersive player exploration experience across three distinct locations (**Forest**, **Cave**, and **River**), while accurately tracking player health, scores, and handling menu choices using core programming constructs.

## 🛠️ 2. Implementation Details

The application was built as a clean, modular Python console script following professional coding standards:

* 🧩 **Modular Function Structure:** Instead of writing all procedural code in a single block, the game logic was broken down into specialized functions:
  * `forest(health, score)`: Handles the main menu interface, displays current status, and captures player input.
  * `cave(health, score)`: Simulates monster encounters, calculates damage, updates health, and awards key points (`+20`).
  * `river(health, score)`: Manages treasure discovery and awards points (`+50`) without damaging health.
  * `main()`: Controls the primary `while` loop, initializes player attributes, and routes user selections.

* 🔄 **Control Flow & Conditions:** Utilized a `while health > 0:` loop to keep the game running continuously until the player voluntarily quits or loses all health. Multi-way `if-elif-else` conditional statements were used to route choices and evaluate survival.

* 🎨 **Randomization & Terminal Styling:** Used Python's built-in `random.randint(10, 40)` module for dynamic monster damage. ANSI escape codes were integrated to color-code terminal outputs (**Red** for damage/game over, **Green** for success, **Cyan/Yellow** for UI status) making it visually appealing without requiring external libraries.

## 🚧 3. Difficulties Faced & Solutions

During the development and testing against the college lab test cases, a few practical challenges were encountered and successfully resolved:

### ⚡ Challenge 1: Test Case 2 Output Mismatch
* **Problem:** Initially, when running Test Case 2 where starting health is `30` and monster damage is fixed to `30`, the health was defaulting to `100` or carrying over from previous test runs, causing `100 - 30 = 70` instead of dropping instantly to `0`.
* **Solution:** Added a flexible startup check (`start_hp = input(...)`) and a `test_mode = True` toggle at the top of the script. This allows instant setup of `30` starting health and fixed `30` damage specifically for faculty verification.

### 🚫 Challenge 2: Program Crashes on Invalid Input
* **Problem:** When entering alphabetic strings like `abc` or out-of-range numbers like `7`, standard numeric parsing caused the program to crash with a `ValueError`.
* **Solution:** Kept input strictly as a string using `.strip()`. Any entry other than `"1"`, `"2"`, or `"3"` is routed to the `else` block, which safely prints `"Invalid choice. Enter 1, 2 or 3."` and `"No health lost."` without crashing.

### 📈 Challenge 3: Score Accumulation Across Multiple Test Runs
* **Problem:** During Test Case 4 (sequential execution of Cave, River, and Quit), testing individual functions sequentially caused scores to accumulate incorrectly if the interpreter session was preserved.
* **Solution:** Implemented clean state-passing arguments (health and score returned as tuples from functions) so that player stats are explicitly tracked and updated per session step.

## ✅ 4. Test Case Verification Summary

All four official test cases from the problem specification sheet were successfully tested and verified:

| Test Case | Scenario Description | Expected & Actual Result | Status |
| :--- | :--- | :--- | :--- |
| **Test Case 1** | Normal Input (River) | `You found a treasure!` <br> `Score: 50 \| Health: 100` | **PASS** ✅ |
| **Test Case 2** | Boundary Input (Cave with 30 HP) | `Monster attacks! Damage: 30. Health: 0` <br> `Game Over! Final score: 0` | **PASS** ✅ |
| **Test Case 3** | Invalid Input (`7` and `abc`) | `Invalid choice. Enter 1, 2 or 3.` <br> `No health lost.` | **PASS** ✅ |
| **Test Case 4** | Multi-Step Scenario (Cave ➔ River ➔ Quit) | `Health: 70 \| Score: 70` <br> `You left the adventure. Final score: 70 \| Health: 70` | **PASS** ✅ |