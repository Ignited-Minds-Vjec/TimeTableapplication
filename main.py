import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import time
import webbrowser

days = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
}

timing = {
    0: "08:25:00",
    1: "09:15:00",
    2: "10:05:00",
    3: "10:55:00",
    4: "11:45:00",
    5: "12:35:00",
    6: "01:25:00"
}


links = {
    "Ms. Divya": "https://meet.google.com/gxw-tjzh-tzm",
    "Ms. Jeethu": "https://meet.google.com/tgu-syum-kkn",
    "Ms. Akhila": "https://meet.google.com/byh-xpvu-its",
    "Ms. Vidhya": "https://meet.google.com/oop-kqsp-zxu",
    "Ms. Tintu": "https://meet.google.com/mon-xjru-cat",
    "Ms. Asha": "https://meet.google.com/uyz-sogj-dvo",
    "Ms. Derroll": "https://meet.google.com/zbc-oryd-uhx",
    "Ms. Achala": "https://meet.google.com/kyu-wguq-psi"
}

tt = [
    ["Ms. Jeethu", "Ms. Vidhya", "Ms. Asha", "Ms. Tintu", "Ms. Akhila", "Ms. Divya"],
    ["NULL", "NULL", "NULL", "Ms. Divya", "Ms. Asha", "Ms. Akhila"],
    ["Ms. Jeethu", "Ms. Asha", "Ms. Divya", "Ms. Tintu", "Ms. Akhila", "Ms. Tintu"],
    ["Ms. Jeethu", "Ms. Tintu", "Ms. Divya", "NULL", "NULL", "NULL"],
    ["NULL", "Ms. Vidhya", "Ms. Jeethu", "Ms. Asha", "Ms. Akhila", "Ms. Vidhya"]
]
periodCount = 6
noOfDays = 5
c = 0


class TimeTableApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Developer, DataPage_1, DataPage_2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(DataPage_1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def destroy_frame(self):
        self.destroy()

    def periodClassOpener(self, k):
        webbrowser.open_new(links[k])

    def periodNowOpener(self):
        t = time.ctime()
        l = t.split(" ")
        day = l[0]
        k = days[day]
        now = l[4]

        if noOfDays == 5 or day == "Sun" or now < timing[0] or timing[len(timing)-1]:
            messagebox.showinfo("Error", "Classes NOT Available")
        else:
            flag = 0
            for i in range(periodCount):
                atl = timing[i]
                ath = timing[i + 1]
                if atl <= now < ath:
                    flag = 1
                    classes = tt[k][i]
                    if classes == "NULL":
                        messagebox.showinfo("Error", "Multiple Options available\nUse Dropdown")
                    else:
                        webbrowser.open_new(links[classes])
            if flag == 0:
                messagebox.showinfo("Error", "Classes NOT Available/\n Multiple Options available")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="MY TIME",
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
        period = ttk.Combobox(self, width=20, values=
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

        label1 = tk.Label(self, text="MY TIME",
                          foreground="red",
                          font=("Times New Roman", 15))
        label1.pack(padx=50, pady=10)

        label2 = tk.Label(self, text="Time Table App\nDevelopers",
                          foreground="red",
                          font=("Times New Roman", 13))
        label2.pack()

        label3 = tk.Label(self, text="Adila Farha P K\nNathasha K V\n(S3 CSE B)\nArchana A\nAromal Joseph K M\n"
                                     "Agin Chandran\n(S7 CSE)",
                          foreground="green",
                          font=("Times New Roman", 10))
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


class DataPage_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global periodCount, noOfDays, c
        label1 = tk.Label(self, text="MY TIME",
                          foreground="red",
                          font=("Times New Roman", 15))
        label1.pack(padx=50, pady=10)

        label2 = tk.Label(self, text="Time Table App",
                          foreground="red",
                          font=("Times New Roman", 13))
        label2.pack()

        label3 = tk.Label(self, text="Enter the No of Working Days :",
                          foreground="black",
                          font=("Times New Roman", 10))
        label3.pack()

        Days = ttk.Combobox(self, width=20, values=('5', '6'))

        Days.current(0)
        Days.pack(pady=5)
        noOfDays = int(Days.get())
        label4 = tk.Label(self, text="Enter the No of Periods in a day :",
                          foreground="black",
                          font=("Times New Roman", 10))
        label4.pack()

        Count = ttk.Combobox(self, width=20, values=('1', '2', '3', '4', '5', '6', '7', '8'))

        Count.current(0)
        Count.pack(pady=5)
        periodCount = int(Count.get())
        button1 = tk.Button(self, text="Set & Continue",
                            command=lambda: controller.show_frame(DataPage_2))
        button1.pack(pady=5)

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack(pady=5)


class DataPage_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global c, periodCount, noOfDays
        c += 1
        label1 = tk.Label(self, text="MY TIME",
                          foreground="red",
                          font=("Times New Roman", 15))
        label1.pack(padx=50, pady=10)

        label2 = tk.Label(self, text="Time Table App",
                          foreground="red",
                          font=("Times New Roman", 13))
        label2.pack()

        label3 = tk.Label(self, text="Enter the Timing 24 hrs:",
                          foreground="black",
                          font=("Times New Roman", 10))
        label3.pack()

        Timeh = ttk.Combobox(self, width=20, values=())
        Timem = ttk.Combobox(self, width=10, values=())
        Timeh.current(0)
        Timem.current(0)
        Timeh.pack(pady=5)
        Timem.pack(pady=5)

        if c == periodCount:
            label4 = tk.Label(self, text="Faculty Count or Subject Count :",
                          foreground="black",
                          font=("Times New Roman", 10))
            label4.pack()

            Count = ttk.Combobox(self, width=20, values=('1', '2', '3', '4', '5', '6', '7', '8'))

            Count.current(0)
            Count.pack(pady=5)

        button1 = tk.Button(self, text="Set & Continue",
                            command=lambda: controller.read_data(Days.get(), Count.get()))
        button1.pack(pady=5)

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack(pady=5)


app = TimeTableApp()
app.mainloop()
