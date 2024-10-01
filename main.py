import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    # Display choices
    result_label.config(text=f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Add instructions
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instructions_label.pack()

# Create result label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Create buttons for user choice
rock_button = tk.Button(root, text="Rock", width=15, command=lambda: determine_winner("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: determine_winner("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: determine_winner("Scissors"))
scissors_button.pack(pady=5)

# Run the application
root.mainloop()
