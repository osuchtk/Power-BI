import meteostat
from datetime import datetime
import pandas as pd
import os
import glob

#gathering weather data
start = datetime(2021, 1, 1)
end = datetime(2021, 12, 31)

locations = [[53.428544, 14.552812], #Szczecin
             [52.229676, 21.012229], #Warszawa
             [52.406374, 16.9251681], #Poznań
             [52.229676, 21.012229], #Lódź
             [51.107885, 17.038538], #Wrocław
             [54.352025, 18.646638], #Gdańsk
             [53.132489, 23.168840], #Białystok
             [53.132489, 23.168840], #Białystok
             [51.246454, 22.568446], #Lublin
             [50.264892, 19.023781], #Katowice
             [50.064650, 19.944980], #Kraków
             [51.935621, 15.506186], #Zielona Góra
             [54.111522, 22.930788], #Suwałki
             [49.299181, 19.949562], #Zakopane
             [53.013790, 18.598444], #Toruń
             [50.866077, 20.628568], #Kielce
             [51.402724, 21.147133], #Radom
             [50.286264, 19.104079], #Sosnowiec
             [53.483749, 18.753565], #Grudziądz
             [50.041187, 21.999120], #Rzeszów
             [53.778422, 20.480119], #Olsztyn
             [50.348382, 18.915717], #Bytom
             [50.811819, 19.120309], #Częstochowa
             [50.294492, 18.671380], #Gliwice
             [50.324928, 18.785719], #Zabrze
             [49.822377, 19.058384], #Bielsko-Biała
             [50.675107, 17.921298], #Opole
             [52.728295, 15.241226], #Gorzów Wielkopolski
             [50.330667, 19.208353], #Dąbrowa Górnicza
             [53.909051, 14.249265], #Świnoujście
             [54.464148, 17.028482], #Słupsk
             [49.624954, 20.691550], #Nowy Sącz
             [49.782433, 22.769044], #Przemyśl
             [49.555019, 22.206066], #Sanok
             [50.723088, 23.251969], #Zamość
             [52.032952, 23.117571], #Biała Podlaska
             ]

cities = ['Szczecin', 'Warszawa', 'Poznań', 'Lódź', 'Wrocław', 'Gdańsk', 'Białystok', 'Lublin', 'Katowice', 'Kraków',
          'Zielona Góra', 'Suwałki', 'Zakopane', 'Toruń', 'Kielce', 'Radom', 'Sosnowiec', 'Grudziądz', 'Rzeszów',
          'Olsztyn', 'Bytom', 'Częstochowa', 'Gliwice', 'Zabrze', 'Bielsko-Biała', 'Opole', 'Gorzów Wielkopolski',
          'Dąbrowa Górnicza', 'Świnoujście', 'Słupsk', 'Nowy Sącz', 'Przemyśl', 'Sanok', 'Zamość', 'Biała Podlaska']


for (loc, name) in zip(locations, cities):
    mainDataframe = pd.DataFrame()

    place = meteostat.Point(loc[0], loc[1])
    data = meteostat.Daily(place, start, end)
    data = data.fetch()

    mainDataframe = mainDataframe.append(data)

    mainDataframe['name'] = name

    mainDataframe.to_csv('pogoda' + name +'.csv', encoding='utf-8')
print('Gathering weather data completed.')


#merging csv files
path = os.path.join('D:/Naukowe/powerbi/weather', "*.csv")

files = glob.glob(path)
#print(files)

df = pd.concat(map(pd.read_csv, files))
df.to_csv("allWeather.csv", encoding='utf-8')

print("All csv's merged into one file.")

