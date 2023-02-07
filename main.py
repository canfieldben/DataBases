import tkinter as tk

root = tk.Tk()
root.title("Calculator")

canvas1 = tk.Canvas(root, width=200, height=150)
canvas1.pack()

label3 = tk.Label(root, text="Calculator")
canvas1.create_window(100, 25, window=label3)

entry1 = tk.Entry(root)
canvas1.create_window(100, 50, window=entry1)


def calc():
    bio_val = entry1.get()

    label2 = tk.Label(root, text="Value:")
    canvas1.create_window(100, 75, window=label2)

    label1 = tk.Label(root, text=bio_val)
    canvas1.create_window(100, 100, window=label1)


button1 = tk.Button(text='Calculate', command=calc)
canvas1.create_window(100, 125, window=button1)

root.mainloop()
