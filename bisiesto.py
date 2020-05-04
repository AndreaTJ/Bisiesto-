"""La lógica de los años bisiestos:
Cómo saber si un año va a ser bisiesto
• Los años bisiestos son los divisibles entre 4 (como 2004, 2008, etc.)
• excepto si es divisible entre 100, entonces no es bisiesto (como 2100, 2200, etc.)
• excepto si es divisible entre 400, entonces sí (como 2000, 2400)
Reto
Crear una función que compruebe si un año es bisiesto. 
Intentar hacerlo con un if único (ands y ors incluidos) y un else.
También sin elif""" 

def esbisiesto(anno): 
    if (anno%4==0 and anno%100!=0) or anno%400==0: 
        return "Es bisiesto"
    else: 
        return "No es bisiesto"

