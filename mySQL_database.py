from tkinter import *
import mysql.connector

# create tkinter window
root = Tk()
root.title('mySQL Database')
root.geometry('400x400')

# connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cabinVT!1",
    database="saltyGraphing"
)

# create cursor
my_cursor = mydb.cursor()

# create database
# my_cursor.execute("CREATE DATABASE saltyGraphing")

# database creation test
'''
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
'''

# create database table
'''
my_cursor.execute("CREATE TABLE graphs "
                  "(graph_name VARCHAR(255), "
                  "x_axis int(10), "
                  "y_axis int(10), "
                  "graph_id INT AUTO_INCREMENT PRIMARY KEY)")
'''

# show table
'''
my_cursor.execute("SELECT * FROM graphs")
for entry in my_cursor.description:
    print(entry)
'''


# clear entry boxes
def clear_boxes():
    graph_name_box.delete(0, END)
    x_axis_box.delete(0, END)
    y_axis_box.delete(0, END)


# submit graph to database
def submit_graph():
    sql_command = "INSERT INTO graphs (graph_name, x_axis, y_axis) VALUES (%s, %s, %s)"
    values = (graph_name_box.get(), x_axis_box.get(), y_axis_box.get())
    my_cursor.execute(sql_command, values)
    mydb.commit()
    clear_boxes()


# list graphs
def list_graphs():
    my_cursor.execute("SELECT * FROM graphs")
    graph_list = my_cursor.fetchall()
    for graph in graph_list:
        print(graph)


# get graphs
def get_graph():
    return


def store_graph():
    return


def show_graphs():
    return


# labels
title_label = Label(root, text="Salty Inc. Graphing", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

graph_name_label = Label(root, text="Graph Name:")
graph_name_label.grid(row=1, column=0)
x_axis_label = Label(root, text="X-Axis:")
x_axis_label.grid(row=2, column=0)
y_axis_label = Label(root, text="Y-Axis:")
y_axis_label.grid(row=3, column=0)

# entry boxes
graph_name_box = Entry(root, width=30)
graph_name_box.grid(row=1, column=1, padx=20, pady=(10, 0))
x_axis_box = Entry(root, width=30)
x_axis_box.grid(row=2, column=1)
y_axis_box = Entry(root, width=30)
y_axis_box.grid(row=3, column=1)

# buttons
store_graph_button = Button(root, text="Store Graph", command=store_graph)
store_graph_button.grid(row=4, column=0, ipadx=20, padx=10, pady=10)
show_graphs_button = Button(root, text="Show Graphs", command=show_graphs)
show_graphs_button.grid(row=4, column=1, ipadx=20, padx=10, pady=10)


# show graphs
'''my_cursor.execute("SELECT * FROM graphs")
result = my_cursor.fetchall()
for item in result:
    print(item)
'''


root.mainloop()
