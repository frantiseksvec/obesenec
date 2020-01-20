from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import sys
import os

window = Tk()
window.title("Oběšenec")
window.geometry("574x500")
window.resizable(0, 0)
pokusy = 5
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
img = Image.open('prvni.jpg')
img = img.resize((200, 200), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.place(x=35, y=290)
#Slovník slov
odpovedi = {
    1:"KOMBAJN",2:"TRUBICE",3:"INDUKCE",4:"CENOVKA",5:"BROSKEV",6:"CIBULKA",7:"BLEDULE",8:"DIVADLO",9:"TRAKTOR",10:"KLADINA",11:"IMUNITA",12:"MODELKA",13:"JALOVEC",14:"KLADIVO",
    15:"LEDOVKA",16:"ENERGIE"
}
#Slovník obrázků
obrazky = {
    0: "sesty.jpg",1: "paty.jpg",2: "ctvrty.jpg",3: "treti.jpg",4: "druhy.jpg",5: "prvni.jpg"
}
#Nahodný výběr slov podle přiděleného čísla
vyber = random.randint(1,len(odpovedi))



class App():
    def __init__(self):
        self.btn01 = None
        self.btn02 = None
        self.btn03 = None
        self.btn04 = None
        self.btn05 = None
        self.btn06 = None
        self.btn07 = None
        self.pismenka()
        self.funkce("")

    def reset(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def pismenka(self):
        self.btn01 = Button(window, text=" ",bg="white", fg="Black",width=4,height=1,font=('Times','25'))
        self.btn01.grid(column=2, row=0)
        self.btn02 = Button(window, text=" ",bg="white", fg="Black",width=4,height=1,font=('Times','25'))
        self.btn02.grid(column=3, row=0)
        self.btn03 = Button(window, text=" ",bg="white", fg="Black",width=4,height=1,font=('Times','25'))
        self.btn03.grid(column=4, row=0)
        self.btn04 = Button(window, text=" ",bg="white", fg="Black",width=4,height=1,font=('Times','25'))
        self.btn04.grid(column=5, row=0)
        self.btn05 = Button(window, text=" ",bg="white", fg="Black",width=4,height=1,font=('Times','25'))
        self.btn05.grid(column=6, row=0)
        self.btn06 = Button(window, text=" ",bg="white", fg="Black",width=4,height=1,font=('Times','25'))
        self.btn06.grid(column=7, row=0)
        self.btn07 = Button(window, text=" ",bg="white", fg="Black",width=4,height=1,font=('Times','25'))
        self.btn07.grid(column=8, row=0)
    
    def funkce(self,alphabet):
        btn2 = Button(window, text="K",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("K"))
        btn2.grid(column=2, row=1)
        btn3 = Button(window, text="B",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("B"))
        btn3.grid(column=3, row=1)
        btn4 = Button(window, text="R",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("R"))
        btn4.grid(column=4, row=1)
        btn5 = Button(window, text="V",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("V"))
        btn5.grid(column=5, row=1)
        btn6 = Button(window, text="I",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("I"))
        btn6.grid(column=6, row=1)
        btn7 = Button(window, text="C",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("C"))
        btn7.grid(column=7,row=1)
        btn8 = Button(window, text="O",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("O"))
        btn8.grid(column=8, row=1)
        btn9 = Button(window, text="L",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("L"))
        btn9.grid(column=2, row=2)
        btn10 = Button(window, text="N",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("N"))
        btn10.grid(column=3, row=2)
        btn11= Button(window, text="G",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("G"))
        btn11.grid(column=4, row=2)
        btn12 = Button(window, text="A",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("A"))
        btn12.grid(column=5, row=2)
        btn13 = Button(window, text="D",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("D"))
        btn13.grid(column=6, row=2)
        btn14 = Button(window, text="S",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("S"))
        btn14.grid(column=7, row=2)
        btn16 = Button(window, text="E",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("E"))
        btn16.grid(column=4, row=3)
        btn17 = Button(window, text="J",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("J"))
        btn17.grid(column=5, row=3)
        btn18 = Button(window, text="U",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("U"))
        btn18.grid(column=6, row=3)
        btn18 = Button(window, text="T",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("T"))
        btn18.grid(column=8, row=2)
        btn20 = Button(window, text="M",bg="PaleGreen1", fg="Black",width=4,height=1,font=('Times','25'),command=lambda: self.funkce("M"))
        btn20.grid(column=5, row=4)
        reset = Button(window, text="RESTART",bg="PaleGreen1", fg="Black",width=8,height=1,font=('Times','25'),command=lambda: self.reset())
        reset.place(x=380, y=340)
        
        #Porovnávaní zadaných písmenek s písmenkama ze správné odpovědi
        global pokusy,t1,t2,t3,t4,t5,t6,t7
        if alphabet in odpovedi[vyber]:
            if alphabet==odpovedi[vyber][0:1]:
                t1 = t1 + 1
                self.btn01["text"] = alphabet;
            if alphabet==odpovedi[vyber][1:2]:
                self.btn02["text"] = alphabet;
                t2 = t2 + 1
            if alphabet==odpovedi[vyber][2:3]:
                self.btn03["text"] = alphabet;
                t3 = t3 + 1
            if alphabet==odpovedi[vyber][3:4]:
                self.btn04["text"] = alphabet;
                t4 = t4 + 1
            if alphabet==odpovedi[vyber][4:5]:
                self.btn05["text"] = alphabet;
                t5 = t5 + 1
            if alphabet==odpovedi[vyber][5:6]:
                self.btn06["text"] = alphabet;
                t6 = t6 + 1
            if alphabet==odpovedi[vyber][6:7]:
                self.btn07["text"] = alphabet;
                t7 =  t7 + 1
            if t1 > 1 or t2 > 1 or t3 > 1 or t4 > 1 or t5 > 1 or t6 > 1 or t7 > 1:
                pokusy = pokusy - 1
                image = Image.open(obrazky[pokusy])
                image = image.resize((200, 200), Image.ANTIALIAS)
                imgnew = ImageTk.PhotoImage(image)
                panel.configure(image=imgnew)
                panel.image = imgnew
            if pokusy == 0:
                messagebox.showwarning("Konec","Prohrál jsi!!!!")
            if pokusy < 0:
                pokusy = 0
        else:
            pokusy = pokusy - 1
            image = Image.open(obrazky[pokusy])
            image = image.resize((200, 200), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.image = imgnew
            if pokusy == 0:
                messagebox.showwarning("Konec","Prohrál jsi!!!!")
            if pokusy < 0:
                pokusy = 0
            #Porovnavní zadaného slova  ze slovem ze slovníku
        if self.btn01["text"]==odpovedi[vyber][0:1] and self.btn02["text"]==odpovedi[vyber][1:2] and self.btn03["text"]==odpovedi[vyber][2:3] and self.btn04["text"]==odpovedi[vyber][3:4] and self.btn05["text"]==odpovedi[vyber][4:5] and self.btn06["text"]==odpovedi[vyber][5:6]and self.btn07["text"]==odpovedi[vyber][6:7]:
            messagebox.showwarning("Hurá","Vyhrál jsi!!!!")
        print(pokusy)
        print(vyber)
        pocet=Label(window,text=pokusy)
        pocet.grid(row=5,column=5)
        pocet.config(font=("Courier", 44))
myapp = App()
window.mainloop()
