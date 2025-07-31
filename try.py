from tkinter import *
root=Tk()
root.geometry("300x300")
root.title("COunter ")

number=0

def clickButton():
    global number
    number+=1
    ShowInfo["text"]="U click "+str(number)+" Times"

clickingButton=Button(root,text="click me",padx=50,pady=50,font=("Arial",22),bg="gold",command=clickButton)
ShowInfo=Label(root,text="massge",font=("Arial",22),pady=11,fg="green")

clickingButton.pack()
ShowInfo.pack()

root.mainloop()