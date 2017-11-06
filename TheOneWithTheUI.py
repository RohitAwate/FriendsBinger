import tkinter as tk
from TheOneWithTheLogic import play_episode


window = tk.Tk()
window.geometry("300x60")
window.title("Friends Binger")
play_button = tk.Button(text="PLAY A RANDOM EPISODE", command=play_episode)
play_button.grid(column=0, row=0)


window.mainloop()
