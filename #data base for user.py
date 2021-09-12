#data base for user
name = "AbdelRahman Salah" 
passcode ="123042135"
username=input("your username please ")
password=input("your password please ")
if username == name:
    if password == passcode:
        print("welcome Mestar",name)
    else:
        print("your password isn't correct,please enter it again")
else:
    print("please enter your name correctly")        