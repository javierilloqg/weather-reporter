#******************************************************************************
#* Copyright (C) 2020 by Javier Quesada Galban
#*
#* Python module to show wind direction
#*
#******************************************************************************
#
#* @file modulo_direccion_viento.py
#* @author Javier Quesada Galban
#* @date 13 April 2021
#* @brief This module returns cardinal points based on wind direction (degrees)  
#*
#

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