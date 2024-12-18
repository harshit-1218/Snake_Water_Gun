import random

def game_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == 'snake' and computer_choice == 'water') or \
         (user_choice == 'water' and computer_choice == 'gun') or \
         (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win!", 1
    else:
        return "You lose!", -1

# Options to select
choices = ['snake', 'water', 'gun']

print("Welcome to Snake Water Gun Game!")
print("Choices: snake, water, gun")

# Initialize scores
user_score = 0
computer_score = 0
rounds = 3

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    user_choice = input("Enter your choice: ").lower()

    # Validate input
    if user_choice not in choices:
        print("Invalid choice! Please choose snake, water, or gun.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Get result
    result, score = game_result(user_choice, computer_choice)
    print(result)

    # Update scores
    if score == 1:
        user_score += 1
    elif score == -1:
        computer_score += 1

# Display final results
print("\nGame Over!")
print(f"Your score: {user_score}")
print(f"Computer's score: {computer_score}")

if user_score > computer_score:
    print("Congratulations, you win the game!")
elif user_score < computer_score:
    print("Sorry, you lost the game!")
else:
    print("It's a tie game!")