import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()


Email = input("Enter your Gmail-ID :")
Password = input("Enter your password :")


server.login(Email, Password)


def sendEmail(participant_name, to, certificate):
    

    subject = f"Hello {participant_name}, Your Certificate is Ready!"
 
 
    msg = MIMEMultipart()
    msg['From'] = Email
    msg['To'] = to
    msg['Subject'] = subject
 
     
    body = f"""\
        <html>
        <body>

        Dear <strong>{participant_name}</strong>, <br>

        <p>Greetings from Google developer Student Club Gaya College of Engineering!<br><br>

            Congratulations on the successful completion of your Android Basics in Kotlin Course <br>
            through Android Study Jam Program organized by GDSC GCE community.<br>
            We hope this program was helpful to you.<br><br>

            Now that you've earned your certificate, why not share it wih your network?<br>

            Ways to share:<br>

                <ol>
                    <li>
                     Add your Certificate directly to your LinkedIn Profile
                    </li>
                <li> Share on social media and your LinkedIn Feed</li>
                </ol>

            Once again, congratulations on your achievement.<br>
        </p>

            Keep it Up,<br>
           <strong>
            Shalu Ambasta<br>
            Android Jam Facilitator
           </strong>
            </body>
        </html>
    """

    msg.attach(MIMEText(body, 'html'))
 
    attachment = open(certificate, "rb")
 
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    "attachment; filename= %s" % certificate)
 
    msg.attach(part)
    
    text = msg.as_string()
    server.sendmail(Email, to, text)
 


sendEmail("Lhasa Apso", "receiver@gmail.com", "Certificates\Lhasa Apso.jpg")


print("Emails Sent")


server.quit()
print("Server Quits")