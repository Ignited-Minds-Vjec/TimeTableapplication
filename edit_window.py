import S7TT
import tkinter as tk
from tkinter import ttk


def prn(x):
    print(x)


def label_change(event=None):
    value1 = tk.StringVar()
    value2 = tk.StringVar()
    value3 = tk.StringVar()
    value4 = tk.StringVar()
    value5 = tk.StringVar()
    value6 = tk.StringVar()

    label1 = tk.Label(edit, textvariable=value1, font=("arial", 10), width=30)
    label1.grid(row=2, column=0, pady=5, padx=10)

    label2 = tk.Label(edit, textvariable=value2, font=("arial", 10), width=30)
    label2.grid(row=3, column=0, pady=5, padx=10)

    label3 = tk.Label(edit, textvariable=value3, font=("arial", 10), width=30)
    label3.grid(row=4, column=0, pady=5, padx=10)

    label4 = tk.Label(edit, textvariable=value4, font=("arial", 10), width=30)
    label4.grid(row=5, column=0, pady=5, padx=10)

    label5 = tk.Label(edit, textvariable=value5, font=("arial", 10), width=30)
    label5.grid(row=6, column=0, pady=5, padx=10)

    label6 = tk.Label(edit, textvariable=value6, font=("arial", 10), width=30)
    label6.grid(row=7, column=0, pady=5, padx=10)

    selection = weekdays_comboBox.current()
    value1.set(S7TT.S7_CSE_tt[selection][0])
    value2.set(S7TT.S7_CSE_tt[selection][1])
    value3.set(S7TT.S7_CSE_tt[selection][2])
    value4.set(S7TT.S7_CSE_tt[selection][3])
    value5.set(S7TT.S7_CSE_tt[selection][4])
    value6.set(S7TT.S7_CSE_tt[selection][5])


def submit():
    one = period1.get()
    two = period2.get()
    three = period3.get()
    four = period4.get()
    five = period5.get()
    six = period6.get()
    print(one, two, three, four, five, six)
    S7TT.S7_CSE_tt[weekdays_comboBox.current()][0] = one
    S7TT.S7_CSE_tt[weekdays_comboBox.current()][1] = two
    S7TT.S7_CSE_tt[weekdays_comboBox.current()][2] = three
    S7TT.S7_CSE_tt[weekdays_comboBox.current()][3] = four
    S7TT.S7_CSE_tt[weekdays_comboBox.current()][4] = five
    S7TT.S7_CSE_tt[weekdays_comboBox.current()][5] = six


edit = tk.Tk()
edit.geometry("450x300")
edit.resizable(False, False)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
dayLabel = tk.Label(edit, text="Choose day:", font=("arial", 13))
dayLabel.grid(row=0, column=0, pady=5)
weekdays_comboBox = ttk.Combobox(edit, width=15, font=("arial", 10),
                                 state="readonly",
                                 values=weekdays)
weekdays_comboBox.current(0)
label_change()
weekdays_comboBox.bind("<<ComboboxSelected>>", label_change)
weekdays_comboBox.grid(row=0, column=1, padx=10)

print(weekdays_comboBox.get())
i = 0

labelNow = tk.Label(edit, text="Current Selection", font=("arial", 12, "bold"), width=25)
labelNow.grid(row=1, column=0)

labelChange = tk.Label(edit, text="New Selection", font=("arial", 12, "bold"))
labelChange.grid(row=1, column=1)

# -----------------Subject selection Combobox------------
subjects = list(S7TT.S7_SubTeachers_Subjects.keys())
period1 = ttk.Combobox(edit, width=15, font=("arial", 10),
                       state="readonly",
                       values=subjects)
period1.grid(row=2, column=1)
period2 = ttk.Combobox(edit, width=15, font=("arial", 10),
                       state="readonly",
                       values=subjects)
period2.grid(row=3, column=1)
period3 = ttk.Combobox(edit, width=15, font=("arial", 10),
                       state="readonly",
                       values=subjects)
period3.grid(row=4, column=1)
period4 = ttk.Combobox(edit, width=15, font=("arial", 10),
                       state="readonly",
                       values=subjects)
period4.grid(row=5, column=1)
period5 = ttk.Combobox(edit, width=15, font=("arial", 10),
                       state="readonly",
                       values=subjects)
period5.grid(row=6, column=1)
period6 = ttk.Combobox(edit, width=15, font=("arial", 10),
                       state="readonly",
                       values=subjects)
period6.grid(row=7, column=1)
# -----------------------------------------------------------

submitButton = tk.Button(edit, text="Submit", command=submit)
submitButton.grid(row=8, column=1, pady=10)

edit.mainloop()
