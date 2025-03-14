# Main project file
import tkinter
from PIL import Image, ImageTk

# Define constants
# Define fonts and colors
black = "#010101"
project_image = "./images/DME.png"
project_icon = "./images/DME.ico"

# Define window
root = tkinter.Tk()
root.title("DME")
#root.iconbitmap(project_icon)   #It doesn't worked in Linux, but it worked for Windows
root.geometry("600x600")
root.resizable(0,0)
root.config(bg=black)

# Define GUI Layout
# Create Canva
canvas = tkinter.Canvas(root, width=600, height=600)
canvas.pack()

image = ImageTk.PhotoImage(Image.open(project_image).resize((600,600), Image.Resampling.LANCZOS))

canvas.backgroud = image
bg = canvas.create_image(0, 0, anchor=tkinter.NW, image=image)

root.after(2500, root.destroy)
root.mainloop()

if True:
    import login


