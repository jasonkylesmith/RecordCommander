from tkinter import *

window=Tk()
window.title('Record Commander')
window.configure(bg="#1f1f1f")
window.geometry("300x200")
window.resizable(False, False)


""" 
https://www.tutorialspoint.com/python/tk_frame.htm """

wins=0
losses=0
ties=0

record="Reset"

def resetRecord():
    file = open("record.txt", "a+")
    file.truncate(0)
    file.write("Record 0-0")
    file.close

def updateRecord():
    global wins
    global losses
    global ties
    global record
    if ties < 1:
        record = "Record "+str(wins)+"-"+str(losses)
    else:
        record = "Record "+str(wins)+"-"+str(losses)+"-"+str(ties)
    file = open("record.txt", "r+")
    file.truncate(0)
    file.write(record)
    file.close

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)


winsLbl=Label(window, text="Wins", font=("Helvetica", 30), background="#1f1f1f", foreground="white")
winsLbl.grid(column=0, row=0, columnspan=3, sticky=W, padx=5)

winsNum=Label(window, text=wins, font=("Helvetica", 30), width=2, background="#1f1f1f", foreground="white")
winsNum.grid(column=3, row=0, columnspan=2, sticky=E)

winsBtnFrm=Frame(window)
winsBtnFrm.columnconfigure(0, weight=1)
winsBtnFrm.columnconfigure(1, weight=1)
winsBtnFrm.rowconfigure(0, weight=1)
winsBtnFrm.grid(column=5, row=0, columnspan=2, sticky=E, padx=5)

winMnsBtn=Button(winsBtnFrm, text="-", font=("Helvetica", 16), width=1, bg="white", foreground="#1f1f1f")
winMnsBtn.grid(column=0, row=0, ipadx=10, ipady=0)

winPlsBtn=Button(winsBtnFrm, text="+", font=("Helvetica", 16), width=1, bg="white", foreground="#1f1f1f")
winPlsBtn.grid(column=1, row=0, ipadx=10, ipady=0)

def increaseWins(event):
    global wins
    global winsNum
    wins += 1
    winsNum.config(text=wins)
    updateRecord()

def decreaseWins(event):
    global wins
    global winsNum
    if wins > 0:
        wins -= 1
    winsNum.config(text=wins)
    updateRecord()
    
winPlsBtn.bind('<Button-1>', increaseWins)
winMnsBtn.bind('<Button-1>', decreaseWins)



lossLbl=Label(window, text="Losses", font=("Helvetica", 30), background="#1f1f1f", foreground="white")
lossLbl.grid(column=0, row=1, columnspan=3, sticky=W, padx=5)

lossNum=Label(window, text=losses, font=("Helvetica", 30), width=2, background="#1f1f1f", foreground="white")
lossNum.grid(column=3, row=1, columnspan=2, sticky=E)

lossesBtnFrm=Frame(window)
lossesBtnFrm.columnconfigure(0, weight=1)
lossesBtnFrm.columnconfigure(1, weight=1)
lossesBtnFrm.rowconfigure(0, weight=1)
lossesBtnFrm.grid(column=5, row=1, columnspan=2, sticky=E, padx=5)

lossMnsBtn=Button(lossesBtnFrm, text="-", font=("Helvetica", 16), width=1, bg="white", foreground="#1f1f1f")
lossMnsBtn.grid(column=0, row=0, ipadx=10, ipady=0)

lossPlsBtn=Button(lossesBtnFrm, text="+", font=("Helvetica", 16), width=1, bg="white", foreground="#1f1f1f")
lossPlsBtn.grid(column=1, row=0, ipadx=10, ipady=0)

def increaseLosses(event):
    global losses
    global lossNum
    losses += 1
    lossNum.config(text=losses)
    updateRecord()

def decreaseLosses(event):
    global losses
    global lossNum
    if losses > 0:
        losses -= 1
    lossNum.config(text=losses)
    updateRecord()

lossPlsBtn.bind('<Button-1>', increaseLosses)
lossMnsBtn.bind('<Button-1>', decreaseLosses)



tiesLbl=Label(window, text="Ties", font=("Helvetica", 30), background="#1f1f1f", foreground="white")
tiesLbl.grid(column=0, row=2, columnspan=3, sticky=W, padx=5)

tiesNum=Label(window, text=wins, font=("Helvetica", 30), width=2, background="#1f1f1f", foreground="white")
tiesNum.grid(column=3, row=2, columnspan=2, sticky=E)

tiesBtnFrm=Frame(window)
tiesBtnFrm.columnconfigure(0, weight=1)
tiesBtnFrm.columnconfigure(1, weight=1)
tiesBtnFrm.rowconfigure(0, weight=1)
tiesBtnFrm.grid(column=5, row=2, columnspan=2, sticky=E, padx=5)

tieMnsBtn=Button(tiesBtnFrm, text="-", font=("Helvetica", 16), width=1, bg="white", foreground="#1f1f1f")
tieMnsBtn.grid(column=0, row=0, ipadx=10, ipady=0)

tiePlsBtn=Button(tiesBtnFrm, text="+", font=("Helvetica", 16), width=1, bg="white", foreground="#1f1f1f")
tiePlsBtn.grid(column=1, row=0, ipadx=10, ipady=0)

def increaseTies(event):
    global ties
    global tiesNum
    ties += 1
    tiesNum.config(text=ties)
    updateRecord()

def decreaseTies(event):
    global ties
    global tiesNum
    if ties > 0:
        ties -= 1
    tiesNum.config(text=ties)
    updateRecord()
    
tiePlsBtn.bind('<Button-1>', increaseTies)
tieMnsBtn.bind('<Button-1>', decreaseTies)

window.bind('<Control-Key-1>', increaseWins)

def main():
    resetRecord()

if __name__ == "__main__":
    main()


window.mainloop()

