from geopy.geocoders import Nominatim
import geocoder

def obtenir_coordonnees():
    g = geocoder.ip('me')
    return g.latlng

def obtenir_ville(lat, lon):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True, language="fr")
    address = location.raw.get('address', {})
    ville = address.get('city', 'Non disponible')
    return ville

if __name__ == "__main__":
    # Obtention des coordonnées GPS
    latitude, longitude = obtenir_coordonnees()

    # Obtention de la ville
    ville = obtenir_ville(latitude, longitude)

    # Affichage des résultats
    print(f"Latitude : {latitude}")
    print(f"Longitude : {longitude}")
    print(f"Ville : {ville}")
