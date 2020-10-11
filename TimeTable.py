import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import webbrowser

timeFontSize = 12
dayFontSize = 13
padinY = 5
padinX = 5
periodFontSize = 8

buttonList = []


def period_class_opener(k):
    if k == 'NULL':
        print("Error")
    else:
        webbrowser.open_new(S7_CSE_links[k])


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

S7_SubTeachers_Subjects = {
    "Ms. Jeethu": "ML",
    "NULL": "Lab/Seminar",
    "Ms. Vidhya": "Crypto",
    "Ms. Tintu": "PP",
    "Ms. Akhila": "DC",
    "Ms. Divya": "CSA",
    "Ms. Asha": "CG"
}


def get_keyFriday(val):
    for key, value in fritiming.items():
        if val == value:
            return key


def get_key(val):
    for key, value in alltiming.items():
        if val == value:
            return key


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
timeLabel1.grid(row=0, column=1, padx=padinX)

timeLabel2 = tk.Label(toolsFrame, text="09:20 - 10:00", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabel2.grid(row=0, column=2, padx=padinX)

timeLabel3 = tk.Label(toolsFrame, text="10:10 - 10:50", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabel3.grid(row=0, column=3, padx=padinX)

timeLabel4 = tk.Label(toolsFrame, text="11:00 - 11:40", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabel4.grid(row=0, column=4, padx=padinX)

timeLabel5 = tk.Label(toolsFrame, text="11:50 - 12:30", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabel5.grid(row=0, column=5, padx=padinX)

timeLabel6 = tk.Label(toolsFrame, text="12:40 - 01:20", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabel6.grid(row=0, column=6, padx=padinX)

dayLabel1 = tk.Label(toolsFrame, text="Mon", font=("arial", dayFontSize), background="LightSteelBlue2")
dayLabel1.grid(row=1, column=0, pady=padinY)

dayLabel2 = tk.Label(toolsFrame, text="Tue", font=("arial", dayFontSize), background="LightSteelBlue2")
dayLabel2.grid(row=2, column=0, pady=padinY)

dayLabel3 = tk.Label(toolsFrame, text="Wed", font=("arial", dayFontSize), background="LightSteelBlue2")
dayLabel3.grid(row=3, column=0, pady=padinY)

dayLabel4 = tk.Label(toolsFrame, text="Thu", font=("arial", dayFontSize), background="LightSteelBlue2")
dayLabel4.grid(row=4, column=0, pady=padinY)

# MONDAY
butM1 = tk.Button(toolsFrame, text=S7_CSE_tt[0][0], font=("arial", periodFontSize), command=lambda: period_class_opener
(butM1.cget('text').split("\n")[0]))
butM1.grid(row=1, column=1, padx=padinX, sticky="nsew")

butM2 = tk.Button(toolsFrame, text=S7_CSE_tt[0][1], font=("arial", periodFontSize), command=lambda: period_class_opener
(butM2.cget('text').split("\n")[0]))
butM2.grid(row=1, column=2, padx=padinX, sticky="nsew")

butM3 = tk.Button(toolsFrame, text=S7_CSE_tt[0][2], font=("arial", periodFontSize), command=lambda: period_class_opener
(butM3.cget('text').split("\n")[0]))
butM3.grid(row=1, column=3, padx=padinX, sticky="nsew")

butM4 = tk.Button(toolsFrame, text=S7_CSE_tt[0][3], font=("arial", periodFontSize), command=lambda: period_class_opener
(butM4.cget('text').split("\n")[0]))
butM4.grid(row=1, column=4, padx=padinX, sticky="nsew")

butM5 = tk.Button(toolsFrame, text=S7_CSE_tt[0][4], font=("arial", periodFontSize), command=lambda: period_class_opener
(butM5.cget('text').split("\n")[0]))
butM5.grid(row=1, column=5, padx=padinX, sticky="nsew")

butM6 = tk.Button(toolsFrame, text=S7_CSE_tt[0][5], font=("arial", periodFontSize), command=lambda: period_class_opener
(butM6.cget('text').split("\n")[0]))
butM6.grid(row=1, column=6, padx=padinX, sticky="nsew")

buttonList.append(butM1)
buttonList.append(butM2)
buttonList.append(butM3)
buttonList.append(butM4)
buttonList.append(butM5)
buttonList.append(butM6)

# TUESDAY
butTu1 = tk.Button(toolsFrame, text=S7_CSE_tt[1][0], font=("arial", periodFontSize), command=lambda: period_class_opener
(butTu1.cget('text').split("\n")[0]))
butTu1.grid(row=2, column=1, columnspan=3, padx=padinX, sticky="nsew")

butTu2 = tk.Button(toolsFrame, text=S7_CSE_tt[1][3], font=("arial", periodFontSize), command=lambda: period_class_opener
(butTu2.cget('text').split("\n")[0]))
butTu2.grid(row=2, column=4, padx=padinX, sticky="nsew")

butTu3 = tk.Button(toolsFrame, text=S7_CSE_tt[1][4], font=("arial", periodFontSize), command=lambda: period_class_opener
(butTu3.cget('text').split("\n")[0]))
butTu3.grid(row=2, column=5, padx=padinX, sticky="nsew")

butTu4 = tk.Button(toolsFrame, text=S7_CSE_tt[1][5], font=("arial", periodFontSize), command=lambda: period_class_opener
(butTu4.cget('text').split("\n")[0]))
butTu4.grid(row=2, column=6, padx=padinX, sticky="nsew")

buttonList.append(butTu1)
buttonList.append(butTu2)
buttonList.append(butTu3)
buttonList.append(butTu4)

# WEDNESDAY
butW1 = tk.Button(toolsFrame, text=S7_CSE_tt[2][0], font=("arial", periodFontSize), command=lambda: period_class_opener
(butW1.cget('text').split("\n")[0]))
butW1.grid(row=3, column=1, padx=padinX, sticky="nsew")

butW2 = tk.Button(toolsFrame, text=S7_CSE_tt[2][1], font=("arial", periodFontSize), command=lambda: period_class_opener
(butW2.cget('text').split("\n")[0]))
butW2.grid(row=3, column=2, padx=padinX, sticky="nsew")

butW3 = tk.Button(toolsFrame, text=S7_CSE_tt[2][2], font=("arial", periodFontSize), command=lambda: period_class_opener
(butW3.cget('text').split("\n")[0]))
butW3.grid(row=3, column=3, padx=padinX, sticky="nsew")

butW4 = tk.Button(toolsFrame, text=S7_CSE_tt[2][3], font=("arial", periodFontSize), command=lambda: period_class_opener
(butW4.cget('text').split("\n")[0]))
butW4.grid(row=3, column=4, padx=padinX, sticky="nsew")

butW5 = tk.Button(toolsFrame, text=S7_CSE_tt[2][4], font=("arial", periodFontSize), command=lambda: period_class_opener
(butW5.cget('text').split("\n")[0]))
butW5.grid(row=3, column=5, padx=padinX, sticky="nsew")

butW6 = tk.Button(toolsFrame, text=S7_CSE_tt[2][5], font=("arial", periodFontSize), command=lambda: period_class_opener
(butW6.cget('text').split("\n")[0]))
butW6.grid(row=3, column=6, padx=padinX, sticky="nsew")

buttonList.append(butW1)
buttonList.append(butW2)
buttonList.append(butW3)
buttonList.append(butW4)
buttonList.append(butW5)
buttonList.append(butW6)

# THURSDAY
butTh1 = tk.Button(toolsFrame, text=S7_CSE_tt[3][0], font=("arial", periodFontSize), command=lambda: period_class_opener
(butTh1.cget('text').split("\n")[0]))
butTh1.grid(row=4, column=1, padx=padinX, sticky="nsew")

butTh2 = tk.Button(toolsFrame, text=S7_CSE_tt[3][1], font=("arial", periodFontSize), command=lambda: period_class_opener
(butTh2.cget('text').split("\n")[0]))
butTh2.grid(row=4, column=2, padx=padinX, sticky="nsew")

butTh3 = tk.Button(toolsFrame, text=S7_CSE_tt[3][2], font=("arial", periodFontSize), command=lambda: period_class_opener
(butTh3.cget('text').split("\n")[0]))
butTh3.grid(row=4, column=3, padx=padinX, sticky="nsew")

butTh4 = tk.Button(toolsFrame, text=S7_CSE_tt[3][3], font=("arial", periodFontSize), command=lambda: period_class_opener
(butTh4.cget('text').split("\n")[0]))
butTh4.grid(row=4, column=4, columnspan=3, padx=padinX, sticky="nsew")

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

timeLabelF1 = tk.Label(toolsFrame1, text="08:00 - 08:35", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabelF1.grid(row=0, column=1, padx=padinX)

timeLabelF2 = tk.Label(toolsFrame1, text="08:45 - 09:20", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabelF2.grid(row=0, column=2, padx=padinX)

timeLabelF3 = tk.Label(toolsFrame1, text="09:30 - 10:05", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabelF3.grid(row=0, column=3, padx=padinX)

timeLabelF4 = tk.Label(toolsFrame1, text="10:15 - 10:50", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabelF4.grid(row=0, column=4, padx=padinX)

timeLabelF5 = tk.Label(toolsFrame1, text="11:00 - 11:35", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabelF5.grid(row=0, column=5, padx=padinX)

timeLabelF6 = tk.Label(toolsFrame1, text="11:45 - 12:20", font=("arial", timeFontSize), background="LightSteelBlue2")
timeLabelF6.grid(row=0, column=6, padx=padinX)

dayLabel4 = tk.Label(toolsFrame1, text="Fri", font=("arial", dayFontSize), background="LightSteelBlue2")
dayLabel4.grid(row=1, column=0, pady=padinY)

butF1 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][0], font=("arial", periodFontSize), command=lambda: period_class_opener
(butF1.cget('text').split("\n")[0]))
butF1.grid(row=1, column=1, padx=padinX, sticky="nsew")

butF2 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][1], font=("arial", periodFontSize), command=lambda: period_class_opener
(butF2.cget('text').split("\n")[0]))
butF2.grid(row=1, column=2, padx=padinX, sticky="nsew")

butF3 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][2], font=("arial", periodFontSize), command=lambda: period_class_opener
(butF3.cget('text').split("\n")[0]))
butF3.grid(row=1, column=3, padx=padinX, sticky="nsew")

butF4 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][3], font=("arial", periodFontSize), command=lambda: period_class_opener
(butF4.cget('text').split("\n")[0]))
butF4.grid(row=1, column=4, padx=padinX, sticky="nsew")

butF5 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][4], font=("arial", periodFontSize), command=lambda: period_class_opener
(butF5.cget('text').split("\n")[0]))
butF5.grid(row=1, column=5, padx=padinX, sticky="nsew")

butF6 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][5], font=("arial", periodFontSize), command=lambda: period_class_opener
(butF6.cget('text').split("\n")[0]))
butF6.grid(row=1, column=6, padx=padinX, sticky="nsew")

buttonList.append(butF1)
buttonList.append(butF2)
buttonList.append(butF3)
buttonList.append(butF4)
buttonList.append(butF5)
buttonList.append(butF6)

# end of friday


# Subject name allocation
for i in buttonList:
    textTemp = i.cget('text') + "\n" + "[" + S7_SubTeachers_Subjects.get(i.cget('text')) + "]"
    i['text'] = textTemp

root.mainloop()
