from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import string
import re
import random
import cv2
from PIL import Image, ImageTk

root = Tk()
root.title('ATM SYSTEM')
root.geometry('600x500+300+200')
root.configure(bg='blue')
root.resizable(False, False)

def signin():
    username = user.get()
    accountno1 = accountno.get()

    if accountno1 == '' or username == '':
        messagebox.showerror("Empty Fields", "Enter the Registered Account_No and Username")
    else:
        conn = sqlite3.connect('ATM_System.db')
        cur = conn.execute('Select * from ATM where accountno="%s" AND user="%s"' % (accountno1, username))

        if cur.fetchone():
            screen = Frame(root, width=400, height=400)
            screen.place(anchor='center', relx=0.5, rely=0.5)

            def generate_otp():
                global generateotp
                generateotp = random.randint(1000, 9999)
                print('Here is your generated OTP:', generateotp)
                return generateotp

            def verify_otp():
                otp1 = otp.get()
                print(otp1)
                if otp1 == "":
                    messagebox.showerror("Empty OTP", "Enter the generated OTP")
                else:
                    if int(otp1) == generateotp:
                        print("Verification successful")
                        messagebox.showinfo("Verification", "Verification Successful")
                        face_detection()
                    else:
                        messagebox.showerror("Wrong OTP", "Please Enter Valid OTP")
                        print("Invalid Otp")

            def face_detection():
                screen.destroy()

                # Capture video from the default camera
                cap = cv2.VideoCapture(0)

                def close_camera():
                    cap.release()
                    options_frame.destroy()

                def deposit():
                    messagebox.showinfo("Deposit", "Deposit option selected")

                def withdraw():
                    messagebox.showinfo("Withdraw", "Withdraw option selected")

                # Create a function to update the video frames
                def update():
                    ret, frame = cap.read()
                    if ret:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                        canvas.create_image(0, 0, anchor=NW, image=photo)
                        canvas.photo = photo
                        canvas.after(10, update)

                options_frame = Frame(root, width=400, height=400)
                options_frame.place(anchor='center', relx=0.5, rely=0.5)

                canvas = Canvas(options_frame, width=400, height=300)
                canvas.pack()

                update()  # Start updating video frames

                Button(options_frame, width=20, pady=7, text='Deposit', bg='#57a1f8', fg='white', border=2,
                       font=('Microsoft YaHei UI Light', 11, 'bold'), command=deposit).place(x=100, y=320)

                Button(options_frame, width=20, pady=7, text='Withdraw', bg='#57a1f8', fg='white', border=2,
                       font=('Microsoft YaHei UI Light', 11, 'bold'), command=withdraw).place(x=100, y=380)

                Button(options_frame, width=20, pady=7, text='Close Camera', bg='#57a1f8', fg='white', border=2,
                       font=('Microsoft YaHei UI Light', 11, 'bold'), command=close_camera).place(x=100, y=440)

            def back():
                screen.destroy()

            Button(screen, width=20, pady=7, text='GENERATE OTP', bg='#57a1f8', fg='white', border=2,
                   font=('Microsoft YaHei UI Light', 11, 'bold'), command=generate_otp).place(x=100, y=80)

            Label(screen, text='ENTER OTP:').place(x=40, y=180)
            otp = Entry(screen, width=25, fg='black', font=('Microsoft YaHei UI Light', 11, 'bold'))
            otp.place(x=110, y=180)

            Button(screen, width=20, pady=7, text='VERIFY OTP', bg='#57a1f8', fg='white', border=2,
                   font=('Microsoft YaHei UI Light', 11, 'bold'), command=verify_otp).place(x=100, y=250)

            global back1
            back1 = Button(screen, width=20, pady=7, text='Back', bg='#57a1f8', fg='white', border=2,
                           font=('Microsoft YaHei UI Light', 11, 'bold'), command=back).place(x=100, y=310)

def signup():
    def signup1():
        username = user.get()
        accountno1 = accountno.get()
        atmpin1 = atmpin.get()
        mobileno1 = mobileno.get()
        email_id = email.get()
        address = address1.get()

        if username == '' or accountno1 == '' or atmpin1 == '' or mobileno1 == '' or email_id == '' or address == '':
            messagebox.showerror("Empty Fields", "All fields are required")
        elif not mobileno1.isdigit() or len(mobileno1) != 10:
            messagebox.showerror("Invalid Mobile Number", "Invalid Mobile Number")
        elif len(accountno1) != 6:
            messagebox.showerror("Invalid Account Number", "Invalid Account Number")
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_id):
            messagebox.showerror("Invalid Email", "Invalid Email")
        else:
            conn = sqlite3.connect('ATM_System.db')
            with conn:
                cur = conn.cursor()
                cur.execute(
                    'CREATE TABLE IF NOT EXISTS ATM (user TEXT, accountno INT, atmpin INT, mobileno INT, email INT, address1 TEXT)')

            cur.execute('INSERT INTO ATM (user,accountno,atmpin,mobileno,email,address1) VALUES(?,?,?,?,?,?)',
                        (username, accountno1, atmpin1, mobileno1, email_id, address))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful")

    frame = Frame(root, width=400, height=400)
    frame.place(anchor='center', relx=0.5, rely=0.5)

    heading = Label(frame, text='REGISTRATION', fg='#57a1f8', font=('Microsoft YaHei UI Light', 25, 'bold'))
    heading.place(x=100, y=10)

    label = Label(frame, text='Username:', font=("bold")).place(x=40, y=80)
    user = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=160, y=80)

    label = Label(frame, text='Account_No:', font=("bold")).place(x=40, y=160)
    accountno = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
    accountno.place(x=160, y=160)

    label = Label(frame, text='User_Id:', font=("bold")).place(x=40, y=120)
    atmpin = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
    atmpin.place(x=160, y=120)

    label = Label(frame, text='Mobile_No:', font=("bold")).place(x=40, y=200)
    mobileno = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
    mobileno.place(x=160, y=200)

    label = Label(frame, text='Email_Id:', font=("bold")).place(x=40, y=240)
    email = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
    email.place(x=160, y=240)

    label = Label(frame, text='Address:', font=("bold")).place(x=40, y=280)
    address1 = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
    address1.place(x=160, y=280)

    Button(frame, width=20, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=1, font=("bold"),
           command=signup1).place(x=100, y=330)

# LOGIN_FRAME
frame = Frame(root, width=400, height=400)
frame.place(anchor='center', relx=0.5, rely=0.5)

heading = Label(frame, text='LOGIN', fg='#57a1f8', font=('Microsoft YaHei UI Light', 40, 'bold'))
heading.place(x=120, y=15)

label = Label(frame, text='Username:', font=("bold")).place(x=40, y=100)
user = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=160, y=100)

label = Label(frame, text='Account_No:', font=("bold")).place(x=40, y=140)
accountno = Entry(frame, width=25, fg='black', border=1, bg="white", font=('Microsoft YaHei UI Light', 11))
accountno.place(x=160, y=140)

Button(frame, width=20, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=2, font=("bold"),
       command=signin).place(x=110, y=200)

label = Label(frame, text="Don't have an account", fg='black', bg='white',
              font=('Microsoft YaHei UI Light', 9, 'bold'))
label.place(x=120, y=330)

sign_up = Button(frame, width=20, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=2, cursor='hand2',
                 font=("bold"), command=signup).place(x=110, y=275)

root.mainloop()
