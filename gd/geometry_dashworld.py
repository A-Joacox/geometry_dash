import sys
import numpy as np
from colorama import init, Back, Style

init(autoreset=True)

x1, y1 = 22, 1
tria = False
init = ""


def clockwise90(matriz):
    n = np.array(matriz).T[::-1]
    s = np.array(n).T[::-1]
    return np.array(s).T[::-1]


def clockwise180(matriz):
    n = np.array(matriz).T[::-1]
    return np.array(n).T[::-1]


def cuadrado(color: str):
    matriz = np.zeros((16, 16))
    for i in range(1, 15):
        for j in range(1, 15):
            if 2 < i < 13 and 2 < j < 13:
                matriz[i][j] = 0
            else:
                if color == "green":
                    matriz[i][j] = 1
                elif color == "blue":
                    matriz[i][j] = 2
                elif color == "pink":
                    matriz[i][j] = 7
                else:
                    matriz[i][j] = 1
    for i in range(4, 12):
        for j in range(4, 12):
            if 5 < i < 10 and 5 < j < 10:
                matriz[i][j] = 0
            else:
                if color == "green" or color == "pink":
                    matriz[i][j] = 2
                elif color == "blue":
                    matriz[i][j] = 8
                else:
                    matriz[i][j] = 2
    for i in range(7, 9):
        for j in range(7, 9):
            if color == "green":
                matriz[i][j] = 1
            elif color == "blue":
                matriz[i][j] = 2
            elif color == "pink":
                matriz[i][j] = 7
            else:
                matriz[i][j] = 1
    return matriz


def palanca():
    matriz = np.zeros((16, 7))
    for i in range(0, 16):
        if i == 0 or i == 5:
            for j in range(0, 7):
                if j == 0 or j == 1 or j == 5 or j == 6:
                    matriz[i][j] = 5
                else:
                    matriz[i][j] = 6
        elif i == 1 or i == 4:
            for j in range(0, 7):
                if j == 0 or j == 6:
                    matriz[i][j] = 5
                else:
                    matriz[i][j] = 6
        elif i == 2 or i == 3:
            for j in range(0, 7):
                matriz[i][j] = 6
        elif i in range(6, 15):
            for j in range(0, 7):
                if j == 3:
                    matriz[i][j] = 0
                else:
                    matriz[i][j] = 5
        elif i == 15:
            for j in range(0, 7):
                if j == 2 or j == 3 or j == 4:
                    matriz[i][j] = 0
                else:
                    matriz[i][j] = 5
    return matriz


def palancarot90():
    return np.rot90(palanca(), -1)


