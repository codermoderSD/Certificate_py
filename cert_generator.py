from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import numpy
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def createCertificate(name):
    FONT_COLOR = "#000000"
    WIDTH, HEIGHT = 3627, 1253
    image_source = Image.open(r'dummy.jpg')
    draw = ImageDraw.Draw(image_source)
    font = ImageFont.truetype("arial.ttf", 150)
    w, h= draw.textsize(name, font=font)
    draw.text(((WIDTH-w)/2,1200), name, fill=FONT_COLOR, font=font)
    image_source.save("\shubham\Cert_&_emails_python\\" + "Participation_cert"+".jpg")
    print('printing certificate of: '+name)
    
def sendMail(name,email):
    fromaddr = "sdisilva13@gmail.com"
    #"*Add your email*"
    toaddr = email
    msg = MIMEMultipart()  
    msg['From'] = fromaddr 
    msg['To'] = toaddr  
    msg['Subject'] = "Certificate of Participation"
    body = """\
    <html>
    <body>
        <p>Thank you for participating in the workshop</p>
    </body>
    </html>
    """ 
    msg.attach(MIMEText(body, 'html'))  
    filename = "Participation_cert.jpg"
    #add your path
    attachment = open("\shubham\Cert_&_emails_python\Participation_cert.jpg", "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "saviosavio") 
# *Your Email password*
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 

df = pd.read_csv("cert1.csv")
for i in range(len(df)):
    name = df.iloc[i,0]
    email = df.iloc[i,1]
    createCertificate(name)
    sendMail(name, email)
