import random
import mysql.connector as my
# from random import
conn=my.connect(host="localhost",user="root",password="Naman@1234",database="quizz")
cur=conn.cursor()


def validPass():
 while True:
    password=input("Please enter Password\n")
    l=u=d=s=0
    if len(password)>= 8 and len(password)<=20:
        for i in password:
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
            elif i.isdigit():
                d+=1
            else:
                s+=1
        if l>0 and u>0 and d>0 and s>0:
             return password
        else :
             print("plrase use 1 digit,1 special symbal,1 upper_case,1 lower_case Ex.___Naman@1234___")
             False
    else:
        print("use min 8 character password")



   
   
def register():
    name = input("Enter the name: ")
    Enrollment = input("Enter Enrollment: ")
    college_name = input("Enter college: ")
    # password = input("Enter Password: ")  # Corrected to include input function
    password=validPass()
    contact = input("Enter contact: ")
    s='INSERT INTO registration (name,Enrollment,college_name,password,contact)VALUES(%s,%s,%s,%s,%s)'
    t=(name,Enrollment,college_name,password,contact)
    cur.execute(s,t)
    conn.commit()
    print("registration sccessful")
    login()
   

def login():
    # Placeholder for login function
    global username
    global logged_in
    global data

    uname = input("Enter Enrollment: ")
    cur.execute('SELECT * FROM registration where Enrollment =%s',(uname,))
    data=cur.fetchone()
    if data is not None:
        try:
            pass
        except:
            pass

        
        password = input("Enter Password: ")  # Corrected to include input function
        if data[4]==password:
            print(f"Welcomr{data[1]}")
            username=uname
            logged_in=True
            quizz(data)

        else:
            print("password wrong")
       
    else:
        print("Username is incorrect or you are not registered")
        ch=input("do you want to resiterd y/n:")
        if ch =='y' or ch=='Y':
            register()
        else:
            login()
def quizz(data):
     print("""
Choose 1 for Attempt quiz
Choose 2 for View result
Choose 3 for Show profile
Choose 4 for Update Profile
""")
     
     ch=input("Enter your choice:")
     if ch=='1':
        attemptquiz(data)
     elif ch=='2':
        result()
     elif ch=='3':
         showProfile(data)
     elif ch=='4':
        updateProfile()


def updateProfile():
    # name=input("Enter New NAme")
    # # contact=input("Enter new Contact-no")
    # # college_name=input("Enter new College name")
    # s='update quizz.registration set (name)values(%s) where Enrollment={data[2]}'
    # t=(name)
    # cur.execute(s,t)
    # conn.commit()
    pass

def showProfile(data):
    # print(data)
    if data:
        print(f"HELLO {data[1]} Your college is {data[3]} Your contact number is {data[-1]} and your Enrollment-no is :{data[2]}")
    ch = input("Do you want to update your profile: y/n")
    if ch == 'y' or ch == 'Y':
        updateProfile(data)

def attemptquiz(data):
    ch=input("Choose an option\n 1.python\n 2.java\n 3.Reasoning\n")
    if ch=='1':
      sql="SELECT* FROM quizz.questions WHERE category='python'"
      cur.execute(sql)  
      ques=cur.fetchall()

    #   print(ques)

      qu=[]
      correct = 0
      for i in ques:
          qu.append(i)
          qs=random.sample(qu,1)
          print("/n")
          n=1
          for i in qs:
            print(f"HEllo {data[1]} you are attempting quiz of {i[-1]}")
            print(f"Q.{n}. {i[1]}\n A. {i[4]}\n B. {i[5]}\n C. {i[6]}\n D. {i[7]}\n")
            ans = input("Your Answer A/B/C/D: ").lower()
            correct=0
            if ans == i[2]:
               correct += 1
            n = n+1
      print(f"Your Result is {correct}")
      sql = "INSERT INTO quizz.result (Enrollment,marks,name,category) VALUES (%s,%s,%s,'Python')"
      t=(data[2],correct,data[1])
      cur.execute(sql,t)
      conn.commit()



#         attemptQuiz(uname,data)
    elif ch == '2':
        sql = "select * from questions where category = 'java'"
        cur.execute(sql)
        ques = cur.fetchall() #fetchone()
        # print(ques) #[(),(),(),()]
        qu = [] #100
        correct = 0

        for i in ques:
            qu.append(i) #[, , , , ,]
            qs = random.sample(qu,1) #14, 25, 89, 99
            n = 1
            # correct = 0
            for i in qs:
             print(f"Q.{n}. {i[1]}\n A. {i[4]}\n B. {i[5]}\n C. {i[6]}\n D. {i[7]}\n")
             ans = input("Your Answer A/B/C/D: ").lower()
             if ans == i[2]:
                correct += 1
             n = n+1
        print(f"Your Result is {correct}")
        sql = "INSERT INTO quizz.result (Enrollment,marks,name,category) VALUES (%s,%s,%s,'java')"
        t=(data[2],correct,data[1])
        cur.execute(sql,t)
        conn.commit()


    elif ch == '3':
        sql = "select * from questions where category = 'reasoning'"
        cur.execute(sql)
        ques = cur.fetchall() #fetchone()2
        
        # print(ques) #[(),(),(),()]
        qu = [] #100
        correct = 0

        for i in ques:
            qu.append(i) #[, , , , ,]
            qs = random.sample(qu,1) #14, 25, 89, 99
            n = 1
            # correct = 0
            for i in qs:
             print(f"Q.{n}. {i[1]}\n A. {i[4]}\n B. {i[5]}\n C. {i[6]}\n D. {i[7]}\n")
             ans = input("Your Answer A/B/C/D: ").lower()
             if ans == i[2]:
                correct += 1

             n = n+1
        print(f"Your Result is {correct}")
        sql = "INSERT INTO quizz.result (Enrollment,marks,name,category) VALUES (%s,%s,%s,'reasoning')"
        t=(data[2],correct,data[1])
        cur.execute(sql,t)
        conn.commit()






def result():
    # Placeholder for result function
    print("Result functionality goes here.")

def main():
 print("#" * 150)
print("____________________________________Welcome to Quiz____________________________________")
print("1.Registration")
print("2.login")
    # while True:
choice = input("Enter the Choice 1/2/3/4/5: ")
print(choice)
if choice == '1':
    register()
elif choice == '2':
    login()
     # Exits the while loop and thus the program
else:
    print("Choose a correct option.")
 
if __name__ == "__main__":
    main()