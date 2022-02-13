import re
#simple regex expression for email checking  
pattern =r"([\w\.-]+)@([\w\.-]+)([\w\.-]+)"
email=input("enter your email:")
if re.search(pattern,email):
    print(email)
else:
    print('yor email is incorrect')

Hiii testing
