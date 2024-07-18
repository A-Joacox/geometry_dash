import numpy as np

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