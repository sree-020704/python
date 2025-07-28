def login():
    username="Bhavya274"
    password="274"
    inp_user=input("enter username:")
    inp_pass=input("enter password:")
    if inp_user==username and inp_pass==password:
        print("login success")
    else:
        print("login failed try again")
login()
