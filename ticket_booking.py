import mysql.connector
import smtplib
import datetime
print("***UMA CINEMAS***")
def gst_rate():
    gst_rate=5
    gst_amount=cost*gst_rate/100
    total_price=cost+gst_amount
    print(f"the total amount is {total_price}")
    return total_price
def email_sending(name, movie, show_timing, class_booking):
      try:
       receiver_mails=["kmugil0507@gmail.com"]
       for i in receiver_mails:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("rakshana0211@gmail.com","ejsh lwmf ngyw rwoy")
            x=datetime.datetime.now()
            message=f"***Uma Cinemas***\n date:{x}\n {name} is successfully booked {movie} movie..\nThe show timing is {show_timing}\n You have booked the class {class_booking}"
            s.sendmail("rakshana0211@gmail.com", i, message)
            s.quit()
            print("mail sent successfully")
      except:
       print("mail not sending")
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ticket_booking"
    )
mycursor=mydb.cursor()
sql="insert into booking values(%s,%s,%s,%s,%s)"
name=str(input("enter ur name:"))
movie=str(input("enter the movie name:"))
show_timing=str(input("enter the show timings:"))
class_booking=str(input("enter the class for seating: "))
try:
   if class_booking=="A":
       print("The price for class A is 200 per person")
       price=200
       person=int(input("enter how many tickets do u need?:"))
       cost=price*person
       amount=gst_rate()
       email_sending(name, movie, show_timing, class_booking)
   elif class_booking=="B":
       print("The price for class B is 150 per person")
       price=150
       person=int(input("enter how many tickets do u need?:"))
       cost=price*person
       amount=gst_rate()
       email_sending(name, movie, show_timing, class_booking)
   elif class_booking=="C":
       print("The price for class C is 120 per person")
       price=120
       person=int(input("enter how many tickets do u need?:"))
       cost=price*person
       amount=gst_rate()
       email_sending(name, movie, show_timing, class_booking)
except:
  print("enter only clas A, B, C only")
f=open("movie bill.txt","a")
f.write(f"{name} is successfully booked {movie} movie..The show timing is {show_timing} on ")
f=open("movie bill.txt","a")
x=datetime.datetime.now()
f.write(f"date:{x}\n")
val=(name,movie,show_timing,class_booking,amount)
mycursor.execute(sql,val)
mydb.commit()
print("data saved successfully")

