# creating a Matrix GUI application
from tkinter import *
from tkinter import messagebox
import pickle
from PIL import ImageTk, Image
# creating  a window
win = Tk()
win.title('Matrix GUI')
win.configure(bg='white')
win.geometry("1366x768")

# background image
image = Image.open("images/matrix.png")
image = image.resize((1366, 768), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(image)

# creating a canvas
my_canvas = Canvas(win, width="1366", height="768")
my_canvas.pack(fill="both", expand=True)

# setting image in canvas
my_canvas.create_image(0, 0, image=bg, anchor="nw")

# adding a label
my_canvas.create_text(690, 100, text='BELOW ARE THE OPERATIONS THAT YOU CAN PERFORM IN A MATRIX', fill="white",
                      font=("Britannic bold", 30))

global allmat
allmat = pickle.load(open('alldict.p', "rb"))


def isempty(box):
    if len(box.get()) == 0:
        return True
    else:
        return False


def end():
    if isempty(enter):
        messagebox.showerror('Fill all box', 'one or more boxes are empty!!')
    else:
        size = len(entrybox)
        x = 0
        for i in range(int(row)):
            textrow = []
            for j in range(int(col)):
                if x < size:
                    textrow.append(entrybox[x].get())
                    x += 1
                else:
                    break
            lst.append(textrow)
        allmat[name] = lst
        messagebox.showinfo("Matrix creation successfull ", "Matrix Created Successfully!")
        poo.destroy()
        pickle.dump(allmat, open('alldict.p', 'wb'))

"""function to create the matrix"""

def createmat():
    new = Toplevel()
    new.geometry("683x384")

    # creating row and column labels
    Label(new, text='ROW       = ', font=("aria", 15)).place(x=200, y=0)
    Label(new, text='COLUMN = ', font=("aria", 15)).place(x=200, y=100)
    Label(new, text='NAME    =', font=("aria", 15)).place(x=200, y=200)

    # creating entries for getting row and column
    row_entry = Entry(new)
    row_entry.place(x=312, y=5)
    col_entry = Entry(new)
    col_entry.place(x=312, y=105)
    name_entry = Entry(new)
    name_entry.place(x=312, y=205)

    # creating publish function
    def publish():
        global name
        global poo
        global lst
        global row
        global col
        row = row_entry.get()
        col = col_entry.get()
        name = name_entry.get()
        if name in allmat.keys():
            messagebox.showerror('Name exist!', 'Try another name!!!')
            name_entry.delete(0, END)
        elif isempty(row_entry) or isempty(col_entry) or isempty(name_entry):
            messagebox.showerror("Empty box", "One or more entry is emptY!!")
        else:
            global var
            global num
            global enter
            global entrybox
            global entries
            new.destroy()
            poo = Toplevel()
            poo.geometry("683x384")
            Label(poo, text='Enter the elements in the matrix below ', font=("aria", 15)).pack()
            entrybox = []
            lst = []
            lblframe = LabelFrame(poo, bg="cyan")
            lblframe.pack(pady=10)
            global var
            for i in range(1, int(row) + 1):
                for j in range(1, int(col) + 1):
                    enter = Entry(lblframe, width=10)
                    enter.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                    entrybox.append(enter)

            finish = Button(poo, text='OK', width=10, bg='green', command=end)
            finish.pack()


    # creating ok button
    ok = Button(new, text='     OK      ', bg='red', command=publish)
    ok.place(x=270, y=305)


def done():
    x = entrybox.get()
    if x in allmat.keys():
        window = Toplevel()
        window.configure(bg='blue')
        matname = Label(window, text=str(x).capitalize())
        matname.pack()
        matname.configure(anchor='center')
        frame = LabelFrame(window, bg='red', width=4)
        frame.pack()
        rows = len(allmat[x])
        columns = len(allmat[x][0])

        for i in range(rows):
            for j in range(columns):
                entery = Entry(frame, width=6)
                entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                entery.insert(0, str(allmat[x][i][j]))
                entery.configure(state='disabled')

    else:
        messagebox.showerror('Invalid', 'Name does not exists!')

"""function to display the already created matrix"""

def showmat():
    global entrybox
    top1 = Toplevel()
    top1.configure(bg='green')
    ask = Label(top1, bg='white', text='Enter the name of the Matrix you want to see:', font=("Courier New", 15, "bold"))
    ask.grid(row=0, column=1, pady=10)
    entrybox = Entry(top1)
    entrybox.grid(row=1, column=1, ipadx=50)
    ok = Button(top1, text='OK', bg='white', fg="black", command=done)
    ok.grid(row=2, column=1, pady=(10, 10), ipadx=20)

"""function to find the addition of two matrices"""
def addmat():
    # adding labels and buttons
    khol = Toplevel()
    khol.configure(bg='green')
    x = Label(khol, text='Name 1 : ')
    title = Label(khol, text='ENTER THE NAMES OF TWO MATRIX YOU WANT TO ADD', font=("Courier New", 15, "bold"))
    x.grid(row=1, column=0, pady=10)
    title.grid(row=0, column=0, columnspan=2, pady=(4, 10))
    y = Label(khol, text='Name 2 : ')
    y.grid(row=2, column=0, pady=10)
    enter1 = Entry(khol)
    enter1.grid(row=1, column=1)
    enter2 = Entry(khol)
    enter2.grid(row=2, column=1)

    # creating start function to add matrices
    def start():
        p1 = enter1.get()
        p2 = enter2.get()
        if p1 and p2 in allmat.keys():
            khol.destroy()
            if len(allmat[p1]) == len(allmat[p2]) and len(allmat[p1][0]) == len(allmat[p2][0]):
                load = Toplevel()
                load.configure(bg='royal blue')
                Label(load, text=str(p1)).grid(row=0, column=0, pady=(10, 10))
                lbl1 = LabelFrame(load, bg='dark slate blue')
                Label(load, text=str(p2)).grid(row=0, column=2, pady=(10, 10))
                lbl2 = LabelFrame(load, bg='dark slate blue')
                Label(load, text='NEW MATRIX').grid(row=0, column=4, pady=(10, 10))
                lbl3 = LabelFrame(load, bg='dark slate blue')
                lbl1.grid(row=1, column=0, pady=10, padx=(10, 10))
                Label(load, text='+', bg='royal blue').grid(row=1, column=1, pady=10)
                lbl2.grid(row=1, column=2, pady=10, padx=(10, 10))
                Label(load, text='=', bg='royal blue').grid(row=1, column=3, pady=10)
                lbl3.grid(row=1, column=4, pady=10, padx=(10, 10))

                # displaying matrix
                for i in range(len(allmat[p1])):
                    for j in range(len(allmat[p1][0])):
                        entery = Entry(lbl1, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(allmat[p1][i][j]))
                        entery.configure(state='disabled')

                for i in range(len(allmat[p2])):
                    for j in range(len(allmat[p2][0])):
                        entery = Entry(lbl2, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(allmat[p2][i][j]))
                        entery.configure(state='disabled')

                for i in range(len(allmat[p2])):
                    for j in range(len(allmat[p2][0])):
                        value = int(allmat[p1][i][j]) + int(allmat[p2][i][j])
                        entery = Entry(lbl3, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(value))
                        entery.configure(state='disabled')
            else:
                messagebox.showerror('Critical error!', 'row or column size doesnt matches!')
        elif p1 and p2 not in allmat.keys():
            messagebox.showerror('None existence!', 'one or both matrices doesnt exists!!')

    ok = Button(khol, text='OK', relief=RAISED, command=start)
    ok.grid(row=3, column=0, columnspan=2, ipadx=10, pady=10)


# function to subtract two matrices
def sub_mat():
    # adding labels and buttons
    khol = Toplevel()
    khol.configure(bg='green')
    x = Label(khol, text='Name 1 : ')
    title = Label(khol, text='ENTER THE NAMES OF TWO MATRIX YOU WANT TO SUBTRACT', font=("Courier New", 15, "bold"))
    x.grid(row=1, column=0, pady=10)
    title.grid(row=0, column=0, columnspan=2, pady=(4, 10))
    y = Label(khol, text='Name 2 : ')
    y.grid(row=2, column=0, pady=10)
    enter1 = Entry(khol)
    enter1.grid(row=1, column=1)
    enter2 = Entry(khol)
    enter2.grid(row=2, column=1)

    def begin():
        p1 = enter1.get()
        p2 = enter2.get()
        if p1 and p2 in allmat.keys():
            khol.destroy()
            if len(allmat[p1]) == len(allmat[p2]) and len(allmat[p1][0]) == len(allmat[p2][0]):
                load = Toplevel()
                load.configure(bg='royal blue')
                Label(load, text=str(p1)).grid(row=0, column=0, pady=(10, 10))
                lbl1 = LabelFrame(load, bg='dark slate blue')
                Label(load, text=str(p2)).grid(row=0, column=2, pady=(10, 10))
                lbl2 = LabelFrame(load, bg='dark slate blue')
                Label(load, text='NEW MATRIX').grid(row=0, column=4, pady=(10, 10))
                lbl3 = LabelFrame(load, bg='dark slate blue')
                lbl1.grid(row=1, column=0, pady=10, padx=(10, 10))
                Label(load, text='-', bg='royal blue').grid(row=1, column=1, pady=10)
                lbl2.grid(row=1, column=2, pady=10, padx=(10, 10))
                Label(load, text='=', bg='royal blue').grid(row=1, column=3, pady=10)
                lbl3.grid(row=1, column=4, pady=10, padx=(10, 10))

                # displaying matrix
                for i in range(len(allmat[p1])):
                    for j in range(len(allmat[p1][0])):
                        entery = Entry(lbl1, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(allmat[p1][i][j]))
                        entery.configure(state='disabled')

                for i in range(len(allmat[p2])):
                    for j in range(len(allmat[p2][0])):
                        entery = Entry(lbl2, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(allmat[p2][i][j]))
                        entery.configure(state='disabled')

                for i in range(len(allmat[p2])):
                    for j in range(len(allmat[p2][0])):
                        value = int(allmat[p1][i][j]) - int(allmat[p2][i][j])
                        entery = Entry(lbl3, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(value))
                        entery.configure(state='disabled')
            else:
                messagebox.showerror('Critical error!', 'row or column size doesnt matches!')
        elif p1 and p2 not in allmat.keys():
            messagebox.showerror('None existence!', 'one or both matrices doesnt exists!!')

    ok = Button(khol, text='OK', relief=RAISED, command=begin)
    ok.grid(row=3, column=0, columnspan=2, ipadx=10, pady=10)


# function to multiply two matrices
def multmat():
    # adding labels and buttons
    khol = Toplevel()
    khol.configure(bg='green')
    x = Label(khol, text='Name 1 : ')
    title = Label(khol, text='ENTER THE NAMES OF TWO MATRIX YOU WANT TO MULTIPLY', font=("Courier New", 15, "bold"))
    x.grid(row=1, column=0, pady=10)
    title.grid(row=0, column=0, columnspan=2, pady=(4, 10))
    y = Label(khol, text='Name 2 : ')
    y.grid(row=2, column=0, pady=10)
    enter1 = Entry(khol)
    enter1.grid(row=1, column=1)
    enter2 = Entry(khol)
    enter2.grid(row=2, column=1)

    def begin():
        p1 = enter1.get()
        p2 = enter2.get()
        if p1 and p2 in allmat.keys():
            khol.destroy()
            if len(allmat[p1][0]) == len(allmat[p2]):
                load = Toplevel()
                load.configure(bg='royal blue')
                Label(load, text=str(p1)).grid(row=0, column=0, pady=(10, 10))
                lbl1 = LabelFrame(load, bg='dark slate blue')
                Label(load, text=str(p2)).grid(row=0, column=2, pady=(10, 10))
                lbl2 = LabelFrame(load, bg='dark slate blue')
                Label(load, text='NEW MATRIX').grid(row=0, column=4, pady=(10, 10))
                lbl3 = LabelFrame(load, bg='dark slate blue')
                lbl1.grid(row=1, column=0, pady=10, padx=(10, 10))
                Label(load, text='x', bg='royal blue').grid(row=1, column=1, pady=10)
                lbl2.grid(row=1, column=2, pady=10, padx=(10, 10))
                Label(load, text='=', bg='royal blue').grid(row=1, column=3, pady=10)
                lbl3.grid(row=1, column=4, pady=10, padx=(10, 10))

                # displaying matrix
                for i in range(len(allmat[p1])):
                    for j in range(len(allmat[p1][0])):
                        entery = Entry(lbl1, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(allmat[p1][i][j]))
                        entery.configure(state='disabled')

                for i in range(len(allmat[p2])):
                    for j in range(len(allmat[p2][0])):
                        entery = Entry(lbl2, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(allmat[p2][i][j]))
                        entery.configure(state='disabled')

                result = [[0 for i in range(len(allmat[p2][0]))] for j in range(len(allmat[p1]))]
                for k in range(len(allmat[p1])):
                    for l in range(len(allmat[p2][0])):
                        for m in range(len(allmat[p1][0])):
                            result[k][l] = result[k][l] + int(allmat[p1][k][m]) * int(allmat[p2][m][l])
                for i in range(len(allmat[p1])):
                    for j in range(len(allmat[p2][0])):
                        entery = Entry(lbl3, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(result[i][j]))
                        entery.configure(state='disabled')
            else:
                messagebox.showerror("Row column mismatch","Row and column doesn't matches ")
        else:
            messagebox.showerror("None Existence", "One or both matrix doesn't exist!!")

    ok = Button(khol, text='OK', relief=RAISED, command=begin)
    ok.grid(row=3, column=0, columnspan=2, ipadx=10, pady=10)


# function to find the transpose of a matrix
def Transpose():
    khol = Toplevel()
    khol.configure(bg='green')
    x = Label(khol, text='Name of the Matrix : ')
    title = Label(khol, text='ENTER THE NAME OF MATRIX YOU WANT TO FIND THE TRANSPOSE OF : ',
                  font=("Courier New", 15, "bold"))
    x.grid(row=1, column=0, pady=10)
    title.grid(row=0, column=0, columnspan=2, pady=(4, 10))
    enter1 = Entry(khol)
    enter1.grid(row=1, column=1)

    def start():
        p1 = enter1.get()
        if p1 in allmat.keys():
            khol.destroy()
            load = Toplevel()
            load.configure(bg='royal blue')
            Label(load, text=str(p1)).grid(row=0, column=0, pady=(10, 10))
            lbl1 = LabelFrame(load, bg='dark slate blue')
            Label(load, text="Transposed Matrix").grid(row=0, column=2, pady=(10, 10))
            lbl2 = LabelFrame(load, bg='dark slate blue')
            lbl1.grid(row=1, column=0, pady=10, padx=(10, 10))
            lbl2.grid(row=1, column=2, pady=10, padx=(10, 10))
            Label(load, text='=', bg='royal blue').grid(row=1, column=1, pady=10)

            # displaying matrix
            for i in range(len(allmat[p1])):
                for j in range(len(allmat[p1][0])):
                    entery = Entry(lbl1, width=6)
                    entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                    entery.insert(0, str(allmat[p1][i][j]))
                    entery.configure(state='disabled')

            result = [[0 for i in range(len(allmat[p1]))] for j in range(len(allmat[p1][0]))]
            for k in range(len(allmat[p1][0])):
                for m in range(len(allmat[p1])):
                    result[k][m] = allmat[p1][m][k]

            for i in range(len(allmat[p1])):
                for j in range(len(allmat[p1][0])):
                    entery = Entry(lbl2, width=6)
                    entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                    entery.insert(0, str(result[i][j]))
                    entery.configure(state='disabled')
        else:
            messagebox.showerror("None existence","Matrix doesn't exist!")

    ok = Button(khol, text='OK', relief=RAISED, command=start)
    ok.grid(row=3, column=0, columnspan=2, ipadx=10, pady=10)


# function to find if a matrix is symmetric or skew symmetric
def skewmet():
    khol = Toplevel()
    khol.configure(bg='green')
    x = Label(khol, text='Name : ')
    title = Label(khol, text='ENTER THE NAME OF MATRIX : ', font=("Courier New", 15, "bold"))
    x.grid(row=1, column=0, pady=10)
    title.grid(row=0, column=0, columnspan=2, pady=(4, 10))
    enter1 = Entry(khol)
    enter1.grid(row=1, column=1)

    def start():
            p1 = enter1.get()
            if p1 in allmat.keys():
                result = [[0 for i in range(len(allmat[p1]))] for j in range(len(allmat[p1][0]))]
                for i in range(len(allmat[p1][0])):
                    for j in range(len(allmat[p1])):
                        result[i][j] = allmat[p1][j][i]
                    if result[i][j] == (allmat[p1][i][j]):
                        return messagebox.showinfo("Symmetric", "Matrix is symmetric!")
                    elif int(result[i][j]) == -int(allmat[p1][i][j]):
                        return messagebox.showinfo("Skew Symmetric", "Matrix is skew symmetric!")
                    else:
                        return messagebox.showinfo("None", "Neither symmetric nor skew symmetric!")
            else:
                messagebox.showerror("None existence", "Matrix doesn't exist!")
                khol.destroy()


    ok = Button(khol, text='OK', relief=RAISED, command=start)
    ok.grid(row=3, column=0, columnspan=2, ipadx=10, pady=10)


def get_transpose(mat):
    '''function to transpose a matrix and where 'mat' is the name of your matrix'''
    row = len(mat)
    col = len(mat[0])
    result = [[0 for j in range(row)] for i in range(col)]
    for i in range(col):
        for j in range(row):
            result[i][j] = mat[j][i]
    return result

# function to find the minor of a matrix
def getminor(mat, i, j):
    minor = []
    for row in (mat[:i] + mat[i + 1:]):
        minor.append(row[:j] + row[j + 1:])
    return minor


# function to find the determinant of a matrix
def getdet(deter):
    if len(deter) == 1 and len(deter[0]) == 1:
        return int(deter[0][0])
    elif len(deter) == 2 and len(deter[0]) == 2:
        return (int(deter[0][0]) * int(deter[1][1]) - int(deter[0][1]) * int(deter[1][0]))
    elif len(deter) > 2 and len(deter[0]) > 2:
        determinant = 0
        for i in range(1):
            for j in range(len(deter)):
                if (i + j) % 2 == 0:
                    determinant += int(deter[i][j]) * int(getdet(getminor(deter, i, j)))
                elif (i + j) % 2 != 0:
                    determinant -= int(deter[i][j]) * int(getdet(getminor(deter, i, j)))
        return int(determinant)


#functions to get the cofactors of the matrix
def getcofactors(deter, i, j):
    return (-1) ** (i + j) * (getdet(getminor(deter, i, j)))

#function to find the adjoint of matrix
def adjoint(mat):
    row = len(mat)
    col = len(mat[0])
    adj = [[0 for j in range(col)] for i in range(row)]
    for k in range(row):
        for l in range(col):
            adj[k][l] = adj[k][l] + getcofactors(mat, k, l)
    return get_transpose(adj)

"""Here i have defined the function to display the determinant of the matrix graphically on the screen"""

#function to display the determinant of the matrix
def getdet2():
    khol = Toplevel()
    khol.configure(bg='green')
    x = Label(khol, text='Name : ')
    title = Label(khol, text='ENTER THE NAME OF MATRIX : ', font=("Courier New", 15, "bold"))
    x.grid(row=1, column=0, pady=10)
    title.grid(row=0, column=0, columnspan=2, pady=(4, 10))
    enter1 = Entry(khol)
    enter1.grid(row=1, column=1)

    def start():
        p1 = enter1.get()
        if p1 in allmat.keys():
            khol.destroy()
            load = Toplevel()
            load.configure(bg='royal blue')
            Label(load, text=str(p1)).grid(row=0, column=0, pady=(10, 10))
            lbl1 = LabelFrame(load, bg='dark slate blue')
            lbl2 = LabelFrame(load, bg='dark slate blue')
            Label(load, text="Determinant of Matrix").grid(row=0, column=2, pady=(10, 10))
            lbl1.grid(row=1, column=0, pady=10, padx=(10, 10))
            lbl2.grid(row=1, column=2, pady=10, padx=(10, 10))
            Label(load, text='=', bg='royal blue').grid(row=1, column=1, pady=10)

            # displaying matrix
            for i in range(len(allmat[p1])):
                for j in range(len(allmat[p1][0])):
                    entery = Entry(lbl1, width=6)
                    entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                    entery.insert(0, str(allmat[p1][i][j]))
                    entery.configure(state='disabled')

            determinant = getdet(allmat[p1])
            entery = Entry(lbl2, width=6)
            entery.pack()
            entery.insert(0, str(determinant))
            entery.configure(state='disabled')

        else:
            messagebox.showerror("None existence", "Matrix doesn't exist!")
            khol.destroy()


    ok = Button(khol, text='OK', relief=RAISED, command=start)
    ok.grid(row=3, column=0, columnspan=2, ipadx=10, pady=10)


#function to find the adjoint of a matrix and show it graphically
def adjoint_show():
    khol = Toplevel()
    khol.configure(bg='green')
    x = Label(khol, text='Name : ')
    title = Label(khol, text='ENTER THE NAME OF MATRIX YOU WANT TO FIND THE ADJOINT: ', font=("Courier New", 15, "bold"))
    x.grid(row=1, column=0, pady=10)
    title.grid(row=0, column=0, columnspan=2, pady=(4, 10))
    enter1 = Entry(khol)
    enter1.grid(row=1, column=1)

    def start():
        p1 = enter1.get()
        if p1 in allmat.keys():
            khol.destroy()
            load = Toplevel()
            load.configure(bg='royal blue')
            Label(load, text=str(p1)).grid(row=0, column=0, pady=(10, 10))
            lbl1 = LabelFrame(load, bg='dark slate blue')
            lbl2 = LabelFrame(load, bg='dark slate blue')
            Label(load, text="Adjoint of Matrix").grid(row=0, column=2, pady=(10, 10))
            lbl1.grid(row=1, column=0, pady=10, padx=(10, 10))
            lbl2.grid(row=1, column=2, pady=10, padx=(10, 10))
            Label(load, text='=', bg='royal blue').grid(row=1, column=1, pady=10)

            # displaying matrix
            for i in range(len(allmat[p1])):
                for j in range(len(allmat[p1][0])):
                    entery = Entry(lbl1, width=6)
                    entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                    entery.insert(0, str(allmat[p1][i][j]))
                    entery.configure(state='disabled')

            adj = adjoint(allmat[p1])
            for i in range(len(allmat[p1])):
                for j in range(len(allmat[p1][0])):
                        entery = Entry(lbl2, width=6)
                        entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                        entery.insert(0, str(adj[i][j]))
                        entery.configure(state='disabled')
        else:
            messagebox.showerror("None existence", "Matrix doesn't exist!")

    ok = Button(khol, text='OK', relief=RAISED, command=start)
    ok.grid(row=3, column=0, columnspan=2, ipadx=10, pady=10)


#function to find the inverse of a matrix
def getinverse():
    khol = Toplevel()
    khol.configure(bg='green')
    x = Label(khol, text='Name : ')
    title = Label(khol, text='ENTER THE NAME OF MATRIX YOU WANT TO FIND THE INVERSE: ', font=("Courier New", 15, "bold"))
    x.grid(row=1, column=0, pady=10)
    title.grid(row=0, column=0, columnspan=2, pady=(4, 10))
    enter1 = Entry(khol)
    enter1.grid(row=1, column=1)

    def start():
        p1 = enter1.get()
        if p1 in allmat.keys():
            khol.destroy()
            load = Toplevel()
            load.configure(bg='royal blue')
            Label(load, text=str(p1)).grid(row=0, column=0, pady=(10, 10))
            lbl1 = LabelFrame(load, bg='dark slate blue')
            lbl2 = LabelFrame(load, bg='dark slate blue')
            Label(load, text="Inverse of Matrix").grid(row=0, column=2, pady=(10, 10))
            lbl1.grid(row=1, column=0, pady=10, padx=(10, 10))
            lbl2.grid(row=1, column=2, pady=10, padx=(10, 10))
            Label(load, text='=', bg='royal blue').grid(row=1, column=1, pady=10)

            # displaying matrix
            for i in range(len(allmat[p1])):
                for j in range(len(allmat[p1][0])):
                    entery = Entry(lbl1, width=6)
                    entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                    entery.insert(0, str(allmat[p1][i][j]))
                    entery.configure(state='disabled')

            det = getdet(allmat[p1])
            adj = adjoint(allmat[p1])
            if det != 0:
                for i in range(len(adj)):
                    for j in range(len(adj[0])):
                        adj[i][j] = float(adj[i][j] / det)

                for i in range(len(adj)):
                    for j in range(len(adj[0])):
                            entery = Entry(lbl2, width=6)
                            entery.grid(row=i, column=j, ipady=3, ipadx=3, padx=2, pady=2)
                            entery.insert(0, str(adj[i][j]))
                            entery.configure(state='disabled')
            else:
                messagebox.showerror("ERROR!", "Inverse Doesn't Exist!!")
        else:
            messagebox.showerror("None existence", "Matrix doesn't exist!")
            khol.destroy()

    ok = Button(khol, text='OK', relief=RAISED, command=start)
    ok.grid(row=3, column=0, columnspan=2, ipadx=10, pady=10)

def close():
    win.destroy()

"""Here i have defined the buttons that is used in this program """

# creating buttons
create = Button(win, text='1 .Create Matrix', font=("Lucida Calligraphy", 13, "bold"), command=createmat, width=19,
                height=2, fg="white", bg="dark green")
show = Button(win, text='2. Show Matrix', font=("Lucida Calligraphy", 13, "bold"), command=showmat, width=19, height=2,
              fg="white", bg="dark green")
add = Button(win, text='3 .Add Matrices', font=("Lucida Calligraphy", 13, "bold"), command=addmat, width=19, height=2,
             fg="white", bg="dark green")
sub = Button(win, text='4 .Subtract Matrices', font=("Lucida Calligraphy", 13, "bold"), command=sub_mat, width=19,
             height=2, fg="white", bg="dark green")
mult = Button(win, text='5. Multiply Matrices', font=("Lucida Calligraphy", 13, "bold"), command=multmat, width=19,
              height=2, fg="white", bg="dark green")
transpose = Button(win, text='6. Find Transpose', font=("Lucida Calligraphy", 13, "bold"), command=Transpose, width=19,
                   height=2, fg="white", bg="dark green")
skewme = Button(win, text='7. symmetric or Skew symmetric', font=("Lucida Calligraphy", 13, "bold"), command=skewmet,
                width=25, height=2, fg="white", bg="dark green")
det = Button(win, text='8. Determinant of Matrix', font=("Lucida Calligraphy", 13, "bold"), command=getdet2, width=25,
             height=2, fg="white", bg="dark green")

adjoint_button = Button(win, text ='9. Adjoint of Matrix', font=("Lucida Calligraphy", 13, "bold"), command=adjoint_show, width=25,
              height=2, fg="white", bg="dark green")

inverse_button = Button(win, text ='10. Inverse of Matrix', font=("Lucida Calligraphy", 13, "bold"), command=getinverse, width=18,
              height=2, fg="white", bg="dark green")
exit_button = Button(win, text ='11. Exit', font=("Lucida Calligraphy", 13, "bold"), command=close, width=18,
              height=2, fg="white", bg="dark green")


"""here i have defined the canvas buttons of the previous buttons that i have made"""


# creating canvas buttons window

create_window = my_canvas.create_window(100, 400, anchor="nw", window=create)
show_window = my_canvas.create_window(100, 480, anchor="nw", window=show)
add_window = my_canvas.create_window(100, 560, anchor="nw", window=add)
sub_window = my_canvas.create_window(380, 400, anchor="nw", window=sub)
mult_window = my_canvas.create_window(380, 480, anchor="nw", window=mult)
tra_window = my_canvas.create_window(380, 560, anchor="nw", window=transpose)
skewme = my_canvas.create_window(660, 400, anchor="nw", window=skewme)
det_window = my_canvas.create_window(660, 480, anchor="nw", window=det)
get_adjoint = my_canvas.create_window(660, 560, anchor="nw", window=adjoint_button)
get_inverse = my_canvas.create_window(1020, 400, anchor="nw", window=inverse_button)
exit_window = my_canvas.create_window(1020, 480, anchor="nw", window=exit_button)

# putting into mainloop
win.mainloop()
