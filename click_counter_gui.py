from tkinter import *
root=Tk()
root.geometry("300x300")
root.title("CLICK COUNT BY REX")
number=0

#button functin

def clickButton():
    global number
    number+=1
    ShowInfo["text"]="u click "+str(number)+" times"

clickingButton=Button(root,text="click me",padx=50,pady=50,bg="gold",font=("Arial",22),command=clickButton)
ShowInfo=Label(root,text="massage",font=("Arial",22),fg="purple",pady=20)

clickingButton.pack()
ShowInfo.pack()
root.mainloop()