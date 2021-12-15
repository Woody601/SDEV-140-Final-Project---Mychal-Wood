
# This file was generated by the Tkinter Designer by Parth Jadhav
# This then was heavily modified and altered by Mychal Wood.

from pathlib import Path
from tkinter import *
from PIL import ImageTk, Image
# Explicit imports to satisfy Flake8
import tkinter.messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# This is the information generated by the Tkinter designer to make it easier, to direct it to the assets folder.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Indy Laser Designs")
window.geometry("1920x800")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

# This is just a list to store some information about the product (the tumbler cup in this instance), I hope to maybe implement this in a database possibly if I get the time to have the product colors that are available be there, so that way it is easier to manage.
productinfo = {'Product Name': ['20 OZ RINGNECK TUMBLER'], 'Price': ['$20'], 'Colors': ['coral', 'red', 'maroon', 'orange', 'yellow', 'green', 'teal', 'lightblue', 'royalblue', 'navyblue', 'lightpurple', 'purple', 'pink', 'white', 'stainlesssteel', 'darkgrey', 'black']}

# This function makes it a whole lot easier to make and place down buttons, so that way it doesn't take up as much space as it normally would.
def placebutton(buttonimage, positionx, positiony, width, height, command= '', borderwidth=0, highlightthickness=0, relief="flat"):
    buttonplace = Button(
        image = buttonimage,
        borderwidth = borderwidth,
        highlightthickness = highlightthickness,
        command = command,
        relief = relief
    )
    buttonplace.place(
        x = positionx,
        y = positiony,
        width = width,
        height = height
    )

# Sets the customize button image.
customizebuttonimage = Image.open(relative_to_assets("customizebutton.png"))
customizebuttonimage = customizebuttonimage.resize((110, 60), Image.ANTIALIAS)
# The code above makes it to where I'm able to resize the image to the size I'd like it to be on the page, and then the code below makes it an actual PhotoImage.
customizebuttonimage = ImageTk.PhotoImage(customizebuttonimage)
# Sets the exit button image.
exitbuttonimage = Image.open(relative_to_assets("exitbutton.png"))
exitbuttonimage = exitbuttonimage.resize((66, 33), Image.ANTIALIAS)
# The code above makes it to where I'm able to resize the image to the size I'd like it to be on the page, and then the code below makes it an actual PhotoImage.
exitbuttonimage = ImageTk.PhotoImage(exitbuttonimage)



# This code makes all of the variables to store the images for the different colors of cups, so that the program can call them and swap them out when a color button is pressed.
for availablecolors in productinfo["Colors"]:
# The temporaryvariable is to create the name for the variable that can be referred to in the future. For example: when looping through the list of available colors, if the color is on red, the variable will be made into redcupimage.
# When it comes to the button color variables, it works the same way that it does for the cup photos, except it makes it into the (color)buttonimage, for example, red would be 'redbuttonimage', and can be called later on in the code by the buttons.
    temporaryvariable = availablecolors + "cupimage"
    globals()[temporaryvariable] = Image.open(relative_to_assets(str(availablecolors + ".png")))
    globals()[temporaryvariable] = globals()[temporaryvariable].resize((318, 318), Image.ANTIALIAS)
    globals()[temporaryvariable] = ImageTk.PhotoImage(globals()[temporaryvariable])
    temporaryvariable = availablecolors + "buttonimage"
    globals()[temporaryvariable] = Image.open(relative_to_assets(str(availablecolors + "button.png")))
    globals()[temporaryvariable] = globals()[temporaryvariable].resize((22, 22), Image.ANTIALIAS)
    globals()[temporaryvariable] = ImageTk.PhotoImage(globals()[temporaryvariable])
    del temporaryvariable

# This changecupcolor(color) is the command to change the color of the product, or the cup in this instance, which will modify the image that is directly on the product tile.
# The if statements are to make the text for the Product tile that updates after the user clicks the button to change the color.
def changecupcolor(color):
    canvas.itemconfig(productphoto,image=globals()[str(color + "cupimage")])
    if color == "coral":
        canvas.itemconfig(productcolor, text = "Coral")
    if color == "red":
        canvas.itemconfig(productcolor, text = "Red")
    if color == "maroon":
        canvas.itemconfig(productcolor, text = "Maroon")
    if color == "orange":
        canvas.itemconfig(productcolor, text = "Orange")
    if color == "yellow":
        canvas.itemconfig(productcolor, text = "Yellow")
    if color == "green":
        canvas.itemconfig(productcolor, text = "Green")
    if color == "teal":
        canvas.itemconfig(productcolor, text = "Teal")
    if color == "lightblue":
        canvas.itemconfig(productcolor, text = "Light Blue")
    if color == "royalblue":
        canvas.itemconfig(productcolor, text = "Royal Blue")
    if color == "navyblue":
        canvas.itemconfig(productcolor, text = "Navy Blue")
    if color == "lightpurple":
        canvas.itemconfig(productcolor, text = "Light Purple")
    if color == "purple":
        canvas.itemconfig(productcolor, text = "Purple")
    if color == "pink":
        canvas.itemconfig(productcolor, text = "Pink")
    if color == "white":
        canvas.itemconfig(productcolor, text = "White")
    if color == "stainlesssteel":
        canvas.itemconfig(productcolor, text = "Stainless Steel")
    if color == "darkgrey":
        canvas.itemconfig(productcolor, text = "Dark Grey")
    if color == "black":
        canvas.itemconfig(productcolor, text = "Black")

