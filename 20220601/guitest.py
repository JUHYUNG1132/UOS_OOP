from tkinter import *

window = Tk()
window.geometry('700x400')

def eventProcess(event):
    print(event.x, event.y, '에서 마우스 클릭')

def process():
    print('버튼 클릭')

label = Label(window, text = 'hello tkinter!!')
label.pack(side=LEFT)

button = Button(window, text='hello!!', bg='red', fg='blue',
                width=40, height=20,
                command=process) # <= 버튼을 누르면 process 수행
button.pack()

entry = Entry(window, fg = 'black', bg='yellow', width = 80)
entry.pack()

window.bind('<Button-1>', eventProcess)

window.mainloop()
