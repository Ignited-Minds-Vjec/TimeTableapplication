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
    "Ms. Divya K": "https://meet.google.com/gxw-tjzh-tzm",
    "Ms. Jeethu V Devasia": "https://meet.google.com/tgu-syum-kkn",
    "Ms. Akhila Mathew": "https://meet.google.com/byh-xpvu-its",
    "Ms. Vidhya S S": "https://meet.google.com/oop-kqsp-zxu",
    "Ms. Tintu Devasia": "https://meet.google.com/mon-xjru-cat",
    "Ms. Asha Baby": "https://meet.google.com/uyz-sogj-dvo",
    "Ms. Derroll David": "https://meet.google.com/zbc-oryd-uhx",
    "Ms. Achala Prasad": "https://meet.google.com/kyu-wguq-psi"
}

S7_CSE_tt = [
    ["Ms. Jeethu", "Ms. Vidhya", "Ms. Asha", "Ms. Tintu", "Ms. Akhila", "Ms. Divya"],
    ["NULL", "NULL", "NULL", "Ms. Divya", "Ms. Asha", "Ms. Akhila"],
    ["Ms. Jeethu", "Ms. Asha", "Ms. Divya", "Ms. Tintu", "Ms. Akhila", "Ms. Tintu"],
    ["Ms. Jeethu", "Ms. Tintu", "Ms. Divya", "NULL", "NULL", "NULL"],
    ["NULL", "Ms. Vidhya", "Ms. Jeethu", "Ms. Asha", "Ms. Akhila", "Ms. Vidhya"]
]

S5_CSE_links = {
    "Ms. Divya": "https://meet.google.com/gxw-tjzh-tzm",
    "Ms. Jeethu": "https://meet.google.com/tgu-syum-kkn",
    "Ms. Akhila": "https://meet.google.com/byh-xpvu-its",
    "Ms. Vidhya": "https://meet.google.com/oop-kqsp-zxu",
    "Ms. Tintu": "https://meet.google.com/mon-xjru-cat",
    "Ms. Asha": "https://meet.google.com/uyz-sogj-dvo",
    "Ms. Derroll": "https://meet.google.com/zbc-oryd-uhx",
    "Ms. Achala": "https://meet.google.com/kyu-wguq-psi"
}

S5_CSE_tt = [
    ["Ms. Divya", "Ms. Vidhya", "Ms. Asha", "Ms. Tintu", "Ms. Akhila", "Ms. Jeethu"],
    ["NULL", "NULL", "NULL", "Ms. Divya", "Ms. Asha", "Ms. Akhila"],
    ["Ms. Divya", "Ms. Asha", "Ms. Jeethu", "Ms. Tintu", "Ms. Akhila", "Ms. Tintu"],
    ["Ms. Jeethu", "Ms. Tintu", "Ms. Divya", "NULL", "NULL", "NULL"],
    ["NULL", "Ms. Vidhya", "Ms. Jeethu", "Ms. Asha", "Ms. Akhila", "Ms. Vidhya"]
]

S3_CSE_A_links = {
            "Mr. Abdul Latheef":"https://meet.google.com/wpy-gpxv-rwg",
            "Ms. Neena V V":"https://meet.google.com/reo-vuhd-qur",
            "Ms. Anisha Joseph":"https://meet.google.com/ejb-cfdr-bem",
            "Ms. Raiza Yusef":"https://meet.google.com/eak-irdk-cwm",
            "Sr. Jisha C T":"https://meet.google.com/nmf-qnzv-fxn",
            "Ms. Angel Varghese":"https://meet.google.com/wpi-sbpx-bbo",
            "Ms. Reema Mathew A":"https://meet.google.com/wfh-qina-bux",
            "Ms. Anisha Joseph":"https://meet.google.com/afh-addo-wim",
            "Ms. Tintu Devasia":"https://meet.google.com/hah-xuvp-qbp"
        }

S3_CSE_A_tt=[
                ["Mr. Abdul Latheef", "Ms. Neena V V", "Mr. Abdul Latheef", "Ms. Anisha Joseph", "Ms. Raiza Yusef", "Ms. Raiza Yusef"],
                ["Sr. Jisha C T", "Ms. Anisha Joseph ", "Mr. Abdul Latheef ", "NULL", "NULL", "NULL"],
                ["Ms. Raiza Yusef", "Ms. Neena V V", "Ms. Raiza Yusef", "Sr. Jisha C T", "Ms. Angel Varghese", "Ms. Anisha Joseph"],
                ["Mr. Abdul Latheef", "Ms. Angel Varghese", "Ms. Anisha Joseph", "Ms. Neena V V", "Sr. Jisha C T", "Ms. Neena V V"],
                ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
            ]

