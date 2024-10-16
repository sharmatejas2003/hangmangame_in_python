import tkinter as tk
import random

class HangmanApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Challenge")

        self.words = ["python", "hangman", "challenge", "programming", "developer"]
        self.secret_word = random.choice(self.words)
        self.guesses = []
        self.remaining_attempts = 6

        # Labels and Entry
        self.current_state_label = tk.Label(master, text="")
        self.current_state_label.pack(pady=10)

        self.attempts_label = tk.Label(master, text=f"Incorrect guesses remaining: {self.remaining_attempts}")
        self.attempts_label.pack(pady=10)

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

        self.update_display()

    def update_display(self):
        """Update the displayed word and attempts remaining."""
        display_word = ''.join(letter if letter in self.guesses else '_' for letter in self.secret_word)
        self.current_state_label.config(text=f"Current word: {display_word}")
        self.attempts_label.config(text=f"Incorrect guesses remaining: {self.remaining_attempts}")

    def submit_guess(self):
        """Handle the user's guess."""
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.result_label.config(text="Please enter a single letter.")
            return

        if guess in self.guesses:
            self.result_label.config(text="You've already guessed that letter.")
            return

        self.guesses.append(guess)

        if guess in self.secret_word:
            self.result_label.config(text="Good guess!")
        else:
            self.remaining_attempts -= 1
            self.result_label.config(text="Incorrect guess.")

        if self.check_win():
            self.result_label.config(text=f"Congratulations! You've guessed the word '{self.secret_word}'!")
            self.submit_button.config(state=tk.DISABLED)
        elif self.remaining_attempts <= 0:
            self.result_label.config(text=f"Game over! The word was '{self.secret_word}'.")
            self.submit_button.config(state=tk.DISABLED)

        self.update_display()

    def check_win(self):
        """Check if the player has guessed the word."""
        return all(letter in self.guesses for letter in self.secret_word)

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
