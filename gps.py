from gps import gps, WATCH_ENABLE, WATCH_NEWSTYLE

def obtenir_coordonnees_gps():
    session = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
    report = session.next()
    if report['class'] == 'TPV':
        return report['lat'], report['lon']
    else:
        return None, None

if __name__ == "__main__":
    # Obtention des coordonnées GPS
    latitude, longitude = obtenir_coordonnees_gps()

    if latitude is not None and longitude is not None:
        print(f"Latitude : {latitude}")
        print(f"Longitude : {longitude}")
    else:
        print("Impossible d'obtenir les coordonnées GPS. Assurez-vous que votre carte GPS est activée et fonctionnelle.")
