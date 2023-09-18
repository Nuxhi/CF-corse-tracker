import ctypes

def get_city_name():
    try:
        geolocation = ctypes.windll.winmm.timeGetTime()
        latitude = (geolocation >> 32) * 1e-7
        longitude = (geolocation & 0xffffffff) * 1e-7
        return f"Latitude: {latitude}, Longitude: {longitude}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    location_info = get_city_name()
    print(f"Votre emplacement (latitude, longitude) est : {location_info}")



import geocoder

def get_city_name():
    g = geocoder.ip('me')
    return g.city

if __name__ == "__main__":
    city_name = get_city_name()
    print(f"Vous êtes dans la ville de {city_name}")


---- 
from geopy.geocoders import Nominatim
import geocoder

def get_city_name():
    # Obtenir les coordonnées GPS
    g = geocoder.ip('me')
    latitude, longitude = g.latlng

    # Utiliser les coordonnées pour obtenir la ville
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)

    # Extraire le nom de la ville
    address = location.raw.get('address', {})
    city = address.get('city', '')
    return city

if __name__ == "__main__":
    city_name = get_city_name()
    print(f"Vous êtes dans la ville de {city_name}")
