from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import numpy
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#read csv file
df = pd.read_csv("cert1.csv")
#for loop
for i in range(len(df)):

    name = df.iloc[i,0]
    email = df.iloc[i,1]

    #template vala code

    FONT_COLOR = "#000000"
    WIDTH, HEIGHT = 3627, 1253

    """function to generate certificate"""
    image_source = Image.open(r'dummy.jpg')
    draw = ImageDraw.Draw(image_source)
    font = ImageFont.truetype("arial.ttf", 150)
    w, h= draw.textsize(name, font=font)
    draw.text(((WIDTH-w)/2,1200), name, fill=FONT_COLOR, font=font)
    image_source.save("\shubham\Cert_&_emails_python\\" + "Participation_cert"+".jpg")
    print('printing certificate of: '+name)

   #email vala code

    fromaddr = "*Add your email*"
    toaddr = email

    # instance of MIMEMultipart 
    msg = MIMEMultipart() 

    # storing the senders email address 
    msg['From'] = fromaddr 

    # storing the receivers email address 
    msg['To'] = toaddr 

    # storing the subject 
    msg['Subject'] = "Certificate of Participation"

    # string to store the body of the mail 
    body = """\
    <html>
    <body>
        <p>Thank you for participating in the workshop</p>
    </body>
    </html>
    """

    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'html')) 

    # open the file to be sent 
    filename = "Participation_cert.jpg"
    #add your path
    attachment = open("\shubham\Cert_&_emails_python\Participation_cert.jpg", "rb") 

    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 

    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 

    # encode into base64 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(fromaddr, "*Your Email password*") 

    # Converts the Multipart msg into a string 
    text = msg.as_string() 

    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 

    # terminating the session 
    s.quit() 