def triangulo():
    matriz = np.zeros((16, 15))

    for i in range(0, 14, 2):
        for j in range(7 - i // 2):
            matriz[i][j] = 5
            matriz[i + 1][j] = 5

    for i in range(0, 14, 2):
        for j in range(14 - (7 - i // 2), 15):
            matriz[i][j] = 5
            matriz[i + 1][j] = 5

    for i in range(15, 1, -2):
        j = (15 - i) // 2
        matriz[i][j] = 6
        matriz[i - 1][j] = 6

    for i in range(2, 16, 2):
        j = 8 + i // 2 - 1
        matriz[i][j] = 6
        matriz[i + 1][j] = 6
    matriz[0][7] = 6
    matriz[1][7] = 6
    return matriz


def draw_tri_amarillo(triangulo):
    for i in range(len(triangulo)):
        for j in range(len(triangulo[0])):
            if triangulo[i][j] == 0:
                triangulo[i][j] = 6
            elif triangulo[i][j] == 6:
                triangulo[i][j] = 6
    return triangulo


def draw_world(fondo):
    colores = {
        0: Back.BLACK,
        1: Back.LIGHTGREEN_EX,
        2: Back.LIGHTBLUE_EX,
        4: Back.WHITE,
        5: Back.LIGHTWHITE_EX,
        6: Back.LIGHTYELLOW_EX,
        7: Back.LIGHTMAGENTA_EX,
        8: Back.CYAN,
    }
    for fila in fondo:
        for celda in fila:
            print(colores[celda] + '   ', end='')
        print()


def create_world():
    global tria
    global x1
    global y1
    fondo = np.zeros((112, 156))
    for i in range(0, 112):
        for j in range(0, 156):
            if 37 < i < 74 and -1 < j < 113:
                fondo[i][j] = 4
            else:
                fondo[i][j] = 5

    x2, y2 = (22, 24)
    for i in range(len(palanca())):
        for j in range(len(palanca()[0])):
            fondo[x2 + i][y2 + j] = palanca()[i][j]

    x3, y3 = (22, 33)
    if tria == False or (tria == True and y1 != 33):
        for i in range(len(triangulo())):
            for j in range(len(triangulo()[0])):
                fondo[x3 + i][y3 + j] = triangulo()[i][j]
    elif tria == True and y1 == 33:
        for i in range(len(draw_tri_amarillo(triangulo()))):
            for j in range(len(draw_tri_amarillo(triangulo())[0])):
                fondo[x3 + i][y3 + j] = draw_tri_amarillo(triangulo())[i][j]

    x4, y4 = (22, 97)
    if tria == False or (tria == True and y1 != 97):
        for i in range(len(triangulo())):
            for j in range(len(triangulo()[0])):
                fondo[x4 + i][y4 + j] = triangulo()[i][j]
    elif tria == True and y1 == 97:
        for i in range(len(triangulo())):
            for j in range(len(triangulo()[0])):
                fondo[x4 + i][y4 + j] = draw_tri_amarillo(triangulo())[i][j]

    x5, y5 = (58, 113)
    if tria == False or (tria == True and y1 != 113):
        for i in range(len(clockwise90(triangulo()))):
            for j in range(len(clockwise90(triangulo())[0])):
                fondo[x5 + i][y5 + j] = clockwise90(triangulo())[i][j]
    elif tria == True and y1 == 113:
        for i in range(len(clockwise90(triangulo()))):
            for j in range(len(clockwise90(triangulo())[0])):
                fondo[x5 + i][y5 + j] = clockwise90(draw_tri_amarillo(triangulo()))[i][j]

    x6, y6 = (74, 66)
    if tria == False or (tria == True and y1 != 65):
        for i in range(len(clockwise180(triangulo()))):
            for j in range(len(clockwise180(triangulo()[0]))):
                fondo[x6 + i][y6 + j] = clockwise180(triangulo())[i][j]
    elif tria == True and y1 == 65:
        for i in range(len(clockwise180(triangulo()))):
            for j in range(len(clockwise180(triangulo()[0]))):
                fondo[x6 + i][y6 + j] = clockwise180(draw_tri_amarillo(triangulo()))[i][j]

    x7, y7 = (74, 18)
    if tria == False or (tria == True and y1 != 17):
        for i in range(len(clockwise180(triangulo()))):
            for j in range(len(clockwise180(triangulo()[0]))):
                fondo[x7 + i][y7 + j] = clockwise180(triangulo())[i][j]
    elif tria == True and y1 == 17:
        for i in range(len(clockwise180(triangulo()))):
            for j in range(len(clockwise180(triangulo()[0]))):
                fondo[x7 + i][y7 + j] = clockwise180(draw_tri_amarillo(triangulo()))[i][j]

    x8, y8 = (49, 113)
    for i in range(len(palancarot90())):
        for j in range(len(palancarot90()[0])):
            fondo[x8 + i][y8 + j] = palancarot90()[i][j]

    x9, y9 = (74, 3)
    for i in range(len(clockwise180(palanca()))):
        for j in range(len(clockwise180(palanca()[0]))):
            fondo[x9 + i][y9 + j] = clockwise180(palanca())[i][j]

    x10, y10 = (74, 47)
    for i in range(len(clockwise180(palanca()))):
        for j in range(len(clockwise180(palanca()[0]))):
            fondo[x10 + i][y10 + j] = clockwise180(palanca())[i][j]
    return fondo


def draw_player():
    global x1
    global y1
    global tria
    global init
    if ((y1 == 33 and 22 <= x1 < 39) or (y1 == 97 and 22 <= x1 < 39) or (113 <= y1 <= 129 and 42 < x1 <= 58)
            or (x1 == 74 and y1 == 65) or (x1 == 74 and y1 == 17)):
        tria = True
    fondo = create_world()
    if tria == True:
        if 22 <= x1 < 39:
            y1 -= 16
            for i in range(len(cuadrado(init))):
                for j in range(len(cuadrado(init)[0])):
                    fondo[x1 + i][y1 + j] = cuadrado(init)[i][j]
        elif y1 == 113 and x1 != 74:
            if 42 < x1 < 58:
                x1 -= 12
            else:
                x1 -= 16
            for i in range(len(cuadrado(init))):
                for j in range(len(cuadrado(init)[0])):
                    fondo[x1 + i][y1 + j] = cuadrado(init)[i][j]
        elif x1 == 74 and y1 == 65:
            for i in range(len(cuadrado(init))):
                for j in range(len(cuadrado(init)[0])):
                    fondo[74 + i][81 + j] = cuadrado(init)[i][j]
        elif x1 == 74 and y1 == 17:
            for i in range(len(cuadrado(init))):
                for j in range(len(cuadrado(init)[0])):
                    fondo[74 + i][33 + j] = cuadrado(init)[i][j]
    else:
        for i in range(len(cuadrado(init))):
            for j in range(len(cuadrado(init)[0])):
                fondo[x1 + i][y1 + j] = cuadrado(init)[i][j]
    return fondo


def mostrar_escena(mundo):
    global x1
    global y1
    ancho_mundo, alto_mundo = 156, 112
    ancho_escena, alto_escena = 78, 56
    distancia_jugador_borde = 29  #modificar si queremos mostrar más

    if y1 >= ancho_escena - distancia_jugador_borde:
        x_inicio = y1 - (ancho_escena - distancia_jugador_borde)
    else:
        x_inicio = 0
    if x_inicio + ancho_escena > ancho_mundo:
        x_inicio = ancho_mundo - ancho_escena
    y_inicio = max(0, min(x1 - alto_escena // 2, alto_mundo - alto_escena))
    return [fila[x_inicio:x_inicio + ancho_escena] for fila in mundo[y_inicio:y_inicio + alto_escena]]


def move_player(n):
    global x1
    global y1
    global tria
    global init
    global count
    n = n.lower()
    salida = n.split()
    for i in salida:
        if i == "init":
            print("Choose your player:")
            print("(Green)-(Blue)-(Pink)")
            a = input().lower()
            init = a
            if a == "blue" or a == "pink" or a == "green":
                pass
            else:
                print(f"{a} is not a valid input, choosing default player")
        if not tria:
            if x1 == 74 and y1 == 1:
                print("You Won!!")
                print("restart? (yes or no)")
                n = input()
                n.lower()
                if n == "yes":
                    x1, y1 = 22, 1
                    tria = False
                    print(move_player("init"))
                elif n == "no":
                    sys.exit()
                else:
                    return f"{n} is not a valid command, closing game"
            if i == "init":
                x1, y1 = 22, 1
                print("Welcome to Geometry Dash World xyz")
                (draw_world(mostrar_escena(draw_player())))
                print(Style.RESET_ALL)
            elif i == "right":
                if x1 < 38 and y1 < 113:
                    y1 += 16
                elif x1 < 74 and y1 == 113:
                    x1 += 16
                elif x1 == 74:
                    y1 -= 16
                (draw_world(mostrar_escena(draw_player())))
                print(Style.RESET_ALL)
            elif i == "up":
                if x1 < 74 and y1 == 113:
                    y1 += 17
                    x1 += 20
                    (draw_world(mostrar_escena(draw_player())))
                    print(Style.RESET_ALL)
                    y1 -= 17
                    x1 += 16
                    (draw_world(mostrar_escena(draw_player())))
                    print(Style.RESET_ALL)
                elif x1 < 38 and y1 < 130:
                    y1 += 16
                    x1 -= 17
                    (draw_world(mostrar_escena(draw_player())))
                    print(Style.RESET_ALL)
                    y1 += 16
                    x1 += 17
                    (draw_world(mostrar_escena(draw_player())))
                    print(Style.RESET_ALL)
                elif x1 == 74:
                    y1 -= 16
                    x1 += 17
                    (draw_world(mostrar_escena(draw_player())))
                    print(Style.RESET_ALL)
                    y1 -= 16
                    x1 -= 17
                    (draw_world(mostrar_escena(draw_player())))
                    print(Style.RESET_ALL)
    if x1 == 74 and y1 == 1:
        print("You Won!!")
        print("Restart? (yes or no)")
        n = input()
        n.lower()
        if n == "yes":
            x1, y1 = 22, 1
            tria = False
            print(move_player("init"))
        elif n == "no":
            sys.exit()
        else:
            return f"{n} is not a valid command, closing game"
    if tria == False and n != "exit":
        print(move_player(input()))
    elif n == "exit":
        print("Closing game...")
        sys.exit()
    elif tria == True:
        print("Would you like to continue? (yes or no)")
        n = input()
        n.lower()
        if n == "yes":
            x1, y1 = 22, 1
            tria = False
            print(move_player("init"))
        elif n == "no":
            print("Game Over")
            sys.exit()
        else:
            return f"{n} is not a valid command, closing game"
    return ""

