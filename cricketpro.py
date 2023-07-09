import random
import tkinter as tk
from tkinter import messagebox

target = random.randint(1, 30)

def game():
    b = 0
    while True:
        a = int(input("Enter the run you want to hit between 1 to 6: "))
        d = ["Bowled", "catch-out", "stumpout"]
        c = random.randint(1, 6)
        if a != c:
            print(f"You hit {a} run")
            b += a
        else:
            b += a
            print(f"You are {random.choice(d)}")
            print(f"Your total score is {b} runs")
            break

def button_click(event):
    text = event.widget.cget("text")
    d = ["bowled", "catch-out", "stumpout", "hit-wicket"]
    run = int(b.cget("text").split('=')[1].strip())
    c = random.randint(1, 6)

    if text != str(c):
        a = tk.Label(root, text=f"You hit {text} runs", font=("Arial", 16), fg="green")
        a.pack()
        run += int(text)
        b.config(text=f"run = {run}", font=("Arial", 16), fg="black")
        if run >= target:
            y = tk.Label(root, text=f"You win the game", font=("Arial", 16), fg="blue")
            y.pack()
            messagebox.showinfo("Game Result", "You win the game, Good job champ")
            root.quit()
    else:
        result = random.choice(d)
        b.config(text=f"run = {run} (You are {result})", font=("Arial", 16), fg="red")
        c = tk.Label(root, text=f"Your total score is {run} runs", font=("Arial", 16), fg="black")
        c.pack()

def text():
    x = tk.Label(root, text=f"Your Target is {target} runs", font=("Arial", 16), fg="purple")
    x.pack()
    e = tk.Label(root, text=f"Score Card", font=("Arial", 16), fg="black")
    e.pack()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    runs = ["1", "2", "3", "4", "5", "6"]
    for run in runs:
        btn = tk.Button(button_frame, text=run, font="Arial 15 bold", width=5)
        btn.pack(side=tk.LEFT, padx=10, pady=10)
        btn.bind("<Button-1>", button_click)

    b.config(text="run = 0", font=("Arial", 16), fg="black")

root = tk.Tk()
root.geometry("600x400")
root.title("Hand Cricket")

a = tk.Label(root, text="Welcome to the game of hand cricket", font=("Arial", 16), fg="navy")
a.pack(side=tk.TOP)
b = tk.Label(root, text="To play press Yesssss", font=("Arial", 16), fg="black")
b.pack()
btn = tk.Button(root, text="Yes", command=text, font=("Arial", 16))
btn.pack()

root.mainloop()



