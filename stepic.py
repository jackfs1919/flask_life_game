import requests
from datetime import datetime


def get_wind_forecast(lat, lon):
    # API параметры: текущий ветер и почасовой прогноз
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["wind_speed_10m", "wind_direction_10m"],
        "hourly": ["wind_speed_10m", "wind_direction_10m"],
        "wind_speed_unit": "ms",  # Получаем сразу в м/с
        "forecast_days": 3,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Функция для перевода градусов в румбы
        def get_direction(deg):
            dirs = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
            return dirs[int((deg + 22.5) // 45) % 8]

        # 1. Текущие данные
        curr_speed = data["current"]["wind_speed_10m"]
        curr_dir = get_direction(data["current"]["wind_direction_10m"])

        # 2. Прогноз на 3 дня (вычисляем среднее или берем пиковые значения)
        # Для краткости выведем средние значения за весь период прогноза
        avg_speed = sum(data["hourly"]["wind_speed_10m"]) / len(
            data["hourly"]["wind_speed_10m"]
        )

        # Находим преобладающее направление (самое частое в прогнозе)
        forecast_dirs = [get_direction(d) for d in data["hourly"]["wind_direction_10m"]]
        most_common_dir = max(set(forecast_dirs), key=forecast_dirs.count)

        return (
            f"скорость в м/с {curr_speed}, {curr_dir} | "
            f"на ближайшие трое суток прогнозируемые скорость в м/с {round(avg_speed, 1)}, {most_common_dir}"
        )

    except Exception as e:
        return f"Ошибка получения данных: {e}"


# Пример вызова для Москвы (55.75, 37.61)
print(get_wind_forecast(68.97, 33.09))

