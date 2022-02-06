def finding_cords(lan, lat):
    try:
        import requests

        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "ll": f"{lan},{lat}",
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()

        if not json_response["response"]["GeoObjectCollection"]["featureMember"]:
            return 0
        else:
            return json_response
    except Exception:
        return -1