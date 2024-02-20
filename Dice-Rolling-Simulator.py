import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        user_input = input("Press 'Enter' to roll the dice or 'q' to quit: ").strip().lower()
        if user_input == 'q':
            break
        result = roll_dice()
        print(f"You rolled a {result}!")


if __name__ == "__main__":
    main()