S3_CSE_B_links = {
            "Ms. Divya B":"https://meet.google.com/jew-jbuj-beq",
            "Ms. Vidhya S S":"https://meet.google.com/uge-prpd-dyg",
            "Ms. Keerthijith P P":"http://meet.google.com/vrv-ohqa-keb",
            "Ms. Divya K Vinod":"http://meet.google.com/cmy-ngie-dto",
            "Ms. Divya B":"https://meet.google.com/eeb-jvyy-zgt",
            "Mr. Manoj V Thomas":"https://meet.google.com/yty-wfdr-jhr",
            "Ms. Shimna P K":"http://meet.google.com/oqr-ksni-tpt",
            "Ms. Angel Varghese":"https://meet.google.com/wpi-sbpx-bbo",
            "Ms. Raiza Yousaf":"https://meet.google.com/nvi-eovz-rsj",
            "Ms. Asha Baby":"http://meet.google.com/bch-yhpr-dun"
        }

S3_CSE_B_tt=[
                ["Ms. Keerthijith P P", "Mr. Manoj V Thomas", "Ms. Raiza Yousaf", "NULL", "NULL", "NULL"],
                ["Ms. Raiza Yousaf", "Ms. Vidhya S S ", "Ms. Divya B ", "Ms. Keerthijith P P", "NULL", "NULL"],
                ["Ms. Divya B", "Ms. Vidhya S S", "Ms. Angel Varghese", "NULL", "NULL", "NULL"],
                ["Ms. Raiza Yousaf", "Ms. Divya B", "Ms. Keerthijith P P", "Ms. Raiza Yousaf"],
                ["Ms. Angel Varghese", "Ms. Divya B", "Mr. Manoj V Thomas", "Ms. Vidhya S S", "NULL", "NULL"]
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

        for F in (ClassSelector, StartPage_S7, Developer, StartPage_S5, StartPage_S3A, StartPage_S3B): # StartPage_S1A, StartPage_S1B, StartPage_S1AI):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ClassSelector)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def select_class(self,k):
        global bat
        bat = k
        if k == "S7 CSE":
            self.show_frame(StartPage_S7)
        elif k == "S5 CSE":
            self.show_frame(StartPage_S5)
        elif k == "S3 CSE A":
            self.show_frame(StartPage_S3A)
        elif k == "S3 CSE B":
            self.show_frame(StartPage_S3B)
        # elif k == "S1 CSE A":
            # self.show_frame(StartPage_S1A)
        # elif k == "S1 CSE B":
            # self.show_frame(StartPage_S1B)
        # elif k == "S1 AI & DS":
            # self.show_frame(StartPage_S1AI)
        else:
            messagebox.showinfo("Error", "Under Progress")

    def periodClassOpener(self, k):
        webbrowser.open_new(S7_CSE_links[k])
        time.sleep(1)
        self.window.destroy()

    def periodNowOpener(self):
        global bat
        t = time.ctime()
        l = t.split(" ")
        #    day = l[0]
        day = "Fri"
        k = days[day]
        #    now = l[4]
        now = "11:40:00"

        if day == "Sat" or day == "Sun":
            messagebox.showinfo("Error", "Classes NOT Available")
        elif day == "Fri":
            flag = 0
            for i in range(6):
                atl = get_keyFriday(i)
                ath = get_keyFriday(i + 1)
                if atl <= now < ath:
                    flag = 1

                    if bat == "S7 CSE":
                        classes = S7_CSE_tt[k][i]
                    elif bat == "S5 CSE":
                        classes = S5_CSE_tt[k][i]
                    elif bat == "S3 CSE A":
                        classes = S3_CSE_A_tt[k][i]
                    elif bat == "S3 CSE B":
                        classes = S3_CSE_B_tt[k][i]

                    if classes == "NULL":
                        messagebox.showinfo("Error", "Multiple Options available")
                    else:
                        webbrowser.open_new(S7_CSE_links[classes])
            if flag == 0:
                messagebox.showinfo("Error", "1Classes NOT Available/\n Multiple Options available")
        else:
            flag = 0
            for i in range(6):
                atl = get_key(i)
                ath = get_key(i + 1)
                if atl <= now < ath:
                    flag = 1

                    if bat == "S7 CSE":
                        classes = S7_CSE_tt[k][i]
                    elif bat == "S5 CSE":
                        classes = S5_CSE_tt[k][i]
                    elif bat == "S3 CSE A":
                        classes = S3_CSE_A_tt[k][i]
                    elif bat == "S7 CSE B":
                        classes = S3_CSE_B_tt[k][i]

                    if classes == "NULL":
                        messagebox.showinfo("Error", "Multiple Options available\nUse Dropdown")
                    else:
                        webbrowser.open_new(S7_CSE_links[classes])
            if flag == 0:
                messagebox.showinfo("Error", "Classes NOT Available/\n Multiple Options available")

    def destroy_frame(self):
        self.destroy()


class ClassSelector(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="CSE VJEC",
                          foreground="red",
                          font=("Times New Roman", 15))
        label1.pack(padx=50, pady=10)

        label2 = tk.Label(self, text="Time Table",
                          foreground="red",
                          font=("Times New Roman", 12))
        label2.pack(padx=50, pady=5)

        label3 = tk.Label(self, text="Select Your Batch :", font=("Times New Roman", 10))
        label3.pack(pady=5)

        batch = ttk.Combobox(self, width=20, values=
        ('S7 CSE', 'S5 CSE', 'S3 CSE A', 'S3 CSE B', 'S1 CSE A', 'S1 CSE B', 'S1 AI & DS'))

        batch.current()
        batch.pack(pady=5)

        button1 = tk.Button(self, text="Continue",
                            command=lambda: controller.select_class(batch.get()))
        button1.pack()

        button = tk.Button(self, text="Developers",
                           command=lambda: controller.show_frame(Developer))
        button.pack()

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack()


class Developer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="CSE VJEC",
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
                            command=lambda: controller.show_frame(ClassSelector))
        button1.pack(pady=5)

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack(pady=5)


