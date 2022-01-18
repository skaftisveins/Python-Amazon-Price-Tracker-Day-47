from pprint import pprint
from bs4 import BeautifulSoup
from config import *
import requests
from notification_manager import NotificationManager

notification_manager = NotificationManager()

URL = "https://www.amazon.de/Bloodborne-Game-Year-PlayStation-4/dp/B016ZU4FIQ/ref=sr_1_3?ie=UTF8&qid=1519566642&sr=8-3&keywords=bloodborne+ps4"

page = requests.get(URL, headers=http_headers)
soup = BeautifulSoup(page.content, "html.parser")
price = soup.find(id="priceblock_ourprice").get_text()

print(price.split())
price_without_currency = price.split("€")[0].replace(",", ".")
price_as_float = float(price_without_currency)
print(price_as_float)
price_barr = 20
if price_as_float > price_barr:
    notification_manager.send_emails()
