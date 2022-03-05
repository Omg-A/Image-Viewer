from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.geometry("500x500")
root.configure(background = "snow")

label_image = Label(root, bg="gold2", highlightthickness=5, borderwidth=2, relief=SOLID)
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

img_path = ""

def open_image():
    img_path = filedialog.askopenfilename(title="Open Image File", filetypes=(("Image Files", ".jpg *.gif *.png *.jpeg"),))
    print(img_path)
    img_e = ImageTk.PhotoImage(Image.open(img_path))
    label_image["image"] = img_e

btn = Button(root, font=("sans-serif", 15, "bold"), text="Open Image", bg="gray", fg="white", command=open_image)
btn.place(relx=0.5, rely=0.1, anchor=CENTER)

root.mainloop()