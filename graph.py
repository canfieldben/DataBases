from tkinter import *
import numpy as np
import matplotlib.pyplot as plt



root = Tk()
root.title("Salty Inc. Graphing")
root.geometry("400x400")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()


show_graph = Button(root, text="Show Graph", command=graph)
show_graph.pack()
root.mainloop()


