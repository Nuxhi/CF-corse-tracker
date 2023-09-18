import requests

def obtenir_coordonnees():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    lat, lon = data['loc'].split(',')
    return float(lat), float(lon)

def obtenir_ville(lat, lon):
    response = requests.get(f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18')
    data = response.json()
    ville = data['address'].get('city', 'Non disponible')
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
