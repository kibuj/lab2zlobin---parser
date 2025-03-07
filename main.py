import requests
from bs4 import BeautifulSoup

URL = "https://meteofor.com.ua/weather-dolyna-12061/month/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

days = soup.find_all("a", class_="row-item row-item-month-date")

for day in days:
    date = day.find("div", class_="date").text.strip()
    weather = day.get("data-tooltip", "Невідомо")

    temp_max_tag = day.find("div", class_="maxt")
    temp_max = temp_max_tag.find("temperature-value")["value"]

    temp_min_tag = day.find("div", class_="mint")
    temp_min = temp_min_tag.find("temperature-value")["value"]

    print(f"Дата: {date}, Погода: {weather}, Температура: {temp_max} / {temp_min}")


