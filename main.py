import requests

URL = "https://meteofor.com.ua/weather-dolyna-12061/month/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    print(response.text[:1000])  # Виводимо перші 1000 символів HTML-коду
else:
    print("Помилка запиту:", response.status_code)