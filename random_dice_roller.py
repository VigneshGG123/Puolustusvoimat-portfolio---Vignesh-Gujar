import random
def random_dice_roller():
    return random.randint(1, 6)
def main():
    print("Welcome to the Random Dice Simulator!")

    while True:
        input("Press Enter to roll the dice...")

        result = random_dice_roller()
        print(f"You rolled a {result}!")

        while True:
            play_again = input("Do you want to roll again? (y/n): ").lower()
            if play_again in ['y', 'n']:
                break
            else:
                print("Invalid option. Please enter 'y' or 'n'.")

        if play_again != 'y':
            print("Thanks for rolling the dice. Goodbye!")
            break

if __name__ == "__main__":
    main()

