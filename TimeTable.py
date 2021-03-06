import tkinter as tk
import webbrowser

timeFontSize = 12
dayFontSize = 13
padinY = 5
padinX = 5
periodFontSize = 8

buttonList = []


def period_class_opener(k):
    if k.split()[1] == 'Achala/Ms.':
        msgBox = tk.Tk()
        msgBox.geometry("300x80")
        msgBox.resizable(False, False)
        msgBox.configure(background="LightSteelBlue3")
        label = tk.Label(msgBox, text="Choose the class", font=("arial", 13), background="LightSteelBlue3")
        label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=80)
        label.grid_columnconfigure(2)

        button1 = tk.Button(msgBox, text="Seminar",
                            command=lambda: lab_seminar_selection("Ms. Achala [Seminar]", msgBox))
        button1.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        button2 = tk.Button(msgBox, text="Lab",
                            command=lambda: lab_seminar_selection("Ms. Derroll [Lab]", msgBox))
        button2.grid(row=1, column=1, sticky="nsew", padx=20, pady=10)
        msgBox.mainloop()
    else:
        teacherName = k.split()[0] + " " + k.split()[1] + " " + k.split()[2]
        webbrowser.open_new(S7_CSE_links[teacherName])


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
    ["Ms. Achala/Ms. Derroll [Seminar/Lab]", "Ms. Achala/Ms. Derroll  [Seminar/Lab]",
     "Ms. Achala/Ms. Derroll  [Seminar/Lab]", "Ms. Divya [CSA]", "Ms. Asha [CG]", "Ms. Akhila [DC]"],
    ["Ms. Jeethu [ML]", "Ms. Asha [CG]", "Ms. Divya [CSA]", "Ms. Tintu [PP]", "Ms. Akhila [DC]", "Ms. Tintu [PP]"],
    ["Ms. Jeethu [ML]", "Ms. Tintu [PP]", "Ms. Divya [CSA]", "Ms. Achala/Ms. Derroll  [Seminar/Lab]",
     "Ms. Achala/Ms. Derroll  [Seminar/Lab]", "Ms. Achala/Ms. Derroll  [Seminar/Lab]"],
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


def lab_seminar_selection(name, root1):
    webbrowser.open_new(S7_CSE_links[name])
    root1.destroy()


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
                  command=lambda: period_class_opener(butM1.cget('text')))
butM1.grid(row=1, column=1, padx=5, sticky="nsew")

butM2 = tk.Button(toolsFrame, text=S7_CSE_tt[0][1], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butM2.cget('text')))
butM2.grid(row=1, column=2, padx=5, sticky="nsew")

butM3 = tk.Button(toolsFrame, text=S7_CSE_tt[0][2], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butM3.cget('text')))
butM3.grid(row=1, column=3, padx=5, sticky="nsew")

butM4 = tk.Button(toolsFrame, text=S7_CSE_tt[0][3], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butM4.cget('text')))
butM4.grid(row=1, column=4, padx=5, sticky="nsew")

butM5 = tk.Button(toolsFrame, text=S7_CSE_tt[0][4], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butM5.cget('text')))
butM5.grid(row=1, column=5, padx=5, sticky="nsew")

butM6 = tk.Button(toolsFrame, text=S7_CSE_tt[0][5], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butM6.cget('text')))
butM6.grid(row=1, column=6, padx=5, sticky="nsew")

buttonList.append(butM1)
buttonList.append(butM2)
buttonList.append(butM3)
buttonList.append(butM4)
buttonList.append(butM5)
buttonList.append(butM6)

# TUESDAY
butTu1 = tk.Button(toolsFrame, text=S7_CSE_tt[1][0], font=("arial", periodFontSize),
                   command=lambda: period_class_opener(butTu1.cget('text')))
butTu1.grid(row=2, column=1, columnspan=3, padx=5, sticky="nsew")

butTu2 = tk.Button(toolsFrame, text=S7_CSE_tt[1][3], font=("arial", periodFontSize),
                   command=lambda: period_class_opener(butTu2.cget('text')))
