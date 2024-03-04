import tkinter as tk
import random

def determine_winner(user_choice):
    computer_choice = random.choice(choices)
    result_text.set("Computer's Choice: " + computer_choice)

    if user_choice == computer_choice:
        result_var.set("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_var.set("You win!")
    else:
        result_var.set("You lose!")

def on_choice_selected():
    user_choice = choice_var.get()
    determine_winner(user_choice)

root = tk.Tk()
root.title("Rock Paper Scissors")

choices = ["Rock", "Paper", "Scissors"]

choice_label = tk.Label(root, text="Choose: ")
choice_label.grid(row=0, column=0, padx=10, pady=10)
choice_var = tk.StringVar()
choice_var.set(choices[0])
choice_menu = tk.OptionMenu(root, choice_var, *choices)
choice_menu.grid(row=0, column=1, padx=10, pady=10)

select_button = tk.Button(root, text="Select", command=on_choice_selected)
select_button.grid(row=0, column=2, padx=10, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=1, columnspan=3, padx=10, pady=10)

result_var = tk.StringVar()
result_display = tk.Label(root, textvariable=result_var, font=("Helvetica", 16))
result_display.grid(row=2, columnspan=3, padx=10, pady=10)

user_score = 0
computer_score = 0
score_label = tk.Label(root, text="Score:", font=("Helvetica", 14))
score_label.grid(row=3, column=0, padx=10, pady=5)

def update_score():
    score_label.config(text=f"Score: You {user_score} - Computer {computer_score}")

update_score()

def update_game_result(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    update_score()

def on_choice_selected():
    user_choice = choice_var.get()
    determine_winner(user_choice)
    update_game_result(result_var.get())

def play_again():
    result_text.set("")
    result_var.set("")
    choice_var.set(choices[0])

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.grid(row=4, columnspan=3, padx=10, pady=10)

root.mainloop()