import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox as tkmbox

window=tk.Tk() #ini adalah syntax pertama tkinter

frame_input=ttk.Frame(window)
frame_input.pack(padx=10,pady=10)

name_var=tk.StringVar()
pwd_var=tk.StringVar()

def submit():
 
    name=name_var.get()
    pwd=pwd_var.get()
    conn = sqlite3.connect('test.db')
 
    print("The name is : " + name)
    print("The password is : " + pwd)

    conn.execute("INSERT INTO COMPANY (NAMA,PASSWORD) VALUES (?,?)",(name,pwd))
    conn.commit()
    conn.close()
    name_var.set("")
    pwd_var.set("")

def lihat():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    tkmbox.showinfo("Say Hello",rows)
    conn.close()


name_label = ttk.Label(frame_input,text = 'Username', font=('calibre',10, 'bold'))
name_label.pack()

name_entry = ttk.Entry(frame_input,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.pack()

passw_label = ttk.Label(frame_input, text = 'Password', font = ('calibre',10,'bold'))
passw_label.pack()

passw_entry=ttk.Entry(frame_input, textvariable = pwd_var, font = ('calibre',10,'normal'), show = '*')
passw_entry.pack()

sub_btn=ttk.Button(frame_input,text = 'Submit', command = submit)
sub_btn.pack()

shwdb_btn=ttk.Button(frame_input,text = 'Lihat Daftar',command = lihat)
shwdb_btn.pack()

window.mainloop()
