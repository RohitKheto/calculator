from tkinter import *
import tkinter.messagebox as tmsg

def calculate(event):
    global sc
    input=event.widget.cget('text')
    
    if input == '=':
        x=str(screen.get())
        r=str(x[-1])
        if r.isdigit():
            if sc.get()[0]=='0':
                tmsg.showinfo("Invalid Syntax","leading zeros in decimal integer are not permitted")
                sc.set('')
                screen.update()
            else:
                value=eval(screen.get())
                sc.set(value)
                screen.update()
        else:
            tmsg.showinfo("Invalid Syntax","Invalid Expression.")

    elif input == 'C':
        sc.set("")
        screen.update()

    elif input == 'Backspace':
        value=sc.get()
        sc.set(value[0:-1])
        screen.update()

    else :
        sc.set(sc.get()+input)
        screen.update()


root = Tk()

root.geometry("310x600")
root.maxsize(310,600)
root.minsize(310,600)

root.title("SIMPLE CALCULATOR")

l=['C','(',')','%','9' ,'8' ,'7' ,'/ ','6' ,'5' ,'4' ,'*','3' ,'2' ,'1' ,'+','00' , '0','.','-','Backspace','=']
bt=l.copy()
f=['f1','f2','f3','f4','f5','f6']


def theme():
    if slider.get()==1:
        bg1="grey12"
        bg2="black"
        fg2="white"
        bg4="DarkOrange"
        fg4="white"
        bg6="white"
        fg6="black"

    else:
        bg1="white"
        bg2="LightBlue1"
        fg2="navy"
        bg4="blue"
        fg4="white"
        bg6="orchid1"
        fg6="black"
    screen.configure(bg=bg2,fg=fg2)
    title.configure(bg=bg1)
    slider.configure(bg=bg1,fg=fg2)
    root.configure(background=bg1)
    b.configure(bg=bg2,fg=fg2)
    k=0
    for i in range(0,22,4):
        f[k].configure(bg=bg1)
        for j in range(0,4):
            if (i+j)<22 :
                if (l[i+j] == 'C') or (l[i+j] == 'Backspace') :
                    Bg=bg4
                    Fg=fg4
                elif l[i+j]>='0' and l[i+j]<='9' :
                    Bg=bg2
                    Fg=fg2
                else:
                    Bg=bg6
                    Fg=fg6
                bt[i+j].configure(bg=Bg,fg=Fg)
            
        f[k].pack()
        k=k+1


title=Label(root,text="SIMPLE  CALCULATOR",fg="orange red",bg="white",font=("Book Antiqua", 18 ,"bold", "italic"))
title.pack(pady=10,fill=X)


lb="light theme            dark theme"
slider=Scale(root,from_=0,to=1,length=270,width=30,orient=HORIZONTAL,bg="white",fg="navy",bd=0,label=lb,font=("Book Antiqua", 14 ,"bold", "italic"),showvalue=0)
slider.pack()
b=Button(root,text="change theme",font=("Book Antiqua", 11 ,"bold"),bg="LightBlue1",fg="navy",borderwidth=2,relief=RAISED,command=theme)
b.pack(pady=10)

root.configure(background='white')

sc = StringVar()
sc.set("")
screen=Entry(root,textvariable=sc,font=("Book Antiqua", 14 ,"bold"),bg="LightBlue1",fg="navy")
screen.pack(fill=X,padx=18,ipady=15,pady=10)
k=0
for i in range(0,22,4):
    f[k]=Frame(root,bg="white")
    for j in range(0,4):
        if (i+j)<22 :
            if (l[i+j] == 'C') or (l[i+j] == 'Backspace') :
                Bg="blue"
                Fg="white"
            elif l[i+j]>='0' and l[i+j]<='9' :
                Bg="LightBlue1"
                Fg="navy"
            else:
                Bg="orchid1"
                Fg="black"
            if l[i+j]=='=':
                bt[i+j]=Button(f[k],text=l[i+j],font=("Book Antiqua", 12 ,"bold"),padx=50,bg=Bg,fg=Fg,borderwidth=2,relief=RAISED)
            else:
                bt[i+j]=Button(f[k],text=l[i+j],font=("Book Antiqua", 12 ,"bold"),padx=15,bg=Bg,fg=Fg,borderwidth=2,relief=RAISED)
            bt[i+j].pack(side=LEFT,padx=10,pady=10)
            bt[i+j].bind('<Button-1>',calculate)
    f[k].pack()
    k=k+1



root.mainloop()