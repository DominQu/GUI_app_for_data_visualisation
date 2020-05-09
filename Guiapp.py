from tkinter import *
from tkinter import messagebox
from tkinter import Menu
window = Tk()
window.title("Welcome")
window.geometry('350x200')
menu = Menu(window)

new_item = Menu(menu, tearoff=0)

new_item.add_command(label='New')

menu.add_cascade(label='File', menu=new_item)
menu.add_cascade(label='Edit')

window.config(menu=menu)
lbl = Label(window, text="Hello", font=("Arial Bold", 13))
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()
def clicked():
    messagebox.showwarning('Uwaga!', 'Kliknąłeś!')
btn = Button(window, text="Button", command=clicked)
btn.grid(column=2, row=0)
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=3, row=0)
rad1 = Radiobutton(window,text='First', value=1)

rad2 = Radiobutton(window,text='Second', value=2)

rad3 = Radiobutton(window,text='Third', value=3)

rad1.grid(column=0, row=1)

rad2.grid(column=1, row=1)

rad3.grid(column=2, row=1)
window.mainloop()