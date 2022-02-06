def biz_cords(lan, lat):
    try:
        import requests

        search_api_server = "https://search-maps.yandex.ru/v1/"
        api_key = "d50b871c-4584-4da7-acad-2b798e5758fc"

        search_params = {
            "apikey": api_key,
            "lang": "ru_RU",
            "ll": f"{lan},{lat}",
            "type": "biz",
            "results": "1"
        }
        response = requests.get(search_api_server, params=search_params)
        json_response = response.json()

        if not json_response["features"]:
            return 0
        else:
            return json_response
    except Exception:
        return -1