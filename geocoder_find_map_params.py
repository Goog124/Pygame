import requests


def get_map_params(toponim):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": toponim,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    leftup = list(map(float, toponym["boundedBy"]['Envelope']['lowerCorner'].split()))
    rightdown = list(map(float, toponym["boundedBy"]['Envelope']["upperCorner"].split()))
    spn1 = str(abs(leftup[0] - rightdown[0]) / 2.0)
    spn2 = str(abs(leftup[1] - rightdown[1]) / 2.0)
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    result = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([spn1, spn2])
    }
    return result
