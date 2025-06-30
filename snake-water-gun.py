
import random

# Function to determine the winner
def check(user, computer):
    # Return 0 if it's a draw
    if computer == user:
        return 0
    # Losing conditions for the user
    if (computer == 2 and user == 0):  # Gun vs Snake → Gun wins
        return -1
    if (computer == 1 and user == 2):  # Water vs Gun → Water wins
        return -1
    if (computer == 0 and user == 1):  # Snake vs Water → Snake wins
        return -1
    # If none of the above, the user wins
    return 1

# Generate a random choice for computer: 0 - Snake, 1 - Water, 2 - Gun
computer = random.randint(0, 2)

# Take user input
print("Welcome to the Snake 🐍 Water 💧 Gun 🔫 Game!")
print("Rules: Snake drinks Water, Water drowns Gun, Gun kills Snake.\n")

print("Your choices:\n0 for 🐍 Snake\n1 for 💧 Water\n2 for 🔫 Gun")
user = int(input("Enter your number (0 / 1 / 2): "))

# Print both choices
print("\nYou chose:", ["🐍 Snake(0)", "💧 Water(1)", "🔫 Gun(2)"][user])
print("Computer chose:", ["🐍 Snake(0)", "💧 Water(1)", "🔫 Gun(2)"][computer])

# Determine the winner
score = check(user, computer)

# Display result
print("\nResult:")
if score == 0:
    print("🤝 It's a draw! Try again!")
elif score == 1:
    print("🎉 Congratulations! You win! 🏆")
else:
    print("😢 Oops! You lost. Better luck next time!")

print("\nThanks for playing! 🎮\n")

print("💡 Reminder: A cool Tkinter GUI version of this game is coming soon! Stay tuned! 🖥️✨")