from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.geometry("500x500")
root.configure(background = "Black")

label_image = Label(root)
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

img_path = ""

def open_image():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Image File", filetypes=(("Image Files", ".jpg *.gif *.png *.jpeg"),))
    i = Image.open(img_path)
    img_e = ImageTk.PhotoImage(i)
    label_image["image"] = img_e
    img_e.close()

def rotate_image():
    global img_path
    i = Image.open(img_path)
    img_e = ImageTk.PhotoImage(i.rotate(90))
    label_image["image"] = img_e
    img_e.close()

btn = Button(root, font=("serif", 13, "normal"), text="Open Image", bg="gray", fg="white", command=open_image)
btn.place(relx=0.5, rely=0.1, anchor=CENTER)

btn_rotate = Button(root, font=("serif", 13, "normal"), text="Rotate Image", bg="gray", fg="white", command=rotate_image)
btn_rotate.place(relx=0.5, rely=0.9, anchor=CENTER)
root.mainloop()