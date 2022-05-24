import tkinter
import json

def sub():
    with open('D:/py.json') as f:
        dct=json.load(f)
    l=txt.get()
    h=txt2.get()
    if l in dct and dct[l]==h:
       lbl3.configure(text='username and password already used!',fg='green')
    else:
        dct={}
        dct[l]=h
        with open('D:/py.json','w') as b:
            json.dump(dct,b)
        lbl3.configure(text='Thank you for saving your username in the program.',fg='green')    

def login():
    a=txt.get()
    b=txt2.get()
    with open('D:/py.json') as f:
        dct=json.load(f)
    if a in dct and dct[a]==b:
        lbl3.configure(text='welcome to py app',fg='green')
    else:
        lbl3.configure(text='try agin !',fg='red')
    


def delete():
        s=txt.get()
        b=txt2.get()
        dct1={}
        with open ('D:/py.json') as f:
            dct=json.load(f)
        if s in dct and dct[s]==b:
           dct1[s]=b
           dct1.pop(s)
           with open('D:/py.json','w') as b:
               json.dump(dct1,b)
               lbl3.configure(text='your username removed from your account !',fg='red')
win=tkinter.Tk()
win.title('<py>')
win.geometry('720x480')

lbl1=tkinter.Label(win,text='username:>>>',fg='red')
lbl1.grid(column=3,row=1)

lbl2=tkinter.Label(win,text='password:>>>',fg='red')
lbl2.grid(column=3,row=4)

lbl3=tkinter.Label(win,text='')
lbl3.grid(column=10,row=16)

txt = tkinter.Entry(win,width=30,fg='blue')
txt.grid(column=10,row=1,pady=10)

txt2 = tkinter.Entry(win,width=30,fg='blue')
txt2.grid(column=10,row=4,pady=10)

btn= tkinter.Button(win,text="submit",command=sub,bg='silver',fg='black')
btn.grid(column=9,row=8)
btn1= tkinter.Button(win,text="login",command=login,bg='green',fg='black')
btn1.grid(column=10,row=8)
btn2= tkinter.Button(win,text="delete",command=delete,bg='red',fg='black')
btn2.grid(column=11,row=8)

win.mainloop()