from tkinter import *
import sqlite3

root = Tk()
root.title("Salty Inc. Database")
root.geometry("400x600")

# databases

conn = sqlite3.connect('database.db')

c = conn.cursor()

'''
c.execute("""CREATE TABLE addresses (first_name text, 
                                    last_name text, 
                                    address text, 
                                    city text, 
                                    state text, 
                                    zipcode integer)""")
'''


# create function to delete record
def delete():
    # create a database or connect to one
    conn = sqlite3.connect('database.db')
    # create cursor
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid=" + ID_box.get())
    # commit changes
    conn.commit()
    # close connection
    conn.close()


# Create Submit button
def submit():
    # create a database or connect to one
    conn = sqlite3.connect('database.db')
    # create cursor
    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # commit changes
    conn.commit()
    # close connection
    conn.close()

    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# create query function
query_label = Label(root, text="", justify=LEFT)
query_label.grid(row=12, column=0, columnspan=2)


def query():
    # create a database or connect to one
    conn = sqlite3.connect('database.db')
    # create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SElECT *, oid FROM addresses ORDER BY last_name")
    records = c.fetchall()
    # print(records
    print_records = ""

    # loop through results
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + "\t" + str(record[6]) + "\n"

    query_label.config(text=print_records)

    # commit changes
    conn.commit()
    # close connection
    conn.close()
    ID_box.delete(0, END)
    search_box.delete(0, END)


# create an information function
def information():
    # create a database or connect to one
    conn = sqlite3.connect('database.db')
    # create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses WHERE oid=" + ID_box.get())
    user = c.fetchone()

    query_label.config(
        text="First:\t\t{}\nLast:\t\t{}\nAddress:\t\t{}\nCity:\t\t{}\nState:\t\t{}\nZipcode:\t\t{}\nID:\t\t{}\n".format(
            str(user[0]),
            str(user[1]),
            str(user[2]),
            str(user[3]),
            str(user[4]),
            str(user[5]),
            str(user[6])))

    # commit changes
    conn.commit()
    # close connection
    conn.close()


# define search function
def search():
    # create a database or connect to one
    conn = sqlite3.connect('database.db')
    # create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SElECT *, oid FROM addresses ORDER BY last_name")
    users = c.fetchall()
    user_list = []
    print_records = ""

    # searches for matching last names in record
    for user in users:
        if user[1].lower() == (search_box.get()).lower():
            user_list.append(user)

    # loop records and formats them
    for record in user_list:
        print_records += str(record[0]) + " " + str(record[1]) + " " + " " + "\t" + str(record[6]) + "\n"

    # prints them to the label
    query_label.config(text=print_records)

    # commit changes
    conn.commit()
    # close connection
    conn.close()
    ID_box.delete(0, END)


# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

ID_box = Entry(root, width=30)
ID_box.grid(row=9, column=1, pady=10)

search_box = Entry(root, width=30)
search_box.grid(row=7, column=1, pady=10, padx=10)

# create text box labels
f_name_label = Label(root, text="First Name:")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name:")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address:")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City:")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State:")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zip Code:")
zipcode_label.grid(row=5, column=0)

ID_label = Label(root, text="ID Number:")
ID_label.grid(row=9, column=0, pady=10)

search_label = Label(root, text="Last Name:")
search_label.grid(row=7, column=0, pady=10)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

# Create Query button
query_btn = Button(root, text="Show All Records", command=query)
query_btn.grid(row=8, column=0, columnspan=1, padx=10, ipadx=20)

# Create a show info button
show_info_btb = Button(root, text="Show ID Information", command=information)
show_info_btb.grid(row=10, column=0, columnspan=2, padx=10, ipadx=110)

# create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create a search button
search_btn = Button(root, text="Search For Record", command=search)
search_btn.grid(row=8, column=1, ipadx=40)

conn.commit()

conn.close()

root.mainloop()
