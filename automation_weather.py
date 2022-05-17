import requests
API_CHEIE_INDEX = "fa8055bf40dbe0a42fda1dffea9fa44a"
URL_BAZA_METEO="http://api.openweathermap.org/data/2.5/weather"

Oras = input("Introdu numele unui oras: ")

CERERE_URL =f"{URL_BAZA_METEO}?appid={API_CHEIE_INDEX}&q={Oras}"
CERERE = requests.get(CERERE_URL)

if CERERE.status_code == 200:
    DATA = CERERE.json()
    print(DATA)
    weather = DATA['weather']
    print(weather)
    temperature = DATA["main"]["temp"]
    print(temperature)
else:
    print("A intervenit o eroare!")
