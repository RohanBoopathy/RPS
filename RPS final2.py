#IMPORTING MODULE
import tkinter as tk
import random

OPTIONS = ["Rock", "Paper", "Scissors"]
window = tk.Tk()
window.title("Rock Paper Scissors")
window.config(bg='yellow')
player_score = 0
computer_score = 0
player_label = tk.Label(window,bg='yellow', text="PLAYER: 0", font=("Caladea", 22))
player_label.pack(pady=10)
computer_label = tk.Label(window, text="COMPUTER: 0", font=("Caladea", 22),bg='yellow')
computer_label.pack(padx=1)

# CREATE THE LABELS AND BUTTONS FOR THE GAME:
def play(option):
    global player_score,computer_score
    computer_choice = random.choice(OPTIONS)

    if option == computer_choice:
        result = "Tie!"
    elif (option == "Rock" and computer_choice == "Scissors" or
          option == "Paper" and computer_choice == "Rock" or
          option == "Scissors" and computer_choice == "Paper"):
        result = ("You win! Computer chose:",computer_choice)
        player_score =player_score +1
    else:
        result = ("Computer wins! Computer chose :",computer_choice)
        computer_score=computer_score+1

    player_label.config(text=f"Player: {player_score}",bg='yellow')
    computer_label.config(text=f"Computer: {computer_score}",bg='yellow')
    #Display the result
    result_label.config(text=result)

#BUTTONS:
rock_button = tk.Button(window, text="Rock", command=lambda: play("Rock"),font=('Caladea',16))
rock_button.pack(pady=2)

paper_button = tk.Button(window, text="Paper", command=lambda: play("Paper"),font=('Caladea',16))
paper_button.pack(pady=2)

scissors_button = tk.Button(window, text="Scissors", command=lambda: play("Scissors"),font=('Caladea',16))
scissors_button.pack(pady=2)

result_label = tk.Label(window,text="Choose an option:",bg='yellow',font=('caladea',24) )
result_label.pack()

#TkinteR LOOP:
window.mainloop()
