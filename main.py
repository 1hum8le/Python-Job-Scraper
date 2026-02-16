import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# Sprawdźmy, czy pobieranie się udało (kod 200 oznacza sukces)
if page.status_code == 200:
    print("Strona pobrana pomyślnie!")
else:
    print(f"Błąd: {page.status_code}")