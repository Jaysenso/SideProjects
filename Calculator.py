import tkinter as tk

window = tk.Tk() 

## Calculate size: 470 x 700 (width x height)
#GUI driver code
outputFrame = tk.Frame(master = window, width = 160, height = 150, bg = "white")
outputFrame.pack(fill = tk.BOTH, expand = True)
inputFrame = tk.Frame(master = window, width = 160, height = 500, bg = "gray")
inputFrame.pack(fill = tk.BOTH, expand = True)


width_size = 10
height_size = 3

#number buttons
button0 = tk.Button(master = inputFrame, text = "0", width = width_size, height = height_size)
button0.grid(row = 5, column = 1 , sticky = "nesw")

button1 = tk.Button(master = inputFrame, text = "1", width = width_size, height = height_size)
button1.grid(row = 4, column = 0, sticky = "nesw")
button2 = tk.Button(master = inputFrame, text = "2", width = width_size, height = height_size)
button2.grid(row = 4, column = 1, sticky = "nesw")
button3 = tk.Button(master = inputFrame, text = "3", width = width_size, height = height_size)
button3.grid(row = 4, column = 2, sticky = "nesw")

button4 = tk.Button(master = inputFrame, text = "4", width = width_size, height = height_size)
button4.grid(row = 3, column = 0, sticky = "nesw")
button5 = tk.Button(master = inputFrame, text = "5", width = width_size, height = height_size)
button5.grid(row = 3, column = 1, sticky = "nesw")
button6 = tk.Button(master = inputFrame, text = "6", width = width_size, height = height_size)
button6.grid(row = 3, column = 2, sticky = "nesw")

button7 = tk.Button(master = inputFrame, text = "7", width = width_size, height = height_size)
button7.grid(row = 2, column = 0, sticky = "nesw")
button8 = tk.Button(master = inputFrame, text = "8", width = width_size, height = height_size)
button8.grid(row = 2, column = 1, sticky = "nesw")
button9 = tk.Button(master = inputFrame, text = "9", width = width_size, height = height_size)
button9.grid(row = 2, column = 2, sticky = "nesw")

#arithmetic buttons
divided = tk.Button(master = inputFrame, text = "÷", width = width_size, height = height_size)
divided.grid(row = 1, column = 3)
multiply = tk.Button(master = inputFrame, text = "x", width = width_size, height = height_size)
multiply.grid(row = 2, column = 3)
minus = tk.Button(master = inputFrame, text = "-", width = width_size, height = height_size)
minus.grid(row = 3, column = 3)
add = tk.Button(master = inputFrame, text = "+", width = width_size, height = height_size)
add.grid(row = 4, column = 3)
equal = tk.Button(master = inputFrame, text = "=", width = width_size, height = height_size)
equal.grid(row = 5, column = 3)

#utility buttons
orButton = tk.Button(master = inputFrame, text = "+/-", width = width_size, height = height_size)
orButton.grid(row = 5, column = 0)
decimal = tk.Button(master = inputFrame, text = ".", width = width_size, height = height_size)
decimal.grid(row = 5, column = 2)

modulo = tk.Button(master = inputFrame, text = "%", width = width_size, height = height_size)
modulo.grid(row = 0, column = 0)
CE = tk.Button(master = inputFrame, text = "CE", width = width_size, height = height_size)
CE.grid(row = 0, column = 1)
C = tk.Button(master = inputFrame, text = "C", width = width_size, height = height_size)
C.grid(row = 0, column = 2)
backSpace = tk.Button(master = inputFrame, text = "Back", width = width_size, height = height_size)
backSpace.grid(row = 0, column = 3)

onedivided = tk.Button(master = inputFrame, text = "1/x", width = width_size, height = height_size)
onedivided.grid(row = 1, column = 0)
square = tk.Button(master = inputFrame, text = "x²", width = width_size, height = height_size)
square.grid(row = 1, column = 1)
squareRoot = tk.Button(master = inputFrame, text = "√", width = width_size, height = height_size)
squareRoot.grid(row = 1, column = 2)


for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(6):
    window.rowconfigure(i, weight=1)

window.mainloop()