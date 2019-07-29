from tkinter import messagebox, Tk, Canvas, ALL,LEFT,RIGHT,TOP,Label,Button
#from tkinter import *
#from tkinter import messagebox
import sudoku
import sys


class sudoku9x9(object):
    def __init__(self,puzzle,answer):
        self.answer=answer
        self.puzzle=puzzle
        self.b=[]
        for Y in range(9):
            for X in range(9):
                self.b.append(grids(puzzle[X][Y],X,Y,answer[X][Y]))
    def deneme(self):
        for i in self.b:
            if i.answer!=i.number:
                i.can.config(background="red")
            else:
                i.can.config(background="white")

class grids:
    def __init__(self,number,x,y,answer):
        self.number=number
        self.x=x
        self.y=y
        self.answer=answer 
        self.can=Canvas(root,width=50,height=50,background='white',highlightbackground='darkblue',highlightthickness=1)
        self.can.grid(row=x,column=y)
        self.can.create_text(25,25,text=number,fill="Black",font="Times 20")
        self.can.bind("<Button-1>",self.click) #Kutuya tıklama
        if(self.number==None):
            self.can.focus_set()
    def click(self,event):#Tıklama event
        # print("clicked at", self.x, self.y , self.number)
        if self.number==None:
            self.can.focus_set()
            self.can.bind("<Key>",self.key)
        else:
            self.can.focus_force()
    def key(self,event):#Tuşa basma event
        # print("pressed",self.x,self.y,self.number)
        if event.char in "123456789":
            # print("sayı")
            self.number=int(event.char)
            puzzle[self.x][self.y]=self.number
            self.can.delete(ALL)
            self.can.create_text(25,25,text=self.number,fill="brown",font="Times 20")
            # print(puzzle)
            self.check()
    def check(self):
        if self.checkpuzzle() is False:
            if puzzle==answer:
                messagebox.showinfo("","Kazandınız!")
                root.destroy()
            else:
                sudoku9x9.deneme(Anaoyun)
    def checkpuzzle(self):
        for i in puzzle:
            if None in i:
                return True
        return False

#region zorluk fonksiyon
def bfunction1():
    global ZORLUK
    ZORLUK=1
    root2.destroy()
def bfunction2():
    global ZORLUK
    ZORLUK=2
    root2.destroy()
def bfunction3():
    global ZORLUK
    ZORLUK=3
    root2.destroy()
#endregion
    
#region Zorluk Penceresi
root2=Tk()
lb1=Label(root2,text="Zorluk Seçiniz")
lb1.pack(side=TOP)
bt1=Button(root2,text="Kolay",width=15,height=3,command=bfunction1)
bt1.pack(side=LEFT)
bt2=Button(root2,text="Orta",width=15,height=3,command=bfunction2)
bt2.pack(side=LEFT)
bt3=Button(root2,text="Zor",width=15,height=3,command=bfunction3)
bt3.pack(side=LEFT)
root2.mainloop()
#endregion


#region Sudoku çözümlü ve çözümsüz hali
answer=sudoku.generateSudoku()
puzzle=[]
for i in range(len(answer)):
    puzzle.append([])
    for j in range(len(answer[0])):
        puzzle[i].append(answer[i][j])
try: #ilk ekranda çıkarsan programı kapatır
    puzzle=sudoku.generatePuzzle(puzzle,ZORLUK)
except:
    exit()

print(answer)
print(puzzle)
#endregion

#region Oyun Penceresi
root=Tk()
root.configure(background="Black")
Anaoyun=sudoku9x9(puzzle,answer)
root.mainloop()
#endregion


