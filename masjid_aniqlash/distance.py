import math
from aiogram import types
from .location import Masjid

URL = "http://maps.google.com/maps?q={lat},{lon}"

def show(lat, lon):
    return URL.format(lat=lat, lon=lon)

def calc_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2-lat1)
    delta_lambda = math.radians(lon2-lon1)

    a = math.sin(delta_phi / 2.0) ** 2 +\
        math.cos(phi_1) * math.cos(phi_2) * \
        math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 -a))

    meters = R * c
    return meters / 1000.0


def choose_shortes(location: types.Location):
    distances = list()
    for masjid_location in Masjid:
        distances.append((
                          calc_distance(location.latitude, location.longitude,
                                        masjid_location["lat"], masjid_location["lon"]),
                          show(masjid_location["lat"],  masjid_location["lon"]),
                          masjid_location
                          ))
    return sorted(distances, key=lambda x: x[:1])[:3]