class StartPage_S7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="S7 CSE",
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
        ('Ms. Divya K', 'Ms. Jeethu V Devasia', 'Ms. Akhila Mathew', 'Ms. Vidhya S S', 'Ms. Tintu Devasia', 'Ms. Asha Baby', 'Ms. Derroll David', 'Ms. Achala Prasad'))

        period.current()
        period.pack(pady=5)

        btn1 = tk.Button(self, text='Join Now', bd='5', command=lambda: controller.periodClassOpener(period.get()))
        btn1.pack(padx=10, pady=10)

        btn2 = tk.Button(self, text='Immediate Join', bd='5', command=lambda: controller.periodNowOpener())
        btn2.pack(padx=10, pady=10)

        button = tk.Button(self, text="Developers",
                           command=lambda: controller.show_frame(Developer))
        button.pack()

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack()


class StartPage_S5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="S5 CSE",
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

        period.current()
        period.pack(pady=5)

        btn1 = tk.Button(self, text='Join Now', bd='5', command=lambda: controller.periodClassOpener(period.get()))
        btn1.pack(padx=10, pady=10)

        btn2 = tk.Button(self, text='Immediate Join', bd='5', command=lambda: controller.periodNowOpener())
        btn2.pack(padx=10, pady=10)

        button = tk.Button(self, text="Developers",
                           command=lambda: controller.show_frame(Developer))
        button.pack()

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack()


class StartPage_S3A(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="S3 CSE A",
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
        ('Mr. Abdul Latheef', 'Ms. Neena V V', 'Ms. Anisha Joseph', 'Ms. Raiza Yusef', 'Sr. Jisha C T', 'Ms. Angel Varghese', 'Ms. Reema Mathew A', 'Ms. Tintu Devasia'))

        period.current()
        period.pack(pady=5)

        btn1 = tk.Button(self, text='Join Now', bd='5', command=lambda: controller.periodClassOpener(period.get()))
        btn1.pack(padx=10, pady=10)

        btn2 = tk.Button(self, text='Immediate Join', bd='5', command=lambda: controller.periodNowOpener())
        btn2.pack(padx=10, pady=10)

        button = tk.Button(self, text="Developers",
                           command=lambda: controller.show_frame(Developer))
        button.pack()

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack()


class StartPage_S3B(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="S3 CSE B",
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
        ("Ms. Divya B", "Ms. Vidhya S S", "Ms. Keerthijith P P", "Ms. Divya K Vinod", "Ms. Divya B", "Mr. Manoj V Thomas", "Ms. Shimna P K", "Ms. Angel Varghese", "Ms. Raiza Yousaf", "Ms. Asha Baby"))

        period.current()
        period.pack(pady=5)

        btn1 = tk.Button(self, text='Join Now', bd='5', command=lambda: controller.periodClassOpener(period.get()))
        btn1.pack(padx=10, pady=10)

        btn2 = tk.Button(self, text='Immediate Join', bd='5', command=lambda: controller.periodNowOpener())
        btn2.pack(padx=10, pady=10)

        button = tk.Button(self, text="Developers",
                           command=lambda: controller.show_frame(Developer))
        button.pack()

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy_frame())
        button2.pack()


app = TimeTableApp()
app.mainloop()
