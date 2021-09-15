#******************************************************************************
#* Copyright (C) 2020 by Javier Quesada Galban
#*
#* Python module to show possible storms
#*
#******************************************************************************
#
#* @file modulo_presion.py
#* @author Javier Quesada Galban
#* @date 13 April 2021
#* @brief This module will return information about possible storms based on 
#  barometric preassure from openweather data 
#*
#

def comprobarpresion(presion):
    if presion <= 990:
        return("¡Posibles tormentas!")
    else:
        return("No se esperan tormentas")
