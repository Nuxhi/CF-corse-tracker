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