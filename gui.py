import tkinter as tk


def submit():
    name = e1.get()
    age = e2.get()
    print("Name: ", name)
    print("Age: ", age)


def reset():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)


# Window
root = tk.Tk()
root.title("Student Info")


# Labels
tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Age").grid(row=1, column=0)

# Inputs
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Buttons
tk.Button(root, text="Submit", command=submit).grid(row=2, column=0)
tk.Button(root, text="Reset", command=reset).grid(row=2, column=1)

root.mainloop()
