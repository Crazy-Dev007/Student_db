from tkinter import *
import sqlite3
root = Tk()
# title to window
root.title(" Student Database ")
# win geometry
root.geometry("400x600")

# create db or connect to db
conn = sqlite3.connect("StudentDB.db")

# crate cursor
c = conn.cursor()
'''
c.execute("""CREATE TABLE STUDENT(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''
# To update the record


def update():
    # create db or connect to db
    conn = sqlite3.connect("StudentDB.db")

    # crate cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE STUDENT SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
    
    WHERE oid = :oid""",
              {'first': f_name_editor.get(),
               'last': l_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               'zipcode': zipcode_editor.get(),
               'oid': record_id

               })
    conn.commit()

    conn.close()
    editor.destroy()

# Edit a Record


def edit():
    global editor
    editor = Tk()
    # title to window
    editor.title(" Update a Record ")
    # win geometry
    editor.geometry("400x400")
    # create db or connect to db
    conn = sqlite3.connect("StudentDB.db")

    # crate cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM STUDENT WHERE oid = " + record_id)
    records = c.fetchall()

    # Create Golbal Variable for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # create textboxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # create text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # button to save record
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


# Create  Funtion to Delete A Record
def delete():
    # create db or connect to db
    conn = sqlite3.connect("StudentDB.db")

    # crate cursor
    c = conn.cursor()

    # Delete a Record
    c.execute("DELETE FROM STUDENT WHERE oid= " + delete_box.get())

    conn.commit()

    conn.close()


# crate submit Function for datebase

def submit():
    # create db or connect to db
    conn = sqlite3.connect("StudentDB.db")

    # crate cursor
    c = conn.cursor()

    c.execute("INSERT INTO STUDENT VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    conn.commit()

    conn.close()

    # clear The text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
# Create Query Function


def query():
    # create db or connect to db
    conn = sqlite3.connect("StudentDB.db")

    # crate cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM STUDENT")
    records = c.fetchall()
    # printting on console
    # print(records)

    # printting records
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + \
            str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()

    conn.close()


def valid_del():
    if str(delete_box.get()) == "":
        pass
    else:
        delete()


def valid_submit():
    if str(f_name.get()) == "" and str(l_name.get()) == "" and str(address.get()) == "" and str(city.get()) == "" and str(state.get()) == "" and str(zipcode.get()) == "":
        pass
    else:
        submit()


# create textboxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0,  pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_label = Label(root, text="Select ID")
delete_label.grid(row=9, column=0, pady=5)


# buttons
submit_btn = Button(root, text="Add Record To Database", command=valid_submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# delete btn
delete_btn = Button(root, text="Delete Record", command=valid_del)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


conn.commit()

conn.close()

root.mainloop()