# This colorbuttons is to generate the buttons that are available in the list of colors for the cup.
def colorbuttons(buttonx, buttony):
    numcolorbuttons = 0 
    for color in productinfo["Colors"]:
        numcolorbuttons += 1
        if numcolorbuttons == 1: # This is to set the position of the first color button, so that the ones after it are spaced evenly on the same line and level as the first one.
            currentxpos = buttonx+106
            currentypos = buttony+524
        elif not numcolorbuttons == 10: # This is to make sure that there is only 10 colored buttons in a row on the product tile. If there are not 10, it will continue to proportionally space them out on the product tile.
            currentxpos = currentxpos + 37
        elif numcolorbuttons == 10: # This only runs if there are not already 10 buttons placed down.
            currentxpos = buttonx + 106
            currentypos = currentypos + 40
        placecolorbutton(color, currentxpos, currentypos)

# This will take the colors based on the ones available from the list of available colors, and then determine based on the color, which color will do what. For example, if the color red is in the list of available colors, it will make the red color, with the red button color image as the image of the button, and on click will change the color of the cup to red. All the other colors function the exact same way, just with their respective color.
def placecolorbutton(color, currentxpos, currentypos):
    if color == "coral":
        placebutton(coralbuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "red":
        placebutton(redbuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "maroon":
        placebutton(maroonbuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "orange":
        placebutton(orangebuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "yellow":
        placebutton(yellowbuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "green":
        placebutton(greenbuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "teal":
        placebutton(tealbuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "lightblue":
        placebutton(lightbluebuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "royalblue":
        placebutton(royalbluebuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "navyblue":
        placebutton(navybluebuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "lightpurple":
        placebutton(lightpurplebuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "purple":
        placebutton(purplebuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "pink":
        placebutton(pinkbuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "white":
        placebutton(whitebuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "stainlesssteel":
        placebutton(stainlesssteelbuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "darkgrey":
        placebutton(darkgreybuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))
    if color == "black":
        placebutton(blackbuttonimage, currentxpos, currentypos, 22, 22, command=lambda:changecupcolor(color))

# This makes the product tile, with the product image, the title of the product, the colors available, and the button to customize the product (the cup in this instance). The only issue for the moment is that when there are multiple tiles placed out, the buttons on the first and second one only change the image on the second tile, if there two tiles placed down for example. So what I want to maybe figure out if I get the time (not that it would be useful for me, maybe in the future if I continue on this project in another SDEV class, I forget which one is the Python one). 
def createproducttile(productname, productpic, positionx, positiony, backgroundcolor):
    Font_tuple = ("Roboto", 20) # This does not properly set the font correctly, which I would like it to. 
    canvas.create_rectangle(
        positionx, # X Position
        positiony, # Y Position
        642.0,
        781.0,
        fill=backgroundcolor,
        outline="black")
    canvas.create_text(
        positionx + 30, # X Position of the Text
        positiony + 30, # Y Position of the Text
        anchor="nw",
        text= productname,
        fill="#000000",
        font=Font_tuple
        )
    global productphoto
    productphoto = canvas.create_image(
        positionx+265,
        positiony+318,
        image=productpic
        )
    global productcolor
    productcolor = canvas.create_text(
        218.0,
        665.0,
        anchor="nw",
        text="Red",
        fill="#000000",
        font=("Roboto", 12 * -1)
      )
    # This puts down the color buttons and the button that says customize, but isn't yet working yet.
    placebutton(customizebuttonimage, positionx+420, positiony+650, 110.0, 60.0, command=lambda:tkinter.messagebox.showinfo("",  "Sorry, but the customizer is not ready quite yet. Please check back in the future."))
    colorbuttons(positionx, positiony)
# This creates the top bar, along with the exit button at the top.
canvas.create_rectangle(0.0, 0.0, 1920.0, 50.0, fill="#C4C4C4", outline="")
placebutton(exitbuttonimage, 1846, 9, 66, 33, command=window.destroy)

# This puts down a product tile, with the title of it, and the image of the cup. For the future, I need to change this and make it a class, so that way I can better manage and control it.
createproducttile('20 OZ RINGNECK TUMBLER', redcupimage, 112, 70, "white")

window.mainloop()