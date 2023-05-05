import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "LINK TO AMAZON PRODUCT PAGE"
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWIRD"
TO_EMAIL = "THE RECIPIENT"
TARGET_PRICE = "TARGET PRICE"

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Price trakcer \n\n The price is right!"
        )

head = {
    "User-Agent": "FIND YOURS AT 'https://myhttpheader.com/",
    "Accept-Language": "FIND YOURS AT 'https://myhttpheader.com/",
}
response = requests.get(URL, headers=head)

soup = BeautifulSoup(response.content, "lxml")
price_string = soup.find("span", class_="a-offscreen")

price = str(price_string).split("$")[1]
price_number = (price.split("<")[0])

if float(price_number) < TARGET_PRICE:
    send_mail()
