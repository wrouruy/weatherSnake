from tkinter import *
import urllib.request
from urllib.parse import quote
from PIL import Image, ImageTk
import requests
import json
from io import BytesIO
from datetime import datetime

# set up the window
root = Tk()
root.title('Weather Snake')
root.geometry('420x350')
root.resizable(width=False, height=False)

weatherAPIKey = 'f3786404d317540398ce534959c0104b'

currentWeather = {
    'cityName': StringVar(),
    'cloudInfo': StringVar(value='Enter your city below'),
    'temp': StringVar(),
    'lastUptade': StringVar()
}

# function for getting weather info
def getWeather(city):
    with urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={quote(city)}&appid={weatherAPIKey}') as response:
        data = json.loads(response.read())
        currentWeather['cityName'].set(data['name'] + '🏢')
        currentWeather['cloudInfo'].set(data['weather'][0]['description'] + '⛅')
        currentWeather['temp'].set(f"{round(data['main']['temp_min'] - 273.15, 1)} - {round(data['main']['temp_max'] - 273.15, 1)} ℃")
        currentWeather['lastUptade'].set(f'Last Uptade: {datetime.now().strftime("%H:%M.%S")}')

        new_photo = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(f"https://flagsapi.com/{data['sys']['country']}/flat/64.png").content)).resize((160, 160)))
        label.config(image=new_photo)
        label.image = new_photo

# create container
enterContainer = Frame(root, bg='#c4c4c4', pady=10, padx=10)  

# create Input and Button for entry city
inputCity = Entry(enterContainer, width=30)
inputCity.pack(side="left", padx=5) 
buttonCity = Button(enterContainer, width=5, height=1, text='Send', bg='black', fg='white', command=lambda: getWeather(inputCity.get()))
buttonCity.pack(side="left", padx=5)

enterContainer.pack(side="bottom", anchor="center", pady=10)

# Title Label that updates when city changes
Label(root, textvariable=currentWeather['cityName'], font='Segoe-UI 20').pack(side='top')
Label(root, textvariable=currentWeather['lastUptade'], font='Segoe-UI 10', pady=10 ).pack(side='bottom')

Label(root, textvariable=currentWeather['cloudInfo'], font='Segoe-UI 15').pack(side='bottom')
Label(root, textvariable=currentWeather['temp'], font='Segoe-UI 15').pack(side='bottom')


photo = ImageTk.PhotoImage(Image.open('NaNcountry.png').resize((200, 160)))
label = Label(root, image=photo)
label.pack()

root.mainloop()
