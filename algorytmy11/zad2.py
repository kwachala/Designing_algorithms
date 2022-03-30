from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from numpy import ones, vstack
from numpy.linalg import lstsq


def create_random_vec():
    vec = []
    for i in range(4):
        x = np.random.uniform(-100, 100)
        vec.append(x)
    return vec


def vec_num():
    print('Podaj ilosc wektorow:')
    x = input()
    list = []
    for i in range(int(x)):
        list.append(create_random_vec())
    return list


def przeciecia(vec):
    list = []
    for i in range(len(vec)):
        for j in range(len(vec)):
            if i > j:
                k = ((((vec[j][0] - vec[i][0]) * (vec[j][3] - vec[j][1])) - (
                        (vec[j][2] - vec[j][0]) * (vec[j][1] - vec[i][1]))) / (
                             ((vec[i][2] - vec[i][0]) * (vec[j][3] - vec[j][1])) - (
                             (vec[j][2] - vec[j][0]) * (vec[i][3] - vec[i][1]))))
                dxAP = k * (vec[i][2] - vec[i][0])
                dyAP = k * (vec[i][3] - vec[i][1])

                xP = vec[i][0] + dxAP
                yP = vec[i][1] + dyAP

                if min(vec[i][0], vec[i][2]) <= xP <= max(vec[i][0], vec[i][2]) and min(vec[i][1],
                                                                                        vec[i][3]) <= yP <= max(
                    vec[i][1], vec[i][3]):
                    if min(vec[j][0], vec[j][2]) <= xP <= max(vec[j][0], vec[j][2]) and min(vec[j][1],
                                                                                            vec[j][3]) <= yP <= max(
                        vec[j][1], vec[j][3]):
                        list.append([xP, yP])

    return list


def prosta(vec):
    list = []
    point = (np.random.uniform(-100, 100), np.random.uniform(-100, 100))
    for i in range(len(vec)):
        points = [(vec[i][0], vec[i][1]), (vec[i][2], vec[i][3])]
        x_coords, y_coords = zip(*points)
        A = vstack([x_coords, ones(len(x_coords))]).T
        m, c = lstsq(A, y_coords)[0]

        if vec[i][1] > vec[i][3] and vec[i][0] > vec[i][2]:
            if -m * point[0] + point[1] - c > 0:
                print('prawa')
                list.append(vec[i])
            if -m * point[0] + point[1] - c < 0:
                print('lewa')
        elif vec[i][1] > vec[i][3] and vec[i][0] < vec[i][2]:
            if -m * point[0] + point[1] - c < 0:
                print('prawa')
                list.append(vec[i])
            if -m * point[0] + point[1] - c > 0:
                print('lewa')
        elif vec[i][1] < vec[i][3] and vec[i][0] < vec[i][2]:
            if -m * point[0] + point[1] - c < 0:
                print('prawa')
                list.append(vec[i])
            if -m * point[0] + point[1] - c > 0:
                print('lewa')
        elif vec[i][1] < vec[i][3] and vec[i][0] > vec[i][2]:
            if -m * point[0] + point[1] - c > 0:
                print('prawa')
                list.append(vec[i])
            if -m * point[0] + point[1] - c < 0:
                print('lewa')


    return point, list

"""
def random_point(vec):
    list = []
    x = np.random.uniform(-100, 100)
    y = np.random.uniform(-100, 100)
    for i in range(len(vec)):
        if vec[i][0] < x and vec[i][2] < x:
            list.append(vec[i])

    return list, (x, y)
"""


vec = vec_num()
vec = [[-10,10,10,10],[0,-10,0,10]]
print('Wektory:', vec)

przec = przeciecia(vec)
print('Miejsca przecięć wektorów', przec)
print('Ilość przecięć:', len(przec))

point, vec_right = prosta(vec)

#l = random_point(vec)
#point = l[1]
#vec_list = l[0]

print('Współrzędne punktu:', point)
print('Wektory majace punkt po prawej stronie:', vec_right)
print('Ilość wektorów mających punkt po prawej stronie:', len(vec_right))


def rysuj():
    # czyszczenie ekranu
    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(10.0)
    glBegin(GL_POINTS)
    for i in range(len(vec)):
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(vec[i][2], vec[i][3])

    for i in range(len(przec)):
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(przec[i][0], przec[i][1])

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(point[0], point[1])

    glEnd()
    # rysowanie prostych
    glLineWidth(3)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for i in range(len(vec)):
        glVertex2f(vec[i][0], vec[i][1])
        glVertex2f(vec[i][2], vec[i][3])

    glEnd()
    # wyświetlanie
    glFlush()


glutInit()
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Zadanie 1")
# parametry OpenGL -- single-buffer i rgb
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
# funkcje rysujące
glutDisplayFunc(rysuj)
glutIdleFunc(rysuj)
# kolor tła
glClearColor(1.0, 1.0, 1.0, 1.0)
# projekcja ortograficzna
gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
# główna pętla (zapętla funkcję "rysuj")
glutMainLoop()
