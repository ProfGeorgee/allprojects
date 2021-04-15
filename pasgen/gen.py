import random
s = int(input("enter how many digits you want ur number to be: "))

p = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

def listtostring(s):
    str1 = ""

    for list in s:
        str1 += list

    return str1

if s >= 75:
    print("password is to big input a smaller number")
    
elif s <= 0:
    print("password cant be 0 or negative")

else:
    print("ur pass is :",listtostring(random.sample(p,s)))
