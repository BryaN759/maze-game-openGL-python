from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import keyboard
import numpy as np
import math

print("Press enter to start the game!")

def addPixel(a, b):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(a+(900/2), b+(400/2))
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


def maze():
  glColor3f(0, 0, 1)
  printLine(400, 200, -330, 200)
  printLine(400, 200, 400, -200)
  printLine(-400, 200, -400, -200)
  printLine(330, -200, -400, -200)
  printLine(330, -200, -400, -200)
  printLine(400, 40, 330, 40)
  printLine(330, 40, 330, -60)
  printLine(330, -200, -400, -200)
  printLine(250, -125, 400, -125)
  printLine(80, 200, 80, 120)
  printLine(160, -50, 160, -125)
  printLine(0, -125, 160, -125)
  printLine(0, -50, 0, -125)
  printLine(80, -200, 80, -125)
  printLine(-70, 120, 0, 120)
  printLine(0, 120, 0, 40)
  printLine(70, 40, 0, 40)
  printLine(70, 40, 70, -50)
  printLine(70, -50, 250, -50)
  printLine(250, -50, 250, 120)
  printLine(250, 120, 160, 120)
  printLine(160, 120, 160, 30)
  printLine(-330, -40, -400, -40)
  printLine(-80, -200, -80, -130)
  printLine(-320, -120, -160, -120)
  printLine(-160, -120, -160, -50)
  printLine(-160, -50, -80, -50)
  printLine(-80, -50, -80, 40)
  printLine(-80, 40, -240, 40)
  printLine(-240, 40, -240, -50)
  printLine(-170, 200, -170, 40)
  printLine(-170, 40, -310, 40)
  printLine(-310, 40, -310, 120)
  printLine(-310, 120, -250, 120)
  printLine(250, 120, 340, 120)


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

s = 0
def ballPos():
  global s
  n = keyboard.read_key()
  if n == 'enter' and s == 0:
    print("Game Starts!")
  elif n == 's' and s == 0:
    s = 1
  elif n == 'd' and s == 1:
    s = 2
  elif n == 's' and s == 1:
    s = 5
  elif n == 'a' and s == 2:
    s = 1
  elif n == 's' and s == 2:
    s = 3
  elif n == 'w'and s == 3:
    s = 2
  elif n == 'a' and s == 3:
    s = 4
  elif n == 'd' and s == 4:
    s = 3
  elif n == 'w' and s == 5:
    s = 1
  elif n == 'd' and s == 5:
    s = 6
  elif n == 'a' and s == 6:
    s = 5
  elif n == 's' and s == 6:
    s = 7
  elif n == 'w' and s == 7:
    s = 6
  elif n == 'd' and s == 7:
    s = 8
  elif n == 'a' and s == 7:
    s = 11
  elif n == 'a' and s == 8:
    s = 7
  elif n == 'w' and s == 8:
    s = 9
  elif n == 's' and s == 9:
    s = 8
  elif n == 'd' and s == 9:
    s = 10
  elif n == 'a' and s == 10:
    s = 9
  elif n == 'd' and s == 11:
    s = 7
  elif n == 's' and s == 11:
    s = 12
  elif n == 'w' and s == 12:
    s = 11
  elif n == 'd' and s == 12:
    s = 13
  elif n == 'a' and s == 13:
    s = 12
  elif n == 'w' and s == 13:
    s = 14
  elif n == 's' and s == 14:
    s = 13
  elif n == 'd' and s == 14:
    s = 15
  elif n == 'a' and s == 15:
    s = 14
  elif n == 's' and s == 15:
    s = 16
  elif n == 'w' and s == 15:
    s = 18
  elif n == 'w' and s == 16:
    s = 15
  elif n == 'd' and s == 16:
    s = 17
  elif n == 'a' and s == 17:
    s = 16
  elif n == 's' and s == 18:
    s = 15
  elif n == 'd' and s == 18:
    s = 19
  elif n == 'w' and s == 18:
    s = 22
  elif n == 'a' and s == 19:
    s = 18
  elif n == 's' and s == 19:
    s = 20
  elif n == 'w' and s == 20:
    s = 19
  elif n == 'd' and s == 20:
    s = 21
  elif n == 'a' and s == 21:
    s = 20
  elif n == 's' and s == 22:
    s = 18
  elif n == 'a' and s == 22:
    s = 23
  elif n == 'd' and s == 23:
    s = 22
  elif n == 'w' and s == 23:
    s = 24
  elif n == 's' and s == 24:
    s = 23
  elif n == 'd' and s == 24:
    s = 25
  elif n == 'a' and s == 25:
    s = 24
  elif n == 's' and s == 25:
    s = 26
  elif n == 'w' and s == 26:
    s = 25
  elif n == 'd' and s == 26:
    s = 27
  elif n == 'a' and s == 27:
    s = 26
  elif n == 's' and s == 27:
    s = 28
  elif n == 'w' and s == 27:
    s = 31
  elif n == 'w' and s == 28:
    s = 27
  elif n == 'd' and s == 28:
    s = 29
  elif n == 'a' and s == 29:
    s = 28
  elif n == 'w' and s == 29:
    s = 30
  elif n == 's' and s == 30:
    s = 29
  elif n == 's' and s == 31:
    s = 27
  elif n == 'd' and s == 31:
    s = 32
  elif n == 'a' and s == 32:
    s = 31
  elif n == 's' and s == 32:
    s = 33
  elif n == 'w' and s == 33:
    s = 32
  elif n == 'a' and s == 33:
    s = 34
  elif n == 'd' and s == 34:
    s = 33
  elif n == 's' and s == 34:
    s = 35
  elif n == 'w' and s == 35:
    s = 34
  elif n == 'd' and s == 35:
    s = 36
  elif n == 'a' and s == 35:
    s = 38
  elif n == 'a'and s == 36:
    s = 35
  elif n == 'w' and s == 36:
    s = 37
  elif n == 's' and s == 37:
    s = 36
  elif n == 'd' and s == 38:
    s = 35
  elif n == 's' and s == 38:
    s = 39
  elif n == 'w' and s == 39:
    s = 38
  elif n == 'a' and s == 39:
    s = 40
  elif n == 'd' and s == 39:
    s = 41
  elif n == 'd' and s == 40:
    s = 39
  elif n == 'a' and s == 41:
    s = 39
  elif n == 's' and s == 41:
    s = 42
  elif n == 'esc':
    print("The game has been terminated!")
    glutLeaveMainLoop()
  else:
    print("Invalid direction!")
  ballDraw(s)
  if s == 42:
    print("You have reached the goal!")
    glutLeaveMainLoop()


