from tkinter import *
from tkinter import messagebox
from PIL import ImageTk #pip install Pillow
import pymysql #pip install pymysql

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #=== Bg image ===
        self.bg = ImageTk.PhotoImage(file="images/bg_signup.png")
        bg = Label(self.root,image = self.bg).place(x=0,y=0)

        title = Label(bg, text = "Sign Up", font=("Quicksand",28,"bold"),bg="#FFEAE7",fg="black").place(x=930, y=55)

        name = Label(bg, text = "Name", font=("Quicksand",18),bg="#FFEAE7",fg="black").place(x=817, y=140)
        self.txt_name = Entry(bg, font=("Quicksand",18),bg="#FFFFFF")
        self.txt_name.place(x=819, y=185,width=320)

        email = Label(bg, text = "Email", font=("Quicksand",18),bg="#FFEAE7",fg="black").place(x=817, y=230)
        self.txt_email = Entry(bg, font=("Quicksand",18),bg="#FFFFFF")
        self.txt_email.place(x=819, y=275,width=320)

        username = Label(bg, text = "Username", font=("Quicksand",18),bg="#FFEAE7",fg="black").place(x=817, y=320)
        self.txt_username = Entry(bg, font=("Quicksand",18),bg="#FFFFFF")
        self.txt_username.place(x=819, y=365,width=320)

        password = Label(bg, text = "Password", font=("Quicksand",18),bg="#FFEAE7",fg="black").place(x=817, y=410)
        self.txt_password = Entry(bg, font=("Quicksand",18),bg="#FFFFFF")
        self.txt_password.place(x=819, y=455,width=320)

        self.btn_su_image = ImageTk.PhotoImage(file = "images/signup.png")
        btn_su = Button(bg, image=self.btn_su_image, bg="#FFEAE7", bd=0, cursor="hand2", command=lambda: register_data(self.txt_name, self.txt_email, self.txt_username, self.txt_password)).place(x=800, y=540)

        self.btn_lo_image = ImageTk.PhotoImage(file = "images/login.png")
        btn_lo = Button(bg, image=self.btn_lo_image, bg="#FFEAE7", bd=0, cursor="hand2", command=lambda: login_window()).place(x=1000, y=540)   

root = Tk()
Register(root)

def login_window():
    root.destroy()
    import login_db 

def register_data(txt_name, txt_email, txt_username, txt_password):
    if txt_name.get()=="" or txt_email.get()=="" or txt_username.get()=="" or txt_password.get()=="":
        messagebox.showerror("Error", "All Fields are Required", parent=root)
    else:
        try:
            con = pymysql.connect(host="localhost",user="root",password="",database="account")
            cur = con.cursor()
            cur.execute("select * from account where username=%s",txt_username.get())
            us = cur.fetchone()
            if us!=None:
                messagebox.showerror("Error", "Username Already Exist, Please Try with Another Username", parent=root)
            else :
                cur.execute("insert into account (username, password, nama, email) values (%s, %s, %s, %s)",
                                (txt_username.get(),
                                txt_password.get(),
                                txt_name.get(),
                                txt_email.get()
                                ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Register Successful", parent=root)
                root.destroy()
                import login_db
        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root)

obj = Register(root)
root.mainloop()