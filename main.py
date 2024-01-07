import tkinter as tk
from tkinter import messagebox
import random


class MemoryGame:
    def __init__(self, master, difficulty):
        self.master = master
        self.master.title("Memory Game")

        self.difficulty = difficulty
        self.grid_size = self.get_grid_size()

        self.cards = [i for i in range(1, (self.grid_size ** 2) // 2 + 1)] * 2
        random.shuffle(self.cards)

        self.buttons = []
        self.selected_cards = []

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                button = tk.Button(self.master, text=" ", width=5, height=2,
                                   command=lambda r=row, c=col: self.flip_card(r, c))
                button.grid(row=row, column=col)
                self.buttons.append(button)

        self.moves_label = tk.Label(self.master, text="Moves: 0")
        self.moves_label.grid(row=self.grid_size, columnspan=self.grid_size)

        self.moves = 0
        self.first_card = None

    def get_grid_size(self):
        if self.difficulty == "easy":
            return 3
        elif self.difficulty == "medium":
            return 4
        elif self.difficulty == "hard":
            return 5
        else:
            return 4

    def flip_card(self, row, col):
        index = row * self.grid_size + col
        card = self.cards[index]

        if card != " ":
            self.buttons[index].config(text=str(card), state=tk.DISABLED)
            self.selected_cards.append((index, card))

            if len(self.selected_cards) == 2:
                self.master.after(500, self.check_match)

    def check_match(self):
        index1, card1 = self.selected_cards[0]
        index2, card2 = self.selected_cards[1]

        if card1 == card2:
            self.cards[index1] = " "
            self.cards[index2] = " "
        else:
            self.buttons[index1].config(text=" ", state=tk.NORMAL)
            self.buttons[index2].config(text=" ", state=tk.NORMAL)

        self.selected_cards = []
        self.moves += 1
        self.moves_label.config(text=f"Moves: {self.moves}")

        if all(card == " " for card in self.cards):
            messagebox.showinfo("Congratulations!", f"You completed the game in {self.moves} moves!")
            self.master.destroy()


# Main function
def main():
    root = tk.Tk()

    level = input("Choose difficulty level (easy, medium, hard): ").lower()
    if level not in ["easy", "medium", "hard"]:
        level = "medium"

    game = MemoryGame(root, level)
    root.mainloop()


if __name__ == "__main__":
    main()
