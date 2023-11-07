import requests


api_key = '9537814cec58e39f23aa412a0560a647'

city = input("Enter your place: ")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pl'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    press = data['main']['pressure']
    desc = data['weather'][0]['description']
    print(f'Temperatura: {temp} stopni celsjusza')
    print(f'Ciśnienie: {press} hPa')
    print(f'Pogoda: {desc}')
else:
    print('Oops! Something went wrong!')
    print("Error:", response.status_code)