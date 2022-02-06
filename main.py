import sys
from io import BytesIO

import requests

from PIL import Image

from finding_cords import *
from biz_cords import *
from finding_toponym import *
from biz_toponym import *
from GetDelta import get_param
from other_functions import *

from pprint import pprint


map_api_server = "http://static-maps.yandex.ru/1.x/"

# get search string
toponym_to_find = " ".join(sys.argv[1:])

# get toponym
response = finding_toponym(toponym_to_find)
if response == 0:
    print("Объект не найден")
    sys.exit()
elif response == -1:
    print("Произошла ошибка при поиске объекта")
    sys.exit()
toponym = response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]

# get adress
adress = ",".join(toponym["Point"]["pos"].split())

# get chemist toponym
chemist_response = biz_toponym(*adress.split(","))
if chemist_response == 0:
    print("Аптека не найден")
    sys.exit()
elif chemist_response == -1:
    print("Произошла ошибка при поиске аптеки")
    sys.exit()
chemist_toponym = chemist_response["features"][0]

# get chemist adress
chemist_adress = ",".join(map(str, chemist_toponym['geometry']['coordinates']))

# make map response
map_params = {
    "l": "map",
    "pt": f"{adress},pm2dgl~{chemist_adress},pm2dgl"
}
response = requests.get(map_api_server, params=map_params)

# show map
Image.open(BytesIO(response.content)).show()

# collect snippet
distance = get_distance(*adress.split(","), *chemist_adress.split(","))

name = chemist_toponym['properties']['CompanyMetaData']['Categories'][0]['name']

address = ''.join(chemist_toponym['properties']['CompanyMetaData']["address"])

time = chemist_toponym['properties']['CompanyMetaData']['Hours']['Availabilities']
day = get_weekday()
for i in time:
    if day in i.keys():
        if i[day]:
            time = f"с {i['Intervals'][0]['from']} до {i['Intervals'][0]['to']}"
        else:
            time = "Сегодня не работает"

print(f"name: {name}", f"address: {address}", f"work time today: {time}", f"distance: {distance} meters", sep="\n")
