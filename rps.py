import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    
    result_text = f"Computer chose: {computer_choice}\n"

    if user_choice == computer_choice:
        result_text += "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result_text += "You win!"
    else:
        result_text += "You lose!"
    
    # Display the result in a message box
    messagebox.showinfo("Result", result_text)

# Function to handle the user's choice when a button is clicked
def user_choice(choice):
    determine_winner(choice)

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Create labels and buttons
label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", width=15, command=lambda: user_choice('rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: user_choice('paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: user_choice('scissors'))
scissors_button.pack(pady=5)

# Start the main event loop
root.mainloop()