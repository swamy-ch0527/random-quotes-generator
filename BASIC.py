import tkinter as tk
import random

quotes = [
    "The only way to do great work is to love what you do. — Steve Jobs",
    "Keep going. Everything you need will come to you at the perfect time.",
    "Believe you can and you're halfway there. — Theodore Roosevelt",
    "It always seems impossible until it's done. — Nelson Mandela",
    "Start where you are. Use what you have. Do what you can. — Arthur Ashe",
    "Success is the sum of small efforts repeated day in and day out.",
]

def new_quote():
    quote_label.config(text=random.choice(quotes))

root = tk.Tk()
root.title("Motivational Quotes")
root.geometry("400x200")
root.config(bg="#f7f7f7")

quote_label = tk.Label(root, text="Click below for a quote!", wraplength=350, 
                       justify="center", font=("Arial", "20"), bg="#f7f7f7", fg="#333")
quote_label.pack(pady=25)

btn = tk.Button(root, text="Next Quote", command=new_quote, 
                bg="#4CAF50", fg="white", font=("Arial", 15, "bold"), padx=15, pady=10)
btn.pack()

root.mainloop()