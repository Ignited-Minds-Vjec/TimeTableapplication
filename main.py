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
    "Fri": 4,
    "Sat": 5,
}

alltiming = {
    0: "08:25:00",
    1: "09:15:00",
    2: "10:05:00",
    3: "10:55:00",
    4: "11:45:00",
    5: "12:35:00",
    6: "01:25:00"
}

fritiming = {
    0: "07:55:00",
    1: "08:40:00",
    2: "09:25:00",
    3: "10:10:00",
    4: "10:55:00",
    5: "11:40:00",
    6: "12:25:00"
}




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
        webbrowser.open_new(links[k])

    def periodNowOpener(self):
        t = time.ctime()
        l = t.split(" ")
        day = l[0]
        k = days[day]
        now = l[4]

        if day == "Sat" or day == "Sun":
            messagebox.showinfo("Error", "Classes NOT Available")
        elif day == "Fri":
            flag = 0
            for i in range(6):
                atl = fritiming[i]
                ath = fritiming[i + 1]
                if atl <= now < ath:
                    flag = 1
                    classes = tt[k][i]
                    if classes == "NULL":
                        messagebox.showinfo("Error", "Multiple Options available")
                    else:
                        webbrowser.open_new(links[classes])
            if flag == 0:
                messagebox.showinfo("Error", "Classes NOT Available/\n Multiple Options available")
        else:
            flag = 0
            for i in range(6):
                atl = alltiming[i]
                ath = alltiming[i + 1]
                if atl <= now < ath:
                    flag = 1
                    classes = tt[k][i]
                    if classes == "NULL":
                        messagebox.showinfo("Error", "Multiple Options available\nUse Dropdown")
                    else:
                        webbrowser.open_new(links[classes])
            if flag == 0:
                messagebox.showinfo("Error", "Classes NOT Available/\n Multiple Options available")

    def destroy_frame(self):
        self.destroy()


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

        label3 = tk.Label(self, text="Adila Farha P K\nNathasha K V\n(S3 CSE B)\nArchana A\nAromal Joseph K M\nAgin Chandran\n(S7 "
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
