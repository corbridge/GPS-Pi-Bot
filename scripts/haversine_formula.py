from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0

    # Convierte las coordenadas de grados a radianes
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Diferencias de latitud y longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance

# Ejemplo de uso
lat1, lon1 = 37.7749, -122.4194  # Coordenadas de San Francisco, CA
lat2, lon2 = 34.0522, -118.2437  # Coordenadas de Los Angeles, CA

result = haversine_distance(lat1, lon1, lat2, lon2)
print(f"Distancia entre los puntos: {result:.2f} km")
