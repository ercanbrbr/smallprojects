from tkinter import messagebox, Tk, Canvas, ALL
#from tkinter import *
#from tkinter import messagebox
import sudoku

class grids:
    def __init__(self,number,x,y):
        self.number=number
        self.x=x
        self.y=y
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
            if puzzle==answer:
                messagebox.showinfo("","Kazandınız!")
            # print(puzzle)
        
        

#region Sudoku çözümlü ve çözümsüz hali
answer=sudoku.generateSudoku()
puzzle=[]
for i in range(len(answer)):
    puzzle.append([])
    for j in range(len(answer[0])):
        puzzle[i].append(answer[i][j])
puzzle=sudoku.generatePuzzle(puzzle)
print(answer)
print(puzzle)
#endregion

#region tkinter
root=Tk()
root.configure(background="Black")
b=[]
for Y in range(9):
    for X in range(9):
        b.append(grids(puzzle[X][Y],X,Y))

root.mainloop()
#endregion


