import random
import array as arr

def fill(grid):
    available=[1,2,3,4,5,6,7,8,9]
    for i in grid:
        available.remove(i)
    return available

def ms(): #9x9luk alan açıyor
    matris=[]
    for i in range(9):
        matris.append([])
        for y in range(9):
            matris[i].append(0)
    return matris

def check(x,y,sudoku):
    exist=[]
    for i in sudoku[x]:#Aynı satırdaki sayılar
        exist.append(i)
    
    for i in range(len(sudoku)):#Aynı sütundaki sayılar
        exist.append(sudoku[i][y])
    
    exist+=checkGrid(x,y,sudoku)#3x3lük kare alanı kontrol
    
    exist=list(dict.fromkeys(exist))#Listeyi sözlüğe çeviriyorumki tekrar eden elemanlar silinsin, sonra bunu tekrar diziye çeviriyorum.
    exist.remove(0)
    return exist

def checkGrid(x,y,sudoku):#3x3lük kare alanı kontrol
    existG=[]
    if x<3:
        if y<3:
            for i in range(3):
                for y in range(3):
                    existG.append(sudoku[i][y])
        elif y<6:
            for i in range(3):
                for y in range(3,6):
                    existG.append(sudoku[i][y])
        else:
            for i in range(3):
                for y in range(6,9):
                    existG.append(sudoku[i][y])
    elif x<6:
        if y<3:
            for i in range(3,6):
                for y in range(3):
                    existG.append(sudoku[i][y])
        elif y<6:
            for i in range(3,6):
                for y in range(3,6):
                    existG.append(sudoku[i][y])
        else:
            for i in range(3,6):
                for y in range(6,9):
                    existG.append(sudoku[i][y])
    else:
        if y<3:
            for i in range(6,9):
                for y in range(3):
                    existG.append(sudoku[i][y])
        elif y<6:
            for i in range(6,9):
                for y in range(3,6):
                    existG.append(sudoku[i][y])
        else:
            for i in range(6,9):
                for y in range(6,9):
                    existG.append(sudoku[i][y])
    return existG

def deleteRow(x,sudoku):
    for i in range(len(sudoku)):
        sudoku[x][i]=0
    return sudoku

def generateSudoku():
    sudoku=ms()
    for x in range(len(sudoku)):
        y=0
        while 0 in sudoku[x]: #Sırada 0 olduğu sürece devam et
            exist=check(x,y,sudoku)
            a=fill(exist)
            try: #Sayı eklemeyi dene
                sudoku[x][y]=random.choice(a)
                y=y+1
            except IndexError: #Hata varsa bütün sırayı sıfırla, tekrar başla
                sudoku=deleteRow(x,sudoku)
                y=0

    return sudoku

def generatePuzzle(matris,zorluk):
    temp=[]
    temp=matris.copy()
    if zorluk==1:
        for i in range(random.randint(15,20)):
            temp[random.randint(0,8)][random.randint(0,8)]=None
    elif zorluk==2:
        for i in range(random.randint(30,45)):
            temp[random.randint(0,8)][random.randint(0,8)]=None
    elif zorluk==3:
        for i in range(random.randint(50,65)):
            temp[random.randint(0,8)][random.randint(0,8)]=None
    
    return temp