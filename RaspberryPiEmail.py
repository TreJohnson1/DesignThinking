from picamera import PiCamera
from time import sleep
import smtplib
import imghdr
from email.message import EmailMessage


# SMTP = SIMPLE MESSAGE TRANSFER PROTOCOL
Email_ADDRESS = 'Ferengi902@gmail.com'
Email_PASSWORD = 'Ferengi123!'

picture = PiCamera()
picture.start_preview()
sleep(2)
picture.capture('/home/pi/Desktop/image.jpg') #Path for the image
picture.rotation(180)
picture.stop_preview()

msg = EmailMessage()
msg['Subject'] = 'PICTURE'
msg['From'] = Email_ADDRESS
msg['To'] = 'trexjohnson27@gmail.com' #email your sending to
msg.set_content('GOAL')

with open('/home/pi/Desktop/image.jpg', 'rb') as f:
# I used an absolute path to locate the picture.

    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
    msg.add_attachment(file_data, maintype='image',subtype=file_type,filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

  smtp.login(Email_ADDRESS,Email_PASSWORD)
  smtp.send_message(msg)
