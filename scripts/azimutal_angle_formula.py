from math import radians, sin, cos, atan2, degrees, pi

def azimuth_angle(lat1, lon1, lat2, lon2):
    # Calcula la diferencia de longitud en radianes
    dlon = radians(lon2 - lon1)

    # Convierte las latitudes de grados a radianes
    lat1, lat2 = radians(lat1), radians(lat2)

    # Calcula componentes para la fórmula del ángulo azimutal
    a1 = sin(dlon) * cos(lat2)
    a2 = sin(lat1) * cos(lat2) * cos(dlon)
    a2 = cos(lat1) * sin(lat2) - a2

    # Calcula el ángulo azimutal
    azimuth = atan2(a1, a2)

    # Ajusta el ángulo para que esté en el rango de 0 a 2*pi
    azimuth = (azimuth + 2 * pi) % (2 * pi)

    # Convierte el ángulo de radianes a grados y lo devuelve
    return degrees(azimuth)

# Ejemplo de uso
lat1, lon1 = 25.7423252, -100.2794307  # Mty
lat2, lon2 = 25.7422753, -100.2794433  # san Nico

result = azimuth_angle(lat1, lon1, lat2, lon2)
print(f"Ángulo Azimutal (Rumbo): {result:.2f} grados")
