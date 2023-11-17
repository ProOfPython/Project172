from tkinter import *

root = Tk()
root.title('Dictionary w/ Emails')
root.geometry('450x450')
root.configure(bg = 'snow')

emails = {}

entName = Entry(root)
entName.place(relx = 0.5, rely = 0.3, anchor = CENTER)

entEmail = Entry(root)
entEmail.place(relx = 0.5, rely = 0.4, anchor = CENTER)

def addInfo(name, email):
    emails[name] = email
    lblInfo['text'] = emails

btnAdd = Button(root, text = 'Add Info', 
    command = lambda: addInfo(entName.get(), entEmail.get())
)

btnAdd.place(relx = 0.5, rely = 0.5, anchor = CENTER)

lblInfo = Label(root, bg = 'light blue', text = '')
lblInfo.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()