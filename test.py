import requests


# Готовим запрос.


def get_adress_componet(town, component_index):
    geocoder_request = f'{server_address}apikey={api_key}&geocode={town}&format=json'
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()
        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
        return  toponym_address[component_index]["name"]
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")


server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
geocode_list = ["Барнаул", "Мелеуз", "Йошкар-Ола"]
for town in geocode_list:
    print(get_adress_componet(town,2))