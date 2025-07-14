import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

canvas.create_rectangle(50, 50, 150, 102, fill="blue")

canvas.create_oval(298, 98, 302, 102, fill="black")

canvas.create_oval(170, 170, 230, 230, fill="red")

root.mainloop()
