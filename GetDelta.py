def get_param(toponym_to_find):
    try:
        import requests

        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()

        if not json_response["response"]["GeoObjectCollection"]["featureMember"]:
            return 0

        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

        delta = str((abs(float(toponym["boundedBy"]['Envelope']["lowerCorner"].split()[0]) -
                         float(toponym["boundedBy"]['Envelope']['upperCorner'].split()[0])))) \
                + "," + \
                str(abs(float(toponym["boundedBy"]['Envelope']["lowerCorner"].split()[1]) -
                        float(toponym["boundedBy"]['Envelope']['upperCorner'].split()[1])))

        return [toponym_longitude, toponym_lattitude, delta]
    except Exception:
        return -1
