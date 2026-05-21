from tkinter import*
from PIL import Image, ImageTk
from tkinter import colorchooser
from tkinter import messagebox
from logic import *

top=Tk()
top.title("Online Banking Application")
top.geometry("1275x645")

# Background theme
path=Image.open("Digital Banking Virtual Bank.jfif")
path=path.resize((1275,645))
bg_img=ImageTk.PhotoImage(path)

#global_variables
current_user={}
login_attempts=0

#Functions for back_buttons 
def open_login():
    home_frame.place_forget()
    login_frame.place(x=0, y=0, relwidth=1, relheight=1)

def open_register():
    home_frame.place_forget()
    register_frame.place(x=0, y=0, relwidth=1, relheight=1)

def back_home():
    register_frame.place_forget()
    login_frame.place_forget()
    account_frame.place_forget()
    deposit_frame.place_forget()
    withdraw_frame.place_forget()
    show_balance_frame.place_forget()
    home_frame.place(x=0,y=0,relwidth=1,relheight=1)

def back_options():
    register_frame.place_forget()
    login_frame.place_forget()
    deposit_frame.place_forget()
    withdraw_frame.place_forget()
    show_balance_frame.place_forget()
    home_frame.place_forget()
    account_frame.place(x=0,y=0,relheight=1,relwidth=1)
    
def open_account():
    home_frame.place_forget()
    register_frame.place_forget()
    login_frame.place_forget()
    account_frame.place(x=0, y=0, relwidth=1, relheight=1)
    
def open_balance():
    home_frame.place_forget()
    register_frame.place_forget()
    login_frame.place_forget()
    account_frame.place_forget()
    show_balance_frame.place(x=0,y=0,relheight=1,relwidth=1)
    
def open_deposit():
    home_frame.place_forget()
    register_frame.place_forget()
    login_frame.place_forget()
    account_frame.place_forget()
    deposit_frame.place(x=0,y=0,relheight=1,relwidth=1)
    
def open_withdraw():
    home_frame.place_forget()
    register_frame.place_forget()
    login_frame.place_forget()
    account_frame.place_forget()
    deposit_frame.place_forget()
    withdraw_frame.place(x=0,y=0,relheight=1,relwidth=1)
# Functons for Authentication

def register():
    global current_user
    user_name=username_entry.get()
    dob=dob_entry.get()
    register_e_mail=register_email_entry.get()
    gender_value=gender.get()
    state=state_entry.get()
    city=city_entry.get()
    mob_no=mob_no_entry.get()
    
    register_password1=register_password1_entry.get()
    register_password2=register_password2_entry.get()
    
    if not all([user_name,dob,gender_value,mob_no,city,state]):
        messagebox.showerror("Error","All fields are required")
        return "Invalid"
    elif not user_name.isalnum() :
        messagebox.showerror("Error","Username must contains only letters and numbers")
        return "Invalid"
    elif len(user_name) < 4:
        messagebox.showerror("Error", "Username must have at least 4 characters")
        return "Invalid"
        
    elif "@" not in register_e_mail or "." not in register_e_mail:
        messagebox.showerror("Error","Invalid E-mail")
        return "Invalid"
    
    elif  not mob_no.isdigit() or len(mob_no) !=10:
        messagebox.showerror("Error","Enter valid mobile Number")
        return "Invalid"
    
    elif len(register_password1)<6:
        messagebox.showerror("Error","Password must be at least 6 characters")
        return "Invalid"
    elif len(register_password2) ==0:
        messagebox.showerror("Error","Enter password again")
        return "Invalid"
    
    elif register_password1 != register_password2:
        messagebox.showerror("Error","password mismatched")
        return "Invalid"  
    
    result = register_user(register_email_entry.get(), register_password1_entry.get())

    if result == "Registered":
        messagebox.showinfo("Success", "User Registered")
        current_user=register_e_mail
    elif result == "Exists":
        messagebox.showerror("Error", "User already exists")
    else:
        messagebox.showwarning("Warning", "Fill all fields")
    return result

def login():
    global current_user
    global login_attempts
    
    login_e_mail=login_email_entry.get()
    login_password=login_password_entry.get()
    
    
    if not login_e_mail or not login_password:
        messagebox.showerror("Error","All Fields Required")
        return "Invalid"
    
    elif "@" not in login_e_mail or "." not in login_e_mail:
        messagebox.showerror("Error","Invalid E-mail")
        return "Invalid"
    
    elif len(login_password) < 6:
        messagebox.showerror("Error","Password must be more than 6 characters")
        return "Invalid"
    
    
    result=login_user(login_e_mail,login_password)
    
    if result=="No Users":
        messagebox.showerror("Error","User not Found")
        
    elif result=="Wrong Password":
        login_attempts +=1
        
        remaining = 3 - login_attempts
        
        if remaining > 0 :
            messagebox.showerror("Error", f" Wrong Password \n Attempts remaining :{remaining}")
        else :
            messagebox.showerror("Error", f"Account Blocked \n Maximum login attempts reached")
            login_button.config(state=DISABLED)
            
            
    else:
        messagebox.showinfo("Success","Successfully Login")
        current_user=login_e_mail
        login_attempts=0
    return result
 
def register_and_open():
    result = register()  

    if result == "Registered":
        open_account()   
        
def login_and_open():
    result=login()
    
    if result=="Successful":
        open_account()
        
def login_toggle_password():
    
    if login_password_entry.cget('show')=="*":
        login_password_entry.configure(show='')
        eye_button.config(image=closed_eye)
    else:
        login_password_entry.configure(show='*')
        eye_button.config(image=open_eye)
        
# Functions for Password visibility        
def reg_toggle_password1():
     
    if register_password1_entry.cget('show')=="*" :
        
        register_password1_entry.configure(show='')
        reg_eye_button1.config(image=closed_eye)

    else:    
        register_password1_entry.configure(show="*")
        reg_eye_button1.config(image=open_eye)
        
def reg_toggle_password2():
    
    if register_password2_entry.cget('show')=="*": 
        register_password2_entry.configure(show='')
        reg_eye_button2.config(image=closed_eye)
    else:
        register_password2_entry.configure(show="*")
        reg_eye_button2.config(image=open_eye)

#Functions for transactions
def deposit_money():
    
    amount=deposit_amount_entry.get()
    
    if not amount.isdigit():
        messagebox.showerror("Error","Enter only numbers")
        return 
    
    new_balance=deposit_amount(current_user,int(amount))
    
    messagebox.showinfo("Success",f'Amount Rs.{int(amount)} Successfully Credited .\n Current Balance : {new_balance}')

def withdraw_money():
    
    amount = withdraw_amount_entry.get()
    
    if not amount.isdigit():
        messagebox.showerror("Error","Enter only numbers")
        return
    result=withdraw_amount(current_user,int(amount))
    
    if result=="Insufficient Balance":
        messagebox.showerror("Error","Insufficient Balance")
    else:
        messagebox.showinfo("Success",f'Amount Rs. {int(amount)} Successfully Debited . \n Current Balance :{result}')

def show_balance():
    
    balance=check_balance(current_user)
    
    balance_display.config(
        text=f"Current Balance : ₹{balance}")
    
#Home Frame
home_frame=Frame(top)
home_frame.place(x=0, y=0, relwidth=1, relheight=1)
bg_label=Label(home_frame,image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image=bg_img

sign_in_label=Label(home_frame,text=' Already Have Account ?',width=20,font=('bold',12)).place(x=10,y=100)
sign_in_button=Button(home_frame,text='Sign In',width=20,font=('bold',10),
                      activebackground="#FBFF00",command=open_login)
sign_in_button.place(x=230,y=100)
signup_label=Label(home_frame,text='Create New Account',width=20,font=('bold',12)).place(x=10,y=150)
signup_button=Button(home_frame,text='Register',width=20,font=('bold',10),activebackground="#3E4344",
                     command=open_register)
signup_button.place(x=230,y=150)

#Login Frame
login_frame=Frame(top)
login_frame.configure(bg="#4986F8")
login_label=Label(login_frame,text=' Sign In to Your Account ',width=30,font=('arial',15),bg='#4986F8').place(x=330,y=90)
email_label=Label(login_frame,text=' E_mail ',width=15,font=('plain',12)).place(x=300,y=150)
login_email_entry=Entry(login_frame, width=30,font=('plain',12))
login_email_entry.place(x=500,y=150)
password_label=Label(login_frame,text=' Password ',width=15,font=('plain',12)).place(x=300,y=190)
login_password_entry=Entry(login_frame, width=45,show='*')
login_password_entry.place(x=500,y=190)
login_button=Button(login_frame,text='Login',width=20,font=('bold',10),
                    activebackground="#FBFF00",command=login_and_open)
login_button.place(x=450,y=260)
back_button=Button(login_frame,text=' ⬅ Back',width=10,font=('bold',10),
                   activebackground="#3E4344",command=back_home)
back_button.place(x=10,y=20)

open_eye = PhotoImage(file="open_eye.png")
closed_eye = PhotoImage(file="closed_eye.png")
eye_button=Button(login_frame,image=open_eye,bg="#4986F8", activebackground="#4986F8",bd=0,command=login_toggle_password)
eye_button.place(x=780, y=185)

#Register Frame
register_frame=Frame(top)
register_frame.configure(bg="#4986F8")
back_button=Button(register_frame,text=' ⬅ Back',width=10,font=('bold',10),activebackground="#3E4344",
                   command=back_home)
back_button.place(x=10,y=20)
username_label=Label(register_frame,text=' UserName ',width=15,font=('plain',12)).place(x=300,y=150)
username_entry=Entry(register_frame, width=30,font=('plain',12))
username_entry.place(x=500,y=150)
register_email_label=Label(register_frame,text=' Email Id ',width=15,font=('plain',12)).place(x=300,y=190)
register_email_entry=Entry(register_frame, width=30,font=('plain',12))
register_email_entry.place(x=500,y=190)
dob_label=Label(register_frame,text=' Date of Birth ',width=15,font=('plain',12)).place(x=300,y=230)
dob_entry=Entry(register_frame, width=30,font=('plain',12))
dob_entry.place(x=500,y=230)
gender_label=Label(register_frame,text=' Gender ',width=15,font=('plain',12)).place(x=300,y=270)

gender=StringVar()
Radiobutton(register_frame, text="Male", variable=gender, value="Male",font=('plain',11)).place(x=500,y=270)
Radiobutton(register_frame, text="Female", variable=gender, value="Female",font=('plain',11)).place(x=580,y=270)
Radiobutton(register_frame, text="Others", variable=gender, value="Others",font=('plain',11)).place(x=680,y=270)

mob_no_label=Label(register_frame,text=' Mobile Number ',width=15,font=('plain',12)).place(x=300,y=310)
mob_no_entry=Entry(register_frame, width=30,font=('plain',12))
mob_no_entry.place(x=500,y=310)
city_label=Label(register_frame,text=' City ',width=15,font=('plain',12)).place(x=300,y=350)
city_entry=Entry(register_frame, width=30,font=('plain',12))
city_entry.place(x=500,y=350)
state_label=Label(register_frame,text=' State ',width=15,font=('plain',12)).place(x=300,y=390)
state_entry=Entry(register_frame, width=30,font=('plain',12))
state_entry.place(x=500,y=390)
register_password1_label=Label(register_frame,text=' Password ',width=15,font=('plain',12)).place(x=300,y=430)
register_password1_entry=Entry(register_frame, width=45,show='*')
register_password1_entry.place(x=500,y=430)
register_password2_label=Label(register_frame,text='Confirm Password ',width=15,font=('plain',12)).place(x=300,y=470)
register_password2_entry=Entry(register_frame, width=45,show='*')
register_password2_entry.place(x=500,y=470)
login_label=Label(register_frame,text=' New Account Registration  ',width=30,font=('arial',17),bg='#4986F8').place(x=330,y=90)


submit_button=Button(register_frame,text='Submit',width=20,font=('bold',10),
                     activebackground="#FBFF00",command=register_and_open)
submit_button.place(x=430,y=510)


reg_eye_button1=Button(register_frame,image=open_eye,bg="#4986F8", 
                       activebackground="#4986F8",bd=0 , command=reg_toggle_password1)
reg_eye_button1.place(x=780, y=430)
reg_eye_button2=Button(register_frame,image=open_eye,bg="#4986F8", 
                       activebackground="#4986F8",bd=0 , command=reg_toggle_password2)
reg_eye_button2.place(x=780, y=470)

#Account Frame
account_frame=Frame(top)
account_frame.configure(bg="#4986F8")
instr_label=Label(account_frame,text=" Select  Your  transaction  Option",
                  font=('Terminal',25),bg="#4986F8",).place(x=250,y=150)

back_button=Button(account_frame,text=' ⬅ Back',width=10,font=('bold',10),activebackground="#3E4344",
                   command=back_home)
back_button.place(x=10,y=20)

balance_button=Button(account_frame, text="Check Balance",font=("bold",10),
                            width=15,activebackground='yellow',activeforeground="black",
                            command=lambda:[open_balance(),show_balance()])
balance_button.place(x=140,y=460)
deposit_button=Button(account_frame, text="Deposit",font=("bold",10),
                            width=15,activebackground='yellow',activeforeground="black",command=open_deposit)
deposit_button.place(x=530,y=460)
withdraw_button=Button(account_frame, text="Withdraw",font=("bold",10),width=15,activebackground='yellow',
                          activeforeground="black",command=open_withdraw)
withdraw_button.place(x=930,y=460)

path=Image.open("balance.png")
balance_img=ImageTk.PhotoImage(path)
balance_label=Label(account_frame,image=balance_img)
balance_label.configure(bg="#4986F8")
balance_label.place(x=150, y=350)
balance_label.image=balance_img

path=Image.open("deposit.png")
deposit_img=ImageTk.PhotoImage(path)
deposit_label=Label(account_frame,image=deposit_img)
deposit_label.configure(bg="#4986F8")
deposit_label.place(x=550, y=350)
deposit_label.image=deposit_img

path=Image.open("withdraw.png")
withdraw_img=ImageTk.PhotoImage(path)
withdraw_label=Label(account_frame,image=withdraw_img)
withdraw_label.configure(bg="#4986F8")
withdraw_label.place(x=950, y=350)
withdraw_label.image=withdraw_img

#Transaction Frames
#deposit frame
deposit_frame=Frame(top)
deposit_frame.configure(bg="#4986F8")
amount_label1=Label(deposit_frame,text=" Enter Amount ",font=("Courier",25),bg="#4986F8").place(x=450,y=100)
amount_entry1=Entry(deposit_frame,font=("Courier",25),width=18,bg="#4986F8")
rs_label1=Label(deposit_frame,text=" Rs .",font=("Courier",25),bg="#4986F8").place(x=360,y=200)
deposit_amount_entry=Entry(deposit_frame,font=("Courier",20),bg="#4986F8")
deposit_amount_entry.place(x=470,y=200)
deposit_confirm_button=Button(deposit_frame,text=" Confirm ",font=('bold',12),
                      width=10,activebackground='yellow' , command=deposit_money)
deposit_confirm_button.place(x=550,y=300)
back_button=Button(deposit_frame,text=' ⬅ Back',width=10,font=('bold',10),
                   activebackground="#5C5C4F",command=back_options)
back_button.place(x=10,y=20)

#withdraw frame
withdraw_frame=Frame(top)
withdraw_frame.configure(bg="#4986F8")
amount_label2=Label(withdraw_frame,text=" Enter Amount ",font=("Courier",25),bg="#4986F8").place(x=450,y=100)
amount_entry2=Entry(withdraw_frame,font=("Courier",25),width=18,bg="#4986F8")
rs_label2=Label(withdraw_frame,text=" Rs .",font=("Courier",25),bg="#4986F8").place(x=360,y=200)
withdraw_amount_entry=Entry(withdraw_frame,font=("Courier",20),bg="#4986F8")
withdraw_amount_entry.place(x=470,y=200)
withdraw_confirm_button=Button(withdraw_frame,text=" Confirm ",font=('bold',12),
                      width=10,activebackground='yellow' , command=withdraw_money)
withdraw_confirm_button.place(x=550,y=300)
back_button=Button(withdraw_frame,text=' ⬅ Back',width=10,font=('bold',10),activebackground="#3E4344",
                   command=back_options)
back_button.place(x=10,y=20)

#show_balance frame

show_balance_frame=Frame(top)
show_balance_frame.configure(bg="#4986F8")
back_button=Button(show_balance_frame,text=' ⬅ Back',width=10,font=('bold',10),
                   activebackground="#5C5C4F",command=back_options)
back_button.place(x=10,y=20)
balance_display = Label(
    show_balance_frame,text="Current Balance : \n\n   ₹0",font=('Arial',16),bg="#4986F8",fg="white")
balance_display.place(x=450,y=300)


top.mainloop()
