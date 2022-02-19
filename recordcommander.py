from tkinter import *
window=Tk()

wins=0
losses=0
ties=0

record="Reset"

def resetRecord():
    file = open("record.txt", "a+")
    file.truncate(0)
    file.write("Record 0-0")
    file.close


winsLbl=Label(window, text="Wins", font=("Helvetica", 30))
winsLbl.place(x=0, y=0)

winsNum=Label(window, text=wins, font=("Helvetica", 30))
winsNum.place(x=140, y=0)

winMnsBtn=Button(window, text="-", font=("Helvetica", 16))
winMnsBtn.place(x=220, y=0)

winPlsBtn=Button(window, text="+", font=("Helvetica", 16))
winPlsBtn.place(x=250, y=0)

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

lossLbl=Label(window, text="Losses", font=("Helvetica", 30))
lossLbl.place(x=0, y=60)

lossNum=Label(window, text=losses, font=("Helvetica", 30))
lossNum.place(x=140, y=60)

lossMnsBtn=Button(window, text="-", font=("Helvetica", 16))
lossMnsBtn.place(x=220, y=60)

lossPlsBtn=Button(window, text="+", font=("Helvetica", 16))
lossPlsBtn.place(x=250, y=60)

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

tiesLbl=Label(window, text="Ties", font=("Helvetica", 30))
tiesLbl.place(x=0, y=120)

tiesNum=Label(window, text=wins, font=("Helvetica", 30))
tiesNum.place(x=140, y=120)

tieMnsBtn=Button(window, text="-", font=("Helvetica", 16))
tieMnsBtn.place(x=220, y=120)

tiePlsBtn=Button(window, text="+", font=("Helvetica", 16))
tiePlsBtn.place(x=250, y=120)

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

""" window.bind('<Control-Key-1>', increaseWins) """



def main():
    resetRecord()

if __name__ == "__main__":
    main()

window.title('Record Commander')
window.geometry("300x170+10+10")
window.resizable(False, False)
window.mainloop()

