from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
from tkinter import messagebox
import numpy as np
# numpy is an open source library for working on multidimensional arrays


root = Tk()
root.title('APNA PROJECT')
#myLabel1=Label(root,text="hello world").grid(row=0,column=0)
root.iconbitmap('C:\project\santa-claus.ico')
# h_img=ImageTk.PhotoImage(Image.open('C:/project/virat.png'))
# ur_label=Label(image=h_img)
# ur_label.grid(row=1,column=0)


root.geometry("400x400")
c = Canvas(root, bg="blue", height=10, width=10)
filename = PhotoImage(file='C:/project/pic.png')
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()

myLabel4 = Label(root, text="Plagiarism Checker PRO the most trustworthy plagiarism",
                 bg="black", fg="white", font=('Urbane', 22))
myLabel4.pack(pady=19)
myLabel5 = Label(root, text="Our mission is to fulfill everyone's NEEDS in plagiarism detection. Most user-friendly interface with plenty of exclusive FEATURES to execute efficiency & reliability mission.",
                 bg="black", fg="white", font=('Roboto', 14))
myLabel5.pack(pady=5)
e1 = Entry(root, font=('Roman 12'), width=40,
           bg="black", fg="white", borderwidth=40)
e1.pack(pady=30)
e1.insert(0, "Enter the path of 1st file:")
e2 = Entry(root, font=('Roman 12'), width=40,
           bg="black", fg="white", borderwidth=40)
e2.pack(pady=30)
e2.insert(1, "Enter the path of 2nd file:")


def myClick():
    global fnum1, fnum2
    fnum1 = e1.get()
    fnum2 = e2.get()
    # print(fnum1)
    # print(fnum2)


myFont = font.Font(family='Roman')
myButton1 = Button(root, text="click me!",
                   command=myClick, fg="red", bg="black")
# myButton1.pack()
myButton1['font'] = myFont
myButton1.pack()
# myButton2 = Button(root, text="click me!",
#                    command=myClick, fg="red", bg="black")
# # myButton2.pack()
# myButton2.pack()
myFont = font.Font(family='Roman')
button_quit = Button(root, text="GO TO RESULT WINDOW",
                     command=root.quit, fg="red", bg="black")
button_quit['font'] = myFont
button_quit.pack(pady=30)
root.mainloop()


# defining a function to compare the strings using levenshtein's algorithm

def levenshtein(sp1, sp2):
    size_x = len(sp1) + 1
    size_y = len(sp2) + 1

  # defining a zero matrix of size of first string * second string
    matrix = np.zeros((size_x, size_y))

    for x in range(size_x):
        matrix[x, 0] = x  # row aray with elements of x
    for y in range(size_y):
        matrix[0, y] = y  # column array with elements of y
    for x in range(1, size_x):
        for y in range(1, size_y):
            if sp1[x-1] == sp2[y-1]:  # if the alphabets at the postion is same
                matrix[x, y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )

            else:         # if the alphabets at the position are different
                matrix[x, y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1] + 1,
                    matrix[x, y-1] + 1
                )

    # returning the levenshtein distance i.e last element of the matrix
    return (matrix[size_x - 1, size_y - 1])


# path2 = input("Enter the path of the first file to scan:\n")
# path3 = input("Enter the path of the second file to scan:\n")
path2 = fnum1
# print(path2)
path3 = fnum2
# print(path3)
with open(path2, 'r') as file:
    data = file.read().replace('\n', '')
    str1 = data.replace(' ', '')

with open(path3, 'r') as file:
    data = file.read().replace('\n', '')
    str2 = data.replace(' ', '')

if (len(str1) > len(str2)):
    length = len(str1)

else:
    length = len(str2)

n = 100-round((levenshtein(str1, str2)/length)*100, 2)

print("\n These two files have ", n, "% similarity")


roott = Toplevel()
roott.title('APNA ANSWER')
roott.iconbitmap('C:\project\santa-claus.ico')
roott.configure(bg="black")


roott.geometry("400x400")
c = Canvas(roott, bg="blue", height=10, width=10)
# Add image file
bg = PhotoImage(file = 'C:/project/moon.png.png')
  
# Show image using label
label1 = Label( roott, image = bg)
label1.place(x=0, y=0, relwidth=1, relheight=1)



myLabel = Label(roott, text=" HELLO DUNIYA HERE'S YOUR ANSWER  ",
                bg="black", fg="yellow", font=('Roman', 24))
myLabel.pack(pady=50)
myLabel45 = Label(roott, text=" 'Plagiarism is one of the great academic sins. It has the power to destroy a scholar or writer and turn a lifetime's work to dust.'  ",
                  bg="black", fg="yellow", font=('Book script', 18))
myLabel45.pack(pady=50)


def myClick():
    h = n
    myLabel = Label(roott, text=str("These two files have "+str(h) +
                    " % " + "similarity"), fg="pink", bg="black", font=('Roman', 24))
    myLabel.pack(pady=20)


myButton = Button(roott, text="click me for answer!",
                  command=myClick, fg="red", bg="black")
myFont = font.Font(family='Roman')
myButton['font'] = myFont
myButton.pack()
button_quit = Button(roott, text="EXIT PROGRAM",
                     command=roott.quit, fg="red", bg="black")
button_quit['font'] = myFont
button_quit.pack(pady=30)

roott.mainloop()
