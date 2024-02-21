from tkinter import *
from tkinter import messagebox

####fix the issue where 03+2=0 or 3-03=

r=Tk()
r.title('CALCULATOR')

def click(event):
    global scvalue
    text = event.widget.cget('text')  # Use 'text' instead of 'texts'
    print(text)

    if text == '=':
        if screen.update() == 0:
            scvalue.set("")
            screen.update()
            
        try:
            if scvalue.get().isdigit():
                value = float(scvalue.get())  # converting because it's a string due to StringVar
            else:
                value = eval(screen.get())
            
            scvalue.set(value)
            screen.update()  
        except Exception as e:
            messagebox.showwarning(title='ERROR',message=f"Sorry.\nI have yet to address this particular issue.\n{e}")

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set((scvalue.get() + text))
        screen.update()

r.geometry('250x475')
r.minsize(250,475)   ##fixes it to a particular size frame
r.maxsize(250,475)

scvalue=StringVar()  ###converts it to a string variable
scvalue.set('')

screen=Entry(r,textvar=scvalue,bg='silver',fg='black')
screen.pack(fill='x',padx=5,pady=7)

f=Frame(r,bg='grey',padx=6,pady=5,relief=SUNKEN)  
b=Button(f,text='9',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)   #bind is for binding it to a function or event in this case its click function

b=Button(f,text='8',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='7',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()

f=Frame(r,bg='grey',padx=6,pady=5,relief=SUNKEN)
b=Button(f,text='6',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='5',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='4',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()

f=Frame(r,bg='grey',padx=6,pady=5,relief=SUNKEN)
b=Button(f,text='3',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='2',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='1',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()

f=Frame(r,bg='grey',padx=6,pady=5,relief=SUNKEN)
b=Button(f,text='0',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='+',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='-',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()

f=Frame(r,bg='grey',padx=6,pady=5,relief=SUNKEN)
b=Button(f,text='/',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='%',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='*',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()

f=Frame(r,bg='grey',padx=6,pady=5,relief=SUNKEN)
b=Button(f,text='=',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='.',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text='C',padx=34,pady=20,bg='black',fg='white')
b.pack(side=LEFT)
b.bind('<Button-1>',click)
f.pack()

r.mainloop()