def ballDraw(s):
    statePos = {
      0: [-365, 200], 1: [-361, 156], 2: [-211, 160], 3: [-210, 90], 4: [-267, 80],
      5: [-355, 10], 6: [-285, -5], 7: [-285, -77], 8: [-205, -77], 9: [-197, -15],
      10: [-125, -1], 11: [-360, -86], 12: [-357, -158], 13: [-120, -160], 14: [-120, -98],
      15: [-43, -88], 16: [-38, -160], 17: [37, -163], 18: [-33, -8], 19: [30, -10],
      20: [43, -82], 21: [118, -85], 22: [-37, 75], 23: [-127, 80], 24: [-122, 152],
      25: [40, 157], 26: [45, 82], 27: [117, 77], 28: [120, -8], 29: [205, -5],
      30: [208, 70], 31: [130, 163], 32: [362, 158], 33: [362, 83], 34: [295, 78],
      35: [290, -87], 36: [367, -82], 37: [364, -1], 38: [205, -94], 39: [205, -159],
      40: [122, -164], 41: [360, -167], 42: [368, -230]
    }
    dx = statePos[s][0] - statePos[0][0]
    dy = statePos[s][1] - statePos[0][1]
    x , y = statePos[0][0], statePos[0][1]
    xPos, yPos = translation(x, y, dx, dy)
    glColor3f(1, 0, 0)
    for i in range(15):
      midpointCircle(xPos, yPos, i)


def translation(x, y ,dx, dy):
    t = np.array([[1, 0, dx],
                  [0, 1, dy],
                  [0, 0, 1]])
    v1 = np.array([[x],
                   [y],
                   [1]])
    v11 = np.matmul(t, v1)
    return v11[0][0],v11[1][0]

def scaling(x , y, sc):
    s = np.array([[sc, 0, 0],
                  [0, sc, 0],
                  [0, 0, 1]])
    v1 = np.array([[x],
                   [y],
                   [1]])
    v11 = np.matmul(s, v1)
    return v11[0][0], v11[1][0]

def rotation(x, y, a):
    cos = math.cos(math.radians(a))
    sin = math.sin(math.radians(a))
    r = np.array([[cos, -sin, 0],
                  [sin, cos, 0],
                  [0, 0, 1]])
    v1 = np.array([[x],
                   [y],
                   [1]])
    v11 = np.matmul(r, v1)
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
  ballPos()

  glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(900, 400)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Window")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

