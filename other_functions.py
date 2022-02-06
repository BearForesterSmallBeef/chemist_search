def get_distance(a_lon, a_lat, b_lon, b_lat):
    import math

    a_lon, a_lat, b_lon, b_lat = float(a_lon), float(a_lat), float(b_lon), float(b_lat)
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)
    return round(distance)


def get_weekday():
    import datetime
    return datetime.date.today().strftime("%A")