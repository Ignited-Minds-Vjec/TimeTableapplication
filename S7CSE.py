import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import webbrowser

days = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4
}

alltiming = {
    "08:25:00": 0,
    "09:15:00": 1,
    "10:05:00": 2,
    "10:55:00": 3,
    "11:45:00": 4,
    "12:35:00": 5,
    "01:25:00": 6
}

fritiming = {
    "07:55:00": 0,
    "08:40:00": 1,
    "09:25:00": 2,
    "10:10:00": 3,
    "10:55:00": 4,
    "11:40:00": 5,
    "12:25:00": 6
}

S7_CSE_links = {
    "Ms. Divya": "https://meet.google.com/gxw-tjzh-tzm",
    "Ms. Jeethu": "https://meet.google.com/tgu-syum-kkn",
    "Ms. Akhila": "https://meet.google.com/byh-xpvu-its",
    "Ms. Vidhya": "https://meet.google.com/oop-kqsp-zxu",
    "Ms. Tintu": "https://meet.google.com/mon-xjru-cat",
    "Ms. Asha": "https://meet.google.com/uyz-sogj-dvo",
    "Ms. Derroll": "https://meet.google.com/zbc-oryd-uhx",
    "Ms. Achala": "https://meet.google.com/kyu-wguq-psi"
}

S7_CSE_tt = [
    ["Ms. Jeethu", "Ms. Vidhya", "Ms. Asha", "Ms. Tintu", "Ms. Akhila", "Ms. Divya"],
    ["NULL", "NULL", "NULL", "Ms. Divya", "Ms. Asha", "Ms. Akhila"],
    ["Ms. Jeethu", "Ms. Asha", "Ms. Divya", "Ms. Tintu", "Ms. Akhila", "Ms. Tintu"],
    ["Ms. Jeethu", "Ms. Tintu", "Ms. Divya", "NULL", "NULL", "NULL"],
    ["NULL", "Ms. Vidhya", "Ms. Jeethu", "Ms. Asha", "Ms. Akhila", "Ms. Vidhya"]
]


def get_keyFriday(val):
    for key, value in fritiming.items():
        if val == value:
            return key


def get_key(val):
    for key, value in alltiming.items():
        if val == value:
            return key


class TimeTableApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Developer):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def periodClassOpener(self, k):
        webbrowser.open_new(S7_CSE_links[k])

    def periodNowOpener(self):
        t = time.ctime()
        l = t.split(" ")
        day = l[0]
        k = days[day]
        now = l[3]
        if day == "Sat" or day == "Sun":
            messagebox.showinfo("Error", "Classes NOT Available")
        elif day == "Fri":
            flag = 0
            for i in range(6):
                atl = get_keyFriday(i)
                ath = get_keyFriday(i + 1)
                if atl <= now < ath:
                    flag = 1
                    classes = S7_CSE_tt[k][i]
                    if classes == "NULL":
                        messagebox.showinfo("Error", "Multiple Options available")
                    else:
                        webbrowser.open_new(S7_CSE_links[classes])
            if flag == 0:
                messagebox.showinfo("Error", "Classes NOT Available/\n Multiple Options available")
        else:
            flag = 0
            for i in range(6):
                atl = get_key(i)
                ath = get_key(i + 1)
                if atl <= now < ath:
                    flag = 1
                    classes = S7_CSE_tt[k][i]
                    if classes == "NULL":
                        messagebox.showinfo("Error", "Multiple Options available\nUse Dropdown")
                    else:
                        webbrowser.open_new(S7_CSE_links[classes])
            if flag == 0:
                messagebox.showinfo("Error", "Classes NOT Available/\n Multiple Options available")

    def destroy_frame(self):
        self.destroy()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="S7 CSE VJEC",
                          foreground="red",
                          font=("Times New Roman", 15))
        label1.pack(padx=50, pady=10)

        label2 = tk.Label(self, text="Time Table",
                          foreground="red",
                          font=("Times New Roman", 12))
        label2.pack(padx=50, pady=5)

        label3 = tk.Label(self, text="Select Your Period :", font=("Times New Roman", 10))
        label3.pack(pady=5)

        # Combobox creation
        period = ttk.Combobox(self, width=27, values=
        ('Ms. Divya', 'Ms. Jeethu', 'Ms. Akhila', 'Ms. Vidhya', 'Ms. Tintu', 'Ms. Asha', 'Ms. Derroll', 'Ms. Achala'))

        period.current(0)
        period.pack(pady=5)

        btn1 = tk.Button(self, text='Join Now', bd='5', command=lambda: controller.periodClassOpener(period.get()))
        btn1.pack(padx=10, pady=10)

        btn2 = tk.Button(self, text='Immediate Join', bd='5', command=lambda: controller.periodNowOpener())
        btn2.pack(padx=10, pady=10)

        button = tk.Button(self, text="Developers",
                           command=lambda: controller.show_frame(Developer))
        button.pack(pady=5)

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack(pady=5)


class Developer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="S7 CSE VJEC",
                          foreground="red",
                          font=("Times New Roman", 15))
        label1.pack(padx=50, pady=10)

        label2 = tk.Label(self, text="Time Table App\nDevelopers",
                          foreground="red",
                          font=("Times New Roman", 13))
        label2.pack()

        label3 = tk.Label(self, text="Adila Farha P K\nNathasha K V\n(S3 CSE B)\nArchana A\nAromal Joseph K M\n(S7 "
                                     "CSE)",
                          foreground="green",
                          font=("Times New Roman",10))
        label3.pack()

        label4 = tk.Label(self, text="Special Thanks to:\nTeam Ignited Minds",
                          foreground="red",
                          font=("Times New Roman", 10))
        label4.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=5)

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack(pady=5)


app = TimeTableApp()
app.mainloop()
