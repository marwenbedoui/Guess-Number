import tkinter as tk
from tkinter import messagebox
from game import NumberGuessingGame
import database

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.game = NumberGuessingGame()
        self.buttons = []
        self.create_widgets()
        database.create_table()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Guess a number between 1 and 100")
        self.label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        for i in range(1, 101):
            btn = tk.Button(self.buttons_frame, text=str(i), command=lambda i=i: self.make_guess(i))
            btn.grid(row=(i-1)//10, column=(i-1)%10, padx=5, pady=5)
            self.buttons.append(btn)

    def make_guess(self, number):
        if self.game.guess(number):
            self.buttons[number-1].config(bg="green")
            messagebox.showinfo("Congratulations!", f"You guessed the number {self.game.secret_number} in {self.game.attempts} attempts!")
            database.store_attempt(self.game.attempts)
            self.root.destroy()
        else:
            self.buttons[number-1].config(bg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()
    
    # Fetch and print stored attempts after the game ends
    attempts = database.fetch_attempts()
    for attempt in attempts:
        print(f"ID: {attempt[0]}, Attempts: {attempt[1]}, Date: {attempt[2]}")
