#from tkinter import Tk
#from tkinter.filedialog import askopenfilename
from PIL import Image
import sys
import pyperclip
import time

PLAYER = (14, 215, 237, 255) #0ed7ed
END = (66, 245, 75, 255)     #42f54b
LAVA = (245, 87, 66, 255)    #f55742
WALL = (0, 0, 0, 255)        #000000

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
def openi(filename):
    image = Image.open(filename)
    x = 0
    y = 0
    output = []
    tempstring = ""
    for i in range(10):
        for j in range(14):
            color = image.getpixel((x, y))
            if color == PLAYER:
                tempstring = tempstring+"S"
            if color == END:
                tempstring = tempstring+" "
            if color == LAVA:
                tempstring = tempstring+"L"
            if color == WALL:
                tempstring = tempstring+"W"
            x+=1
        output.append(tempstring)
        tempstring = ""
        x=0
        y+=1
    pyperclip.copy(str(output).replace(", ", ",\n"))
    print(str(output).replace(", ", ",\n"))
a = str(sys.argv[1])
openi(a)
print("Copied to clipboard")
time.sleep(2)
