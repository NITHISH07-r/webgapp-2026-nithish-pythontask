import re

common_passwords=["abcd","asdf",";lkj",123,"user","admin","user123",1234567890,9876543210,"admin123"]
special_symbols=["!","@","#","$","%","^","&","*","(",")","()","+","=","{}","{","}","|","]","[","'",";",":","?","/","<",">"]

def check_password_strength(password):
    strength=0
    if password.lower() in common_passwords:
        return "weak password, type any other password"
    
    if any(symbol in password for symbol in special_symbols):
        strength+=5

    if len(password)>8:
        strength+=5

    if re.search(r"[A-Z]",password):
        strength+=5

    if re.search(r"[a-z]",password):
        strength+=5

    if re.search(r"\d",password):
        strength+=5

    if strength >= 18:
        return "your password is strong"
    elif strength < 18 and strength >= 12:
        return "your password is not so strong, I insist u to strengthen your password"
    else:
        return "your password is so weak, so better strengthen your password or it may lead to password theft"

password=input("enter your password: ")
password_strength=check_password_strength(password)
print("\nStrength of the given password: ",password_strength)   
        