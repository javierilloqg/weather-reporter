#otra chapuza para convertir los grados meteorológicos a puntos cardinales. Seguro que se puede hacer más facil con listas y for. Poco preciso pero para el viento puede servir

def direccion(grados):
    if grados == 0 or grados == 360:
        return("N")
    elif grados == 90:
        return("E")
    elif grados == 180:
        return("S")
    elif grados == 270:
        return("O")
    elif 0 < grados < 90:
        return("NE")
    elif 90 < grados < 180:
        return("SE")
    elif 180 < grados < 270:
        return("SO")
    elif 180 < grados < 360:
        return("NO")