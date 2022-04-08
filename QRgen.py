from email.mime import image
from msilib.schema import Font
import qrcode as qr
from tkinter import *
from PIL import Image, ImageTk


#from tkinter import messagebox

root =Tk()
root.title("Create QRCode")
root.geometry('600x350')
c=Canvas(root)
bg=PhotoImage(file="bg.png")
# bg_label=Label(root, image=filename)
# bg_label.place(x=0,y=0)

# lbl1=Label(root, text="Enter your Text / Link:", bg='none' font=('Calibri','10'), foreground='#4FFFC0')
# lbl1.place(x=50,y=50)

def qrc():
    x=con.get()
    y=nam.get()
    feature =qr.QRCode(version=3, box_size=70, border=5)
    feature.add_data(x)
    feature.make(fit=True)

    generate_image = feature.make_image()
    generate_image.save(y)
    #z.config(text="File "+y+" created succesfully")
    c.create_text(200,275, text="File "+y+" created succesfully", font=('Baskerville Old Face','15'), fill='#FA0084')

con=StringVar()
c.create_image(0,0, image=bg, anchor='nw')
c.create_text(130,50, text="Enter Your Content:",fill="#00FFA4", font=('Monotype Corsiva',20, 'bold'))
content=Entry(root, text="Enter here", font=("arial",'10'), bd='1', width='46', bg='#DAFFF2', textvariable=con)
content.place(x=245,y=43)

nam=StringVar()
c.create_text(130,100, text="Enter Your File Name:",fill="#00FFA4", font=('Monotype Corsiva',20, 'bold'))
content=Entry(root, text="File Name", font=("arial",'10'), bd='1', width='45', bg='#DAFFF2', textvariable=nam)
content.place(x=253,y=93)

# z=Label(root, font=('Baskerville Old Face','15'), foreground='red')
# z.place(x=200, y=270)

btn=Button(root, text="Create QR", bg='#BA4FFF', font=('forte','20'),command=qrc)
btn.place(x=300, y=200)









c.pack(fill="both", expand=True)
root.mainloop()