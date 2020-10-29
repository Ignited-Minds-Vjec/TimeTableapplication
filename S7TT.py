import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import webbrowser

frameBackgroundColour = "snow3"
labelBackgroundColour = "snow3"

days = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4
}

allTiming = {
    "08:25:00": 0,
    "09:15:00": 1,
    "10:05:00": 2,
    "10:55:00": 3,
    "11:45:00": 4,
    "12:35:00": 5,
    "13:25:00": 6
}

friTiming = {
    "07:55:00": 0,
    "08:40:00": 1,
    "09:25:00": 2,
    "10:10:00": 3,
    "10:55:00": 4,
    "11:40:00": 5,
    "12:25:00": 6
}

S7_CSE_links = {
    "Ms. Divya [CSA]": "https://meet.google.com/gxw-tjzh-tzm",
    "Ms. Jeethu [ML]": "https://meet.google.com/tgu-syum-kkn",
    "Ms. Akhila [DC]": "https://meet.google.com/byh-xpvu-its",
    "Ms. Vidhya [Crypto]": "https://meet.google.com/oop-kqsp-zxu",
    "Ms. Tintu [PP]": "https://meet.google.com/mon-xjru-cat",
    "Ms. Asha [CG]": "https://meet.google.com/uyz-sogj-dvo",
    "Ms. Derroll [Lab]": "https://meet.google.com/zbc-oryd-uhx",
    "Ms. Achala [Seminar]": "https://meet.google.com/kyu-wguq-psi"
}

S7_CSE_tt = [
    ["Ms. Jeethu [ML]", "Ms. Vidhya [Crypto]", "Ms. Asha [CG]", "Ms. Tintu [PP]", "Ms. Akhila [DC]", "Ms. Divya [CSA]"],
    ["Ms. Achala/Ms. Derroll [Seminar/Lab]", "Ms. Achala/Ms. Derroll [Seminar/Lab]",
     "Ms. Achala/Ms. Derroll [Seminar/Lab]", "Ms. Divya [CSA]", "Ms. Asha [CG]", "Ms. Akhila [DC]"],
    ["Ms. Jeethu [ML]", "Ms. Asha [CG]", "Ms. Divya [CSA]", "Ms. Tintu [PP]", "Ms. Akhila [DC]", "Ms. Tintu [PP]"],
    ["Ms. Jeethu [ML]", "Ms. Tintu [PP]", "Ms. Divya [CSA]", "Ms. Achala/Ms. Derroll [Seminar/Lab]",
     "Ms. Achala/Ms. Derroll [Seminar/Lab]", "Ms. Achala/Ms. Derroll [Seminar/Lab]"],
    ["Ms. Achala/Ms. Derroll [Seminar/Lab]", "Ms. Vidhya [Crypto]", "Ms. Jeethu [ML]", "Ms. Asha [CG]",
     "Ms. Akhila [DC]", "Ms. Vidhya [Crypto]"]
]

S7_SubTeachers_Subjects = {
    "Ms. Jeethu [ML]": "ML",
    "Ms. Achala/Ms. Derroll": "Lab/Seminar",
    "Ms. Vidhya [Crypto]": "Crypto",
    "Ms. Tintu [PP]": "PP",
    "Ms. Akhila [DC]": "DC",
    "Ms. Divya [CSA]": "CSA",
    "Ms. Asha [CG]": "CG"
}


def joining_class(msg):
    joining_info = tk.Tk()
    joining_info.geometry("300x75")
    joining_info.resizable(False, False)
    joining_info.title("Joining Info")
    label = tk.Label(joining_info, text="Joining: "+msg, font=("arial", 13, "bold"))
    label.pack(padx=20, pady=20)
    joining_info.after(2000, joining_info.destroy)
    joining_info.mainloop()


def get_keyFriday(val):
    for key, value in friTiming.items():
        if val == value:
            return key


def get_key(val):
    for key, value in allTiming.items():
        if val == value:
            return key


def lab_seminar_selection(name, root1, root2):
    webbrowser.open_new(S7_CSE_links[name])
    root1.destroy()
    joining_class(name)
    if root2 is not None:
        root2.destroy()


def period_class(k, root=None):
    if k.split()[1] == 'Achala/Ms.':
        print(k.split()[1])
        # tk.messagebox.showinfo("Not Available", "Choose options from Main Menu")
        msgBox = tk.Tk()
        msgBox.geometry("300x80")
        msgBox.resizable(False, False)
        msgBox.configure(background="LightSteelBlue3")
        label = tk.Label(msgBox, text="Choose the class", font=("arial", 13), background="LightSteelBlue3")
        label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=80)
        label.grid_columnconfigure(2)

        button1 = tk.Button(msgBox, text="Seminar",
                            command=lambda: lab_seminar_selection("Ms. Achala [Seminar]", msgBox, root))
        button1.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        button2 = tk.Button(msgBox, text="Lab",
                            command=lambda: lab_seminar_selection("Ms. Derroll [Lab]", msgBox, root))
        button2.grid(row=1, column=1, sticky="nsew", padx=20, pady=10)
        msgBox.mainloop()
    else:
        teacherName = k.split()[0] + " " + k.split()[1] + " " + k.split()[2]
        webbrowser.open_new(S7_CSE_links[teacherName])
        joining_class(teacherName)


def show_timtable():
    timeFontSize = 12
    dayFontSize = 13
    periodFontSize = 8

    buttonList = []

    root = tk.Tk()
    root.geometry("700x350")
    root.title("Time Table")
    root.configure(background="LightSteelBlue3")
    root.grid_columnconfigure(0, weight=1)
    root.resizable(False, False)

    toolsFrame = tk.Frame(root)
    toolsFrame.configure(background="LightSteelBlue2")
    toolsFrame.grid(row=1, column=0, sticky="ew", pady=20)
    toolsFrame.grid_columnconfigure(1, weight=6)

    deptLabel = tk.Label(root, text="S7 CSE", font=("arial", 19, "bold"))
    deptLabel.configure(background="LightSteelBlue3")
    deptLabel.grid(row=0, column=0)

    timeLabel0 = tk.Label(toolsFrame, text="      ", font=("arial", 15), background="LightSteelBlue2")
    timeLabel0.grid(row=0, column=0)

    timeLabel1 = tk.Label(toolsFrame, text="08:30 - 09:10", font=("arial", timeFontSize), background="LightSteelBlue2")
    timeLabel1.grid(row=0, column=1, padx=5)

    timeLabel2 = tk.Label(toolsFrame, text="09:20 - 10:00", font=("arial", timeFontSize), background="LightSteelBlue2")
    timeLabel2.grid(row=0, column=2, padx=5)

    timeLabel3 = tk.Label(toolsFrame, text="10:10 - 10:50", font=("arial", timeFontSize), background="LightSteelBlue2")
    timeLabel3.grid(row=0, column=3, padx=5)

    timeLabel4 = tk.Label(toolsFrame, text="11:00 - 11:40", font=("arial", timeFontSize), background="LightSteelBlue2")
    timeLabel4.grid(row=0, column=4, padx=5)

    timeLabel5 = tk.Label(toolsFrame, text="11:50 - 12:30", font=("arial", timeFontSize), background="LightSteelBlue2")
    timeLabel5.grid(row=0, column=5, padx=5)

    timeLabel6 = tk.Label(toolsFrame, text="12:40 - 01:20", font=("arial", timeFontSize), background="LightSteelBlue2")
    timeLabel6.grid(row=0, column=6, padx=5)

    dayLabel1 = tk.Label(toolsFrame, text="Mon", font=("arial", dayFontSize), background="LightSteelBlue2")
    dayLabel1.grid(row=1, column=0, pady=5)

    dayLabel2 = tk.Label(toolsFrame, text="Tue", font=("arial", dayFontSize), background="LightSteelBlue2")
    dayLabel2.grid(row=2, column=0, pady=5)

    dayLabel3 = tk.Label(toolsFrame, text="Wed", font=("arial", dayFontSize), background="LightSteelBlue2")
    dayLabel3.grid(row=3, column=0, pady=5)

    dayLabel4 = tk.Label(toolsFrame, text="Thu", font=("arial", dayFontSize), background="LightSteelBlue2")
    dayLabel4.grid(row=4, column=0, pady=5)

    # MONDAY
    butM1 = tk.Button(toolsFrame, text=S7_CSE_tt[0][0], font=("arial", periodFontSize),
                      command=lambda: period_class(butM1.cget('text'), root))
    butM1.grid(row=1, column=1, padx=5, sticky="nsew")

    butM2 = tk.Button(toolsFrame, text=S7_CSE_tt[0][1], font=("arial", periodFontSize),
                      command=lambda: period_class(butM2.cget('text'), root))
    butM2.grid(row=1, column=2, padx=5, sticky="nsew")

    butM3 = tk.Button(toolsFrame, text=S7_CSE_tt[0][2], font=("arial", periodFontSize),
                      command=lambda: period_class(butM3.cget('text'), root))
    butM3.grid(row=1, column=3, padx=5, sticky="nsew")

    butM4 = tk.Button(toolsFrame, text=S7_CSE_tt[0][3], font=("arial", periodFontSize),
                      command=lambda: period_class(butM4.cget('text'), root))
    butM4.grid(row=1, column=4, padx=5, sticky="nsew")

    butM5 = tk.Button(toolsFrame, text=S7_CSE_tt[0][4], font=("arial", periodFontSize),
                      command=lambda: period_class(butM5.cget('text'), root))
    butM5.grid(row=1, column=5, padx=5, sticky="nsew")

    butM6 = tk.Button(toolsFrame, text=S7_CSE_tt[0][5], font=("arial", periodFontSize),
                      command=lambda: period_class(butM6.cget('text'), root))
    butM6.grid(row=1, column=6, padx=5, sticky="nsew")

    buttonList.append(butM1)
    buttonList.append(butM2)
    buttonList.append(butM3)
    buttonList.append(butM4)
    buttonList.append(butM5)
    buttonList.append(butM6)

    # TUESDAY
    butTu1 = tk.Button(toolsFrame, text=S7_CSE_tt[1][0], font=("arial", periodFontSize),
                       command=lambda: period_class(butTu1.cget('text'), root))
    butTu1.grid(row=2, column=1, columnspan=3, padx=5, sticky="nsew")

    butTu2 = tk.Button(toolsFrame, text=S7_CSE_tt[1][3], font=("arial", periodFontSize),
                       command=lambda: period_class(butTu2.cget('text'), root))
    butTu2.grid(row=2, column=4, padx=5, sticky="nsew")

    butTu3 = tk.Button(toolsFrame, text=S7_CSE_tt[1][4], font=("arial", periodFontSize),
                       command=lambda: period_class(butTu3.cget('text'), root))
    butTu3.grid(row=2, column=5, padx=5, sticky="nsew")

    butTu4 = tk.Button(toolsFrame, text=S7_CSE_tt[1][5], font=("arial", periodFontSize),
                       command=lambda: period_class(butTu4.cget('text'), root))
    butTu4.grid(row=2, column=6, padx=5, sticky="nsew")

    buttonList.append(butTu1)
    buttonList.append(butTu2)
    buttonList.append(butTu3)
    buttonList.append(butTu4)

    # WEDNESDAY
    butW1 = tk.Button(toolsFrame, text=S7_CSE_tt[2][0], font=("arial", periodFontSize),
                      command=lambda: period_class(butW1.cget('text'), root))
    butW1.grid(row=3, column=1, padx=5, sticky="nsew")

    butW2 = tk.Button(toolsFrame, text=S7_CSE_tt[2][1], font=("arial", periodFontSize),
                      command=lambda: period_class(butW2.cget('text'), root))
    butW2.grid(row=3, column=2, padx=5, sticky="nsew")

    butW3 = tk.Button(toolsFrame, text=S7_CSE_tt[2][2], font=("arial", periodFontSize),
                      command=lambda: period_class(butW3.cget('text'), root))
    butW3.grid(row=3, column=3, padx=5, sticky="nsew")

    butW4 = tk.Button(toolsFrame, text=S7_CSE_tt[2][3], font=("arial", periodFontSize),
                      command=lambda: period_class(butW4.cget('text'), root))
    butW4.grid(row=3, column=4, padx=5, sticky="nsew")

    butW5 = tk.Button(toolsFrame, text=S7_CSE_tt[2][4], font=("arial", periodFontSize),
                      command=lambda: period_class(butW5.cget('text'), root))
    butW5.grid(row=3, column=5, padx=5, sticky="nsew")

    butW6 = tk.Button(toolsFrame, text=S7_CSE_tt[2][5], font=("arial", periodFontSize),
                      command=lambda: period_class(butW6.cget('text'), root))
    butW6.grid(row=3, column=6, padx=5, sticky="nsew")

    buttonList.append(butW1)
    buttonList.append(butW2)
    buttonList.append(butW3)
    buttonList.append(butW4)
    buttonList.append(butW5)
    buttonList.append(butW6)

    # THURSDAY
    butTh1 = tk.Button(toolsFrame, text=S7_CSE_tt[3][0], font=("arial", periodFontSize),
                       command=lambda: period_class(butTh1.cget('text'), root))
    butTh1.grid(row=4, column=1, padx=5, sticky="nsew")

    butTh2 = tk.Button(toolsFrame, text=S7_CSE_tt[3][1], font=("arial", periodFontSize),
                       command=lambda: period_class(butTh2.cget('text'), root))
    butTh2.grid(row=4, column=2, padx=5, sticky="nsew")

    butTh3 = tk.Button(toolsFrame, text=S7_CSE_tt[3][2], font=("arial", periodFontSize),
                       command=lambda: period_class(butTh3.cget('text'), root))
    butTh3.grid(row=4, column=3, padx=5, sticky="nsew")

    butTh4 = tk.Button(toolsFrame, text=S7_CSE_tt[3][3], font=("arial", periodFontSize),
                       command=lambda: period_class(butTh4.cget('text'), root))
    butTh4.grid(row=4, column=4, columnspan=3, padx=5, sticky="nsew")

    buttonList.append(butTh1)
    buttonList.append(butTh2)
    buttonList.append(butTh3)
    buttonList.append(butTh4)

    # Friday
    toolsFrame1 = tk.Frame(root)
    toolsFrame1.configure(background="LightSteelBlue2")
    toolsFrame1.grid(row=2, column=0, sticky="ew", pady=10)
    toolsFrame1.grid_columnconfigure(1, weight=6)

    timeLabelF0 = tk.Label(toolsFrame1, text="      ", font=("arial", 15), background="LightSteelBlue2")
    timeLabelF0.grid(row=0, column=0)

    timeLabelF1 = tk.Label(toolsFrame1, text="08:00 - 08:35", font=("arial", timeFontSize),
                           background="LightSteelBlue2")
    timeLabelF1.grid(row=0, column=1, padx=5)

    timeLabelF2 = tk.Label(toolsFrame1, text="08:45 - 09:20", font=("arial", timeFontSize),
                           background="LightSteelBlue2")
    timeLabelF2.grid(row=0, column=2, padx=5)

    timeLabelF3 = tk.Label(toolsFrame1, text="09:30 - 10:05", font=("arial", timeFontSize),
                           background="LightSteelBlue2")
    timeLabelF3.grid(row=0, column=3, padx=5)

    timeLabelF4 = tk.Label(toolsFrame1, text="10:15 - 10:50", font=("arial", timeFontSize),
                           background="LightSteelBlue2")
    timeLabelF4.grid(row=0, column=4, padx=5)

    timeLabelF5 = tk.Label(toolsFrame1, text="11:00 - 11:35", font=("arial", timeFontSize),
                           background="LightSteelBlue2")
    timeLabelF5.grid(row=0, column=5, padx=5)

    timeLabelF6 = tk.Label(toolsFrame1, text="11:45 - 12:20", font=("arial", timeFontSize),
                           background="LightSteelBlue2")
    timeLabelF6.grid(row=0, column=6, padx=5)

    dayLabel4 = tk.Label(toolsFrame1, text="Fri", font=("arial", dayFontSize), background="LightSteelBlue2")
    dayLabel4.grid(row=1, column=0, pady=5)

    butF1 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][0], font=("arial", periodFontSize),
                      command=lambda: period_class(butF1.cget('text'), root))
    butF1.grid(row=1, column=1, padx=5, sticky="nsew")

    butF2 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][1], font=("arial", periodFontSize),
                      command=lambda: period_class(butF2.cget('text'), root))
    butF2.grid(row=1, column=2, padx=5, sticky="nsew")

    butF3 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][2], font=("arial", periodFontSize),
                      command=lambda: period_class(butF3.cget('text'), root))
    butF3.grid(row=1, column=3, padx=5, sticky="nsew")

    butF4 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][3], font=("arial", periodFontSize),
                      command=lambda: period_class(butF4.cget('text'), root))
    butF4.grid(row=1, column=4, padx=5, sticky="nsew")

    butF5 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][4], font=("arial", periodFontSize),
                      command=lambda: period_class(butF5.cget('text'), root))
    butF5.grid(row=1, column=5, padx=5, sticky="nsew")

    butF6 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][5], font=("arial", periodFontSize),
                      command=lambda: period_class(butF6.cget('text'), root))
    butF6.grid(row=1, column=6, padx=5, sticky="nsew")

    buttonList.append(butF1)
    buttonList.append(butF2)
    buttonList.append(butF3)
    buttonList.append(butF4)
    buttonList.append(butF5)
    buttonList.append(butF6)

    # end of friday

    # Subject name allocation
    for i in buttonList:
        # print(i.cget('text'))
        temp = i.cget('text').split()
        if temp[1] + "" == "Achala/Ms.":
            textTemp = temp[0] + " " + temp[1] + " " + temp[2]  # temp[2] holds derroll
            textTemp = textTemp + '\n' + "[" + S7_SubTeachers_Subjects.get(textTemp) + "]"
        else:
            textTemp = temp[0] + " " + temp[1]
            textTemp = textTemp + '\n' + "[" + S7_SubTeachers_Subjects.get(textTemp + " " + temp[2]) + "]"
        i['text'] = textTemp

    root.mainloop()


class TimeTableApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        self.frames = {}

        for F in (StartPage, Developer):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    '''
    @staticmethod
    def periodClassOpener(k):
        webbrowser.open_new(S7_CSE_links[k])
        messagebox.showinfo("Class", "Joining: "+k)
    '''
    @staticmethod
    def periodNowOpener():
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
                    period_class(classes)
            if flag == 0:
                messagebox.showinfo("Error", "Classes NOT Available")
        else:
            flag = 0
            for i in range(6):
                atl = get_key(i)
                ath = get_key(i + 1)
                if atl <= now < ath:
                    flag = 1
                    classes = S7_CSE_tt[k][i]
                    period_class(classes)
            if flag == 0:
                messagebox.showinfo("Error", "Classes NOT Available")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, background=frameBackgroundColour)
        label1 = tk.Label(self, text="S7 CSE VJEC",
                          foreground="red",
                          font=("Times New Roman", 15),
                          background=labelBackgroundColour)
        label1.grid(row=0, column=0, pady=10, columnspan=3)

        label2 = tk.Label(self, text="Time Table",
                          foreground="red",
                          font=("Times New Roman", 12),
                          background=labelBackgroundColour)
        label2.grid(row=1, column=0, pady=5, columnspan=3)

        label3 = tk.Label(self, text="Select Your Period :",
                          font=("Times New Roman", 11),
                          background=labelBackgroundColour)
        label3.grid(row=2, column=0, columnspan=3, pady=5)

        # Combobox creation
        period = ttk.Combobox(self, width=19,
                              state="readonly",
                              values=
                              ('Ms. Divya [CSA]', 'Ms. Jeethu [ML]', 'Ms. Akhila [DC]', 'Ms. Vidhya [Crypto]',
                               'Ms. Tintu [PP]',
                               'Ms. Asha [CG]', 'Ms. Derroll [Lab]', 'Ms. Achala [Seminar]'))

        period.current(0)
        period.grid(row=3, column=0, pady=5, columnspan=2, padx=9)

        btn1 = tk.Button(self, text='Join Now',
                         command=lambda: period_class(period.get()))
        btn1.grid(row=3, column=2, pady=5)

        btn2 = tk.Button(self, text='Immediate Join',
                         bd='3',
                         command=lambda: controller.periodNowOpener())
        btn2.grid(row=4, column=0, pady=7, columnspan=3, sticky="nsew", padx=20)

        button3 = tk.Button(self, text="TimeTable",
                            command=show_timtable)
        button3.grid(row=5, column=0, pady=7, columnspan=3)

        button = tk.Button(self, text="Developers",
                           command=lambda: controller.show_frame(Developer))
        button.grid(row=6, column=0, pady=7, columnspan=3)


class Developer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, background=frameBackgroundColour)
        label1 = tk.Label(self, text="S7 CSE VJEC",
                          foreground="red",
                          font=("Times New Roman", 15),
                          background=labelBackgroundColour)
        label1.pack(padx=50, pady=10)

        label2 = tk.Label(self, text="Time Table App\nDevelopers",
                          foreground="red",
                          font=("Times New Roman", 13),
                          background=labelBackgroundColour)
        label2.pack()

        label3 = tk.Label(self, text="Adila Farha P K\nNathasha K V\n(S3 CSE B)\nArchana A\nAromal Joseph K M\nAgin "
                                     "Chandran\n(S7CSE)",
                          foreground="green",
                          font=("Times New Roman", 10),
                          background=labelBackgroundColour)
        label3.pack()

        label4 = tk.Label(self, text="Special Thanks to:\nTeam Ignited Minds",
                          foreground="red",
                          font=("Times New Roman", 10),
                          background=labelBackgroundColour)
        label4.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=5)


app = TimeTableApp()
app.mainloop()
