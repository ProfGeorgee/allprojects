import mysql.connector
import hashlib
import bcrypt


class Security():
# registering a new user
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost",user="hospital", password="password",database="hospital")
        self.curse=self.con.cursor()
        self.salt= bcrypt.gensalt()
    def register(self):
        self.uid = input('enter ur username: ')
        self.pas = input('Enter ur password: ').encode("utf-8")
        self.pas_hash = bcrypt.hashpw(self.pas, self.salt)
        self.curse.execute("INSERT INTO users(hash,uid,salt) VALUES ('{}','{}', '{}')".format(self.pas_hash.decode(),self.uid, self.salt.decode()))
        self.con.commit()




    def login(self):
        user_ins = input('Enter your username/email').encode("utf-8")
        pass_ins = input('Enter your password')
        counter = 0
        que = "SELECT salt,hash FROM users WHERE uid = %s"
        self.curse.execute(que, tuple(user_ins))

         
            

s = Security()
ans = input("do you want to register? y/n: ")
if ans == 'y':
    ## redirect to register page and call register
    s.register()
elif ans == 'n':
    ## redirect to the login page
    s.login()
#else:
#connection.commit()
