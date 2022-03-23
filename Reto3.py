# encuentra patrones desde celda actual
def totalPatternFromCur(visit, jump, cur, toTouch):
    if toTouch <= 0:

        # si es la ultima celda devuelve un 1
        if (toTouch == 0):
            return 1
        else:
            return 0

    ways = 0

    # posicion vistiada!
    visit[cur] = True

    for i in range(1, 10):

        # si esta posicion no ha sido visitada y,
        # o i y actual son contiguas
        # o hay una posicion visitada entre ellas

        if visit[i] == False and (jump[i][cur] == 0 or visit[jump[i][cur]]):
            ways += totalPatternFromCur(visit, jump, i, toTouch - 1)

    # posicion  no visitada!
    visit[cur] = False

    return ways


# cantidad de conexiones posibles dependiendo de la posicion
def waysOfConnection(ipos, m):
    jump = [[0 for i in range(10)] for j in range(10)]

    # B entre A y C
    jump[1][3] = jump[3][1] = 2

    # H entre G y I
    jump[7][9] = jump[9][7] = 8

    # D entre A y G
    jump[1][7] = jump[7][1] = 4

    # F entre C y I
    jump[3][9] = jump[9][3] = 6

    # E entre A y I / B y H / C y G / D y F
    jump[1][9] = jump[9][1] = jump[2][8] = jump[8][2] = \
        jump[3][7] = jump[7][3] = jump[4][6] = jump[6][4] = 5

    visit = [False] * 10
    ways = 0
    for i in range(m, m + 1):
        # si empezamos por A, C, G, I
        if ipos == 'A' or ipos == 'C' or ipos == 'G' or ipos == 'I':
            ways += totalPatternFromCur(visit, jump, 1, i - 1)

        # si empezamos por B, D, F, H
        elif ipos == 'B' or ipos == 'D' or ipos == 'F' or ipos == 'H':
            ways += totalPatternFromCur(visit, jump, 2, i - 1)

        # si empezamos por E
        elif ipos == 'E':
            ways += totalPatternFromCur(visit, jump, 5, i - 1)

    return ways


if __name__ == '__main__':
    start = 'E'
    connect = 3

    print("Empezando por " + start + " y con " + str(connect) + " puntos conectados, el numero máximo de patrones es: "
          + str(waysOfConnection(start, connect)))
