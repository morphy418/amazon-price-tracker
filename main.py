import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

#Amazon URL and the Price You Are Looking For
URL = "https://www.amazon.co.uk/Fantasy-Flight-Games-SW03-Rebellion/dp/B017MLIGP0/ref=sr_1_4?crid=3SH19J5T0Q5Z8&keywords=star%2Bwars%2Brebellion%2Bboard%2Bgame&qid=1638280854&qsid=258-9684686-5692145&s=kids&sprefix=star%2Bwars%2Breb%2Ctoys%2C160&sr=1-4&sres=B017MLIGP0%2CB01G8ZY20E%2CB01IQXDQ5I%2CB097954XFN%2CB097977NLC%2CB00ZBQ5DBO%2C1633442896%2C1633441261%2CB07SWT1S13%2CB07NRHKD64%2CB01BKBXQ58%2CB08CB9XJS2%2CB07T738M6J%2CB00U26V4VQ%2CB01IPUGYK6%2CB09KLVQ2RD%2CB0847NVBHQ%2C1616619937%2CB01L93GGVI%2CB0824SPB54&srpt=BOARD_GAME&th=1"
TARGET_PRICE = 200

#Adjust your header according to http://myhttpheader.com/
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,hu;q=0.7"
}

response = requests.get(URL, headers=headers)

amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")

price_span = soup.find(name="span", class_="a-offscreen")
price = float(price_span.getText().split("£")[1])
print(price)

title = soup.find(id="productTitle").get_text().strip()

if price < TARGET_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP HERE, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR EMAIL HERE, PASSWORD HERE)
        connection.sendmail(
            from_addr=FROM EMAIL,
            to_addrs=TO EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )