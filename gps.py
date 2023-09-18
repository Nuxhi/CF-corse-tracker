from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder

def obtenir_coordonnees():
    g = geocoder.ip('me')
    return g.latlng

def obtenir_ville_proche(lat, lon):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True, language="fr")
    current_location = (lat, lon)

    # Obtenir la liste des emplacements dans les environs
    locations = geolocator.reverse(f"{lat}, {lon}", language="fr", exactly_one=False)

    # Initialiser les variables
    ville_proche = None
    distance_min = None

    for loc in locations:
        coords = (loc.latitude, loc.longitude)
        distance = great_circle(current_location, coords).kilometers

        if ville_proche is None or distance < distance_min:
            distance_min = distance
            ville_proche = loc.raw.get('address', {}).get('city', 'Non disponible')

    return ville_proche

if __name__ == "__main__":
    # Obtention des coordonnées GPS
    latitude, longitude = obtenir_coordonnees()

    # Obtention de la ville la plus proche
    ville_proche = obtenir_ville_proche(latitude, longitude)

    # Affichage des résultats
    print(f"Latitude : {latitude}")
    print(f"Longitude : {longitude}")
    print(f"Ville la plus proche : {ville_proche}")
