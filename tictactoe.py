from tkinter import *
root=Tk()
turn=1
x=0
y=0
def check():
    a=b1["text"]
    b=b2["text"]
    c=b3["text"]
    d=b4["text"]
    e=b5["text"]
    f=b6["text"]
    g=b7["text"]
    h=b8["text"]
    i=b9["text"]
    if(len(a)!=0 and len(b)!=0 and len(c)!=0):
        if a==b and a==c:
            if a=="*":
                print("Player1 is winner")
            else:
                print("Player2 is winner")
            restart()
    if (len(d) != 0 and len(e) != 0 and len(f) != 0):
        if d==e and d==f:
            if d=="*":
                print("Player1 is winner")
                add()
            else:
                print("Player2 is winner")
                add1()
            restart()
    if (len(g) != 0 and len(h) != 0 and len(i) != 0):
        if g==h and g==i:
            if g=="*":
                print("Player1 is winner")
                add()
            else:
                print("Player2 is winner")
                add1()
            restart()
    if (len(a) != 0 and len(e) != 0 and len(i) != 0):
        if a==e and a==i:
            if a=="*":
                print("Player1 is winner")
                add()
            else:
                print("Player2 is winner")
                add1()
            restart()
    if (len(c) != 0 and len(e) != 0 and len(g) != 0):
        if c==e and c==g:
            if e=="*":
                print("Player1 is winner")
                add()
            else:
                print("Player2 is winner")
                add1()
            restart()
    if (len(a) != 0 and len(d) != 0 and len(g) != 0):
        if a==d and a==g:
            if a=="*":
                print("Player1 is winner")
                add()
            else:
                print("Player2 is winner")
                add1()
            restart()
    if (len(b) != 0 and len(e) != 0 and len(h) != 0):
        if b==e and b==h:
            if b=="*":
                print("Player1 is winner")
                add()
            else:
                print("Player2 is winner")
                add1()
            restart()
    if (len(c) != 0 and len(f) != 0 and len(i) != 0):
        if c==f and c==i:
            if c=="*":
                print("Player1 is winner")
                add()
            else:
                print("Player2 is winner")
                add1()
            restart()
    if turn==10:
        print("Draw")
        add()
        add1()
        restart()
def restart():
    b1.config(text="")
    b2.config(text="")
    b3.config(text="")
    b4.config(text="")
    b5.config(text="")
    b6.config(text="")
    b7.config(text="")
    b8.config(text="")
    b9.config(text="")
    global turn
    turn=1
def add():
    global x
    x=x+1
    l3.config(text=x)
def add1():
    global y
    y=y+1
    l4.config(text=y)
def show1():
    global turn
    if len(b1["text"])==0:
        if turn%2==1:
            b1.config(text="*")
        else:
            b1.config(text="o")
        turn=turn+1
    check()
def show2():
    global turn
    if len(b2["text"])==0:
        if turn%2==1:
            b2.config(text="*")
        else:
            b2.config(text="o")
        turn=turn+1
    check()
def show3():
    global turn
    if len(b3["text"])==0:
        if turn%2==1:
            b3.config(text="*")
        else:
            b3.config(text="o")
        turn=turn+1
    check()
def show4():
    global turn
    if len(b4["text"])==0:
        if turn%2==1:
            b4.config(text="*")
        else:
            b4.config(text="o")
        turn=turn+1
    check()
def show5():
    global turn
    if len(b5["text"])==0:
        if turn%2==1:
            b5.config(text="*")
        else:
            b5.config(text="o")
        turn=turn+1
    check()
def show6():
    global turn
    if len(b6["text"])==0:
        if turn%2==1:
            b6.config(text="*")
        else:
            b6.config(text="o")
        turn=turn+1
    check()
def show7():
    global turn
    if len(b7["text"])==0:
        if turn%2==1:
            b7.config(text="*")
        else:
            b7.config(text="o")
        turn=turn+1
    check()
def show8():
    global turn
    if len(b8["text"])==0:
        if turn%2==1:
            b8.config(text="*")
        else:
            b8.config(text="o")
        turn=turn+1
    check()
def show9():
    global turn
    if len(b9["text"])==0:
        if turn%2==1:
            b9.config(text="*")
        else:
            b9.config(text="o")
        turn=turn+1
    check()
l1=Label(text="p1")
l2=Label(text="p2")
l3=Label(text="0")
l4=Label(text="0")
l1.grid(row=0,column=0)
l3.grid(row=0,column=1)
l2.grid(row=0,column=2)
l4.grid(row=0,column=3)
b1=Button(command=show1)
b2=Button(command=show2)
b3=Button(command=show3)
b4=Button(command=show4)
b5=Button(command=show5)
b6=Button(command=show6)
b7=Button(command=show7)
b8=Button(command=show8)
b9=Button(command=show9)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
mainloop()


