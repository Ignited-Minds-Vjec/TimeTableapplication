import tkinter as tk

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


def print_value(value):
    print(value)


def button_value(val):
    val = val.split()
    return val[0]+val[1]+'\n'+val[2]


root = tk.Tk()
root.geometry("900x300")
span = 1
k = 0
i = 0
while i < len(S7_CSE_tt):
    j = 0
    while j < len(S7_CSE_tt[i]):
        span = 1
        for k in range(j, len(S7_CSE_tt[i])-1):
            if S7_CSE_tt[i][k] == S7_CSE_tt[i][k+1]:
                span += 1
            else:
                break
        button = tk.Button(root,
                           text=button_value(S7_CSE_tt[i][j]),
                           command=lambda number=S7_CSE_tt[i][j]: print_value(number))
        button.grid(row=i, column=j, columnspan=span, padx=10, sticky="nsew")
        if j != k and (j != len(S7_CSE_tt[i]) - 1):
            j += span
        else:
            j += 1
    i += 1
root.mainloop()


'''
k = 0
    i = 0
    while i < len(S7_CSE_tt):
        j = 0
        while j < len(S7_CSE_tt[i]):
            span = 1
            for k in range(j, len(S7_CSE_tt[i]) - 1):
                if S7_CSE_tt[i][k] == S7_CSE_tt[i][k + 1]:
                    span += 1
                else:
                    break
            button = tk.Button(toolsFrame1,
                               text=button_value(S7_CSE_tt[i][j]),
                               font=("arial", timeFontSize),
                               command=lambda number=S7_CSE_tt[i][j]: period_class(number))
            button.grid(row=i, column=j, columnspan=span, padx=10, sticky="nsew")
            if j != k and (j != len(S7_CSE_tt[i]) - 1):
                j += span
            else:
                j += 1
        i += 1
'''