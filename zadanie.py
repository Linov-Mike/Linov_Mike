import requests
import datetime

api = 'https://api.openweathermap.org/data/2.5/onecall?lat=59.8944&lon=30.2642&units=metric&appid='
print('Введите ваш персональный API ключ с сайта openweathermap.org')
personal_api = input()
url = api + personal_api
json_data = requests.get(url).json()


def creating_a_list_of_data():  # Сбор информации с сайта
    days_info = []
    for total_data in json_data['daily']:
        time = total_data['dt']
        night = total_data['temp']['night']
        morn = total_data['temp']['morn']
        pressure = total_data['pressure']
        days_info.append(sorted([time, night, morn, pressure]))

    return days_info


def information_out():  # расчеты
    info_out = []
    for data in list_of_data[:5]:
        temperature_difference = round(data[1] - data[0], 2)  # разница температур
        pressure = (round(data[2] * 7.50062 * 10 ** 3) / 10000)  # конвертация в мм ртутного столба
        time = datetime.datetime.fromtimestamp(data[3]).strftime('%Y-%m-%d')  # конвертация даты
        info_out.append([temperature_difference, pressure, time])

    return info_out


def printing_info():  # печать
    info.sort(key=lambda i: i[1], reverse=True)
    print('Максимальное давление на предстоящие 5 дней (включая текущий) '
          '{} мм ртутного столба'.format(info[0][1]))
    info.sort(key=lambda i: i[0], reverse=False)
    print('День с минимальной разницей междуночной и утренней температурой '
          '{}'.format(info[0][2]))


list_of_data = creating_a_list_of_data()
info = information_out()
printing = printing_info()