butTu2.grid(row=2, column=4, padx=5, sticky="nsew")

butTu3 = tk.Button(toolsFrame, text=S7_CSE_tt[1][4], font=("arial", periodFontSize),
                   command=lambda: period_class_opener(butTu3.cget('text')))
butTu3.grid(row=2, column=5, padx=5, sticky="nsew")

butTu4 = tk.Button(toolsFrame, text=S7_CSE_tt[1][5], font=("arial", periodFontSize),
                   command=lambda: period_class_opener(butTu4.cget('text')))
butTu4.grid(row=2, column=6, padx=5, sticky="nsew")

buttonList.append(butTu1)
buttonList.append(butTu2)
buttonList.append(butTu3)
buttonList.append(butTu4)

# WEDNESDAY
butW1 = tk.Button(toolsFrame, text=S7_CSE_tt[2][0], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butW1.cget('text')))
butW1.grid(row=3, column=1, padx=5, sticky="nsew")

butW2 = tk.Button(toolsFrame, text=S7_CSE_tt[2][1], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butW2.cget('text')))
butW2.grid(row=3, column=2, padx=5, sticky="nsew")

butW3 = tk.Button(toolsFrame, text=S7_CSE_tt[2][2], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butW3.cget('text')))
butW3.grid(row=3, column=3, padx=5, sticky="nsew")

butW4 = tk.Button(toolsFrame, text=S7_CSE_tt[2][3], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butW4.cget('text')))
butW4.grid(row=3, column=4, padx=5, sticky="nsew")

butW5 = tk.Button(toolsFrame, text=S7_CSE_tt[2][4], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butW5.cget('text')))
butW5.grid(row=3, column=5, padx=5, sticky="nsew")

butW6 = tk.Button(toolsFrame, text=S7_CSE_tt[2][5], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butW6.cget('text')))
butW6.grid(row=3, column=6, padx=5, sticky="nsew")

buttonList.append(butW1)
buttonList.append(butW2)
buttonList.append(butW3)
buttonList.append(butW4)
buttonList.append(butW5)
buttonList.append(butW6)

# THURSDAY
butTh1 = tk.Button(toolsFrame, text=S7_CSE_tt[3][0], font=("arial", periodFontSize),
                   command=lambda: period_class_opener(butTh1.cget('text')))
butTh1.grid(row=4, column=1, padx=5, sticky="nsew")

butTh2 = tk.Button(toolsFrame, text=S7_CSE_tt[3][1], font=("arial", periodFontSize),
                   command=lambda: period_class_opener(butTh2.cget('text')))
butTh2.grid(row=4, column=2, padx=5, sticky="nsew")

butTh3 = tk.Button(toolsFrame, text=S7_CSE_tt[3][2], font=("arial", periodFontSize),
                   command=lambda: period_class_opener(butTh3.cget('text')))
butTh3.grid(row=4, column=3, padx=5, sticky="nsew")

butTh4 = tk.Button(toolsFrame, text=S7_CSE_tt[3][3], font=("arial", periodFontSize),
                   command=lambda: period_class_opener(butTh4.cget('text')))
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
                  command=lambda: period_class_opener(butF1.cget('text')))
butF1.grid(row=1, column=1, padx=5, sticky="nsew")

butF2 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][1], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butF2.cget('text')))
butF2.grid(row=1, column=2, padx=5, sticky="nsew")

butF3 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][2], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butF3.cget('text')))
butF3.grid(row=1, column=3, padx=5, sticky="nsew")

butF4 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][3], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butF4.cget('text')))
butF4.grid(row=1, column=4, padx=5, sticky="nsew")

butF5 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][4], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butF5.cget('text')))
butF5.grid(row=1, column=5, padx=5, sticky="nsew")

butF6 = tk.Button(toolsFrame1, text=S7_CSE_tt[4][5], font=("arial", periodFontSize),
                  command=lambda: period_class_opener(butF6.cget('text')))
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