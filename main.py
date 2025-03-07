import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext


def fetch_weather():
    URL = "https://meteofor.com.ua/weather-dolyna-12061/month/"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    days = soup.find_all("a", class_="row-item row-item-month-date")
    temp = []
    result_text = ""

    for day in days:
        date = day.find("div", class_="date").text.strip()
        weather = day.get("data-tooltip", "Невідомо")

        temp_max_tag = day.find("div", class_="maxt")
        temp_max = temp_max_tag.find("temperature-value")["value"]

        temp_min_tag = day.find("div", class_="mint")
        temp_min = temp_min_tag.find("temperature-value")["value"]

        temp.append(int(temp_max))
        result_text += f"Дата: {date}, Погода: {weather}, Температура: {temp_max} / {temp_min}\n"

    max_temp = max(temp)
    result_text += f"\nНайвища температура в найблищі 30 днів: {max_temp}"

    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, result_text)


root = tk.Tk()
root.title("Прогноз погоди")
root.geometry("1000x800")

btn_fetch = tk.Button(root, text="Отримати прогноз", command=fetch_weather)
btn_fetch.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, width=100, height=40)
text_area.pack()

root.mainloop()
