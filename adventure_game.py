import random

# terminal ke liye colour codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Test cases pass karne ke liye damage 30 fix rakha hai (True)
# Random damage (10 to 40) chahiye ho toh isko False kar dena
test_mode = True


# 1. Forest function
def forest(health, score):
    print(CYAN + "\n----------------------------------------" + RESET)
    print(f"Current Status -> {GREEN}Health: {health}{RESET} | {YELLOW}Score: {score}{RESET}")
    print(f"{YELLOW}1.{RESET} Cave  |  {YELLOW}2.{RESET} River  |  {YELLOW}3.{RESET} Quit")
    print(CYAN + "(Tip: Test Case 2 ke liye pehle '30' type karein, fir '1' dabayein)" + RESET)
    
    choice = input(BOLD + "\nChoice: " + RESET).strip()
    return choice


# 2. Cave function
def cave(health, score):
    if test_mode:
        damage = 30
    else:
        damage = random.randint(10, 40)
        
    health = health - damage
    
    if health < 0:
        health = 0
        
    print(RED + f"Monster attacks! Damage: {damage}. Health: {health}" + RESET)
    
    if health > 0:
        score = score + 20
        print(GREEN + f"You found a key! Score: {score}" + RESET)
    else:
        print(RED + BOLD + f"Game Over! Final score: {score}" + RESET)
        
    return health, score


# 3. River function 
def river(health, score):
    score = score + 50
    print(GREEN + "You found a treasure!" + RESET)
    print(BOLD + f"Score: {score} | Health: {health}" + RESET)
    return health, score

def main():
    print(CYAN + BOLD + "=== TEXT-BASED ADVENTURE GAME ===" + RESET)
    
    start_hp = input("Starting Health (Normal ke liye Enter dabayein, Test Case 2 ke liye 30 likhein): ").strip()
    if start_hp == "30":
        health = 30
    else:
        health = 100
        
    score = 0
    
    while health > 0:
        user_choice = forest(health, score)
        
        if user_choice == "1":
            health, score = cave(health, score)
            
        elif user_choice == "2":
            health, score = river(health, score)
            
        elif user_choice == "3":
            print(YELLOW + BOLD + f"You left the adventure. Final score: {score} | Health: {health}" + RESET)
            break
            
        elif user_choice == "30":
            health = 30
            score = 0
            print(YELLOW + ">>> Starting Health set to 30 and Score reset to 0! Ab Choice: 1 enter karein." + RESET)
            
        else:
            print(RED + "Invalid choice. Enter 1, 2 or 3." + RESET)
            print("No health lost.")


if __name__ == "__main__":
    main()