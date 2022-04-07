"""
Un grajero chino se encontraba mirando un lago circular del cual salia exactamente 
en el centro una porción de un junquillo, este junquillo nacía exactamente en el centro del fondo del lago, 
el granjero observó que cuando el viento soplaba el junquillo se inclinaba sin deformarse 
y al tocar la orilla del lago quedaba exactamente cubierto por el
agua. Escribe un programa que le ayude al granjero a determinar la profundidad del lago.
"""
from decimal import DivisionByZero
import math
import re
def junquillo_chino(d, h):
    """
    d : diámetro
    h : altura del junco 

    x = (d**2 - 4*h**2)/8*h
    """
    if h > 0:
        hn = h*0.01
        result = round((math.pow(d,2) - 4 * math.pow(hn,2))/(8*hn), 1)
    else:
        result = 0
    return result
        

if __name__ == "__main__":
    assert junquillo_chino(3, 30) == 3.6
    assert junquillo_chino(10, 20) == 62.4
    assert junquillo_chino(5, 25) == 12.4
    assert junquillo_chino(0, 0) == 0    