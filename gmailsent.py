import smtplib
sm=smtplib.SMTP("smtp.gmail.com",587)
#here 587 is the port through which you cionnetc
#smptp@gamil.com is to check yoyur gmail is correct or not
sm.ehlo()
sm.starttls()


email="alexanderritik@gmail.com"
password="aejojqixkfvbguco"

sm.login(user=email,password=password)

from_address=email
to_address=input('enter the email of persoon you want to sent: ')
subject=input("Enter the subject of message : ")
message=input("Enter the  message : ")
attach=input("You can attach a text")
msg="Subject : "+subject+ '\n'+" message : "+message+ '\n' + "attachment" + attach
sm.sendmail(from_address,to_address,msg)
