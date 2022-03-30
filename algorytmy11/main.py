from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def rysuj():
    # czyszczenie ekranu
    glClear(GL_COLOR_BUFFER_BIT)
    # rysowanie punktów
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(50.0, 50.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(50.0, -50.0)

    glEnd()
    # rysowanie prostych
    glLineWidth(1)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.0)
    glVertex2f(50.0, 50.0)
    glVertex2f(50.0, 50.0)
    glVertex2f(50.0, -50.0)
    glVertex2f(50.0, -50.0)
    glVertex2f(0.0, 0.0)
    glEnd()
    # wyświetlanie
    glFlush()


# inicjalizacja OpenGL i okna

glutInit()
glutInitWindowSize(600, 400)
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
