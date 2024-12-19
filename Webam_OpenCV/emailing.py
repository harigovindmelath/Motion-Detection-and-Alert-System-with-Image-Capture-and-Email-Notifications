import smtplib
from email.message import EmailMessage
from PIL import Image
from io import BytesIO

SENDER = "portofoliohari@gmail.com"
PASSWORD = "wfratsmvgcbibolr"
RECIEVER = "harikrishnanmelath@gmail.com"


def send_email(image_path):
    print("Email is sending!!")
    email_message = EmailMessage()
    email_message["Subject"] = "New person just entered!!"
    email_message.set_content("Hey,a person just came in")

    with open(image_path, 'rb') as file:
        content = file.read()
    image_data = BytesIO(content)
    img = Image.open(image_data)
    image_format = img.format
    email_message.add_attachment(content, maintype="image", subtype=image_format)
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECIEVER, email_message.as_string())
    gmail.quit()
    print("Email function is ended")


