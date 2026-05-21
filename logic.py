users={}

def register_user(e_mail,password):
    if not e_mail or not password:
        return "Empty"
    elif e_mail in users:
        return "Exists"
    users[e_mail]={"password":password, "balance":0}
    return "Registered"

        
def login_user(e_mail,password):
    if not e_mail in users:
        return "No Users"
    elif users[e_mail]["password"] != password:
        return "Wrong Password"
    return "Successful"
    
def deposit_amount(e_mail,amount):
    users[e_mail]["balance"] += amount
    return users[e_mail]["balance"]

def withdraw_amount(e_mail,amount):
    if amount > users[e_mail]["balance"] :
        return "Insufficient Balance"
    users[e_mail]["balance"] -= amount
    return users[e_mail]["balance"]

def check_balance(e_mail):
    return users[e_mail]["balance"]
