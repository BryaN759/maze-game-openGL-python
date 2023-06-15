from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import keyboard
import numpy as np
import math


def addPixel(a, b):

    glBegin(GL_POINTS)
    glVertex2f(a, b)
    glEnd()


def findZone(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  if abs(dx) <= abs(dy):
    if dx >= 0 and dy >= 0:
      return 1
    elif dx <= 0 and dy >= 0:
      return 2
    elif dx >= 0 and dy <= 0:
      return 6
    elif dx <= 0 and dy <= 0:
      return 5
  else:
    if dx >= 0 and dy >= 0:
      return 0
    elif dx <= 0 and dy >= 0:
      return 3
    elif dx >= 0 and dy <= 0:
      return 7
    elif dx <= 0 and dy <= 0:
      return 4


def convertZero(z, x, y):
  if z == 0:
    return x, y
  elif z == 1:
    return y, x
  elif z == 2:
    return y, -x
  elif z == 3:
    return -x, y
  elif z == 4:
    return -x, -y
  elif z == 5:
    return -y, -x
  elif z == 6:
    return -y, x
  elif z == 7:
    return x, -y


def midpoint(z, x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  d = (2 * dy) - dx
  dE = 2 * dy
  dNE = 2 * (dy - dx)
  y = y1
  x = x1
  while x < x2:
    a, b = convertBack(z, x, y)
    addPixel(a, b)
    if d < 0:  # next pixel: NE
      x += 1
      d += dE

    else:
      y += 1
      x += 1
      d += dNE  # next pixel: E


def convertBack(z, x, y):
  if z == 0:
    return x, y
  elif z == 1:
    return y, x
  elif z == 2:
    return -y, x
  elif z == 3:
    return -x, y
  elif z == 4:
    return -x, -y
  elif z == 5:
    return -y, -x
  elif z == 6:
    return y, -x
  elif z == 7:
    return x, -y


def printLine(x1, y1, x2, y2):
  zone = findZone(x1, y1, x2, y2)
  a, b = convertZero(zone, x1, y1)
  c, d = convertZero(zone, x2, y2)
  midpoint(zone, a, b, c, d)

def midpointCircle(originX, originY, r):
  x = 0
  y = r
  d = 1 - r
  # dE = 2 * x + 3
  # dSe = 2 * (x - y) + 5
  while x <= y:
    if d < 0:  # Choose E
      d += 2 * x + 3

    else:  # Choose SE
      d += 2 * (x - y) + 5
      y -= 1

    x += 1
    eightWay(originX, originY, x, y)


def eightWay(originX, originY, x, y):
  addPixel(originX + x, originY + y)  # zone1
  addPixel(originX + y, originY + x)  # zone0
  addPixel(originX - x, originY + y)  # zone2
  addPixel(originX - y, originY + x)  # zone3
  addPixel(originX - x, originY - y)  # zone5
  addPixel(originX - y, originY - x)  # zone4
  addPixel(originX + x, originY - y)  # zone6
  addPixel(originX + y, originY - x)  # zone7

def box(x ,y):
    glPointSize(10)
    glColor3f(0.7, 0.5, 0.8)
    printLine(x, y+10, x+10, y+10)
    printLine(x, y, x+10, y)
def map(level):
  for y in range(len(level)):
    for x in range(len(level[y])):
      if level[y][x] == "X":
        new_X = (x * 20)+20
        new_Y = (y * 20)+20
        box(new_X, new_Y)
def maze():
  m1 = [
    "XXXXXXXXXXXXX  XXXXXXXXXXXXXXXX",
    "X        X     X        X     X",
    "X        X     X        X     X",
    "X  XXXX  X  X  X  XXXX  X  X  X",
    "X  X  X     X     X  X     X  X",
    "X  X  X     X     X  X     X  X",
    "X  X  XXXXXXXXXX  X  XXXXXXX  X",
    "X  X        X  X     X     X  X",
    "X  X        X  X     X     X  X",
    "X  X  XXXX  X  XXXXXXX  X  X  X",
    "X  X     X     X        X  X  X",
    "X  X     X     X        X  X  X",
    "XXXXXXX  X  XXXX  XXXXXXX  X  X",
    "X        X        X     X     X",
    "X        X        X     X     X",
    "X  XXXXXXX  XXXXXXX  X  X  XXXX",
    "X        X     X  X  X  X     X",
    "X        X     X  X  X  X     X",
    "XXXX  XXXXXXX  X  X  X  XXXX  X",
    "X     X     X        X     X  X",
    "X     X     X        X     X  X",
    "X  X  X  X  XXXXXXXXXXXXX  X  X",
    "X  X  X  X        X  X     X  X",
    "X  X  X  X        X  X     X  X",
    "X  X  X  XXXXXXX  X  X  XXXX  X",
    "X  X  X  X        X  X        X",
    "X  X  X  X        X  X        X",
    "X  X  X  X  XXXXXXX  XXXXXXX  X",
    "X  X     X        X           X",
    "X  X     X        X           X",
    "XXXXXXXXXXXXXXXX  XXXXXXXXXXXXX"
  ]
  map(m1[::-1])
  return m1

def drawBall():
  glPointSize(5)
  glColor3f(1, 0, 0)
  for i in range(10):
    midpointCircle(295, 625, i)


def translation(x, y, dx, dy):
    t = np.array([[1, 0, dx],
                  [0, 1, dy],
                  [0, 0, 1]])
    v1 = np.array([[x],
                   [y],
                   [1]])
    v11 = np.matmul(t, v1)
    return v11[0][0], v11[1][0]

def iterate():
  glViewport(0, 0, 800, 800)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(0.0, 1000, -50.0, 1000, 0.0, 1.0)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()


def showScreen():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()
  #############
  maze()
  drawBall()
  glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(900, 600)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Window")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

