import OpenGL.GLUT
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

clicked = False


prop_r = 10
prop_theta = 0.0

car_d = 10

sun_radius = 600
sun_theta = 0.0

# smoke
sm = 0.0

moon_r = 0
moon_rad = 600
moon_theta = 0.0





def draw_points(x, y, pix):
    glPointSize(pix) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def findZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx >= 0 and dy >= 0:
        if dx >= dy:
            return 0
        else:
            return 1
    elif dx < 0 and dy >= 0:
        if -dx >= dy:
            return 3
        else:
            return 2
    elif dx < 0 and dy < 0:
        if dx <= dy:
            return 4
        else:
            return 5
    elif dx >= 0 and dy < 0:
        if dx >= -dy:
            return 7
        else:
            return 6

# ============ Draw Line ================= #
def drawLine(x1, y1, x2, y2, pix):
    zone = findZone(x1, y1, x2, y2)
    if zone == 0:
        x1, y1 = x1, y1
        x2, y2 = x2, y2
    elif zone == 1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    elif zone == 2:
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2
    elif zone == 3:
        x1, y1 = -x1, y1
        x2, y2 = -x2, y2
    elif zone == 4:
        x1, y1 = -x1, -y1
        x2, y2 = -x2, -y2
    elif zone == 5:
        x1, y1 = -y1, -x1
        x2, y2 = -y2, -x2
    elif zone == 6:
        x1, y1 = -y1, x1
        x2, y2 = -y2, x2
    elif zone == 7:
        x1, y1 = x1, -y1
        x2, y2 = x2, -y2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    x = x1
    y = y1
    while x <= x2:
        if zone == 0:
            draw_points(x, y, pix)
        elif zone == 1:
            draw_points(y, x, pix)
        elif zone == 2:
            draw_points(y, -x, pix)
        elif zone == 3:
            draw_points(-x, y, pix)
        elif zone == 4:
            draw_points(-x, -y, pix)
        elif zone == 5:
            draw_points(-y, -x, pix)
        elif zone == 6:
            draw_points(-y, x, pix)
        elif zone == 7:
            draw_points(x, -y, pix)
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + 2 * dy - 2 * dx
            y = y + 1
        x = x + 1

# def drawButton():
#     if clicked:
#         glColor3f(0.0, 1.0, 0.0)
#     else:
#         glColor3f(button_color[0], button_color[1], button_color[2])
#
#     # glColor3f(0.0, 1.0, 0.0)
#     # solidQuad(0, 0, 100, 0, 100, 100, 0, 100, 1)
#
#     glColor3f(*button_color)
#     glRectf(0, 0, 200, 200)
#
# def mouse_click(button, state, x, y):
#     global clicked
#     if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
#         if x > 0 and x < 200 and y > 0 and y < 200:
#             print("clicked")
#             clicked = not clicked
#             glutPostRedisplay()

def keyboard_callback(key, x, y):
    global clicked
    if key == b'q':
        clicked = not clicked
        print(clicked)
        glutPostRedisplay()


def drawline(x1, y1, x2, y2, pix):
    glPointSize(pix)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

# =============== circle =============== #
def drawCircle(xc, yc, x, y, pix, type = 1):
    draw_points(xc + x, yc + y, pix)
    draw_points(xc - x, yc + y, pix)
    draw_points(xc + x, yc - y, pix)
    draw_points(xc - x, yc - y, pix)
    draw_points(xc + y, yc + x, pix)
    draw_points(xc - y, yc + x, pix)
    draw_points(xc + y, yc - x, pix)
    draw_points(xc - y, yc - x, pix)

    if type:
        drawLine(xc + x, yc + y, xc - x, yc + y, pix)
        drawLine(xc + x, yc - y, xc - x, yc - y, pix)
        drawLine(xc + y, yc + x, xc - y, yc + x, pix)
        drawLine(xc + y, yc - x, xc - y, yc - x, pix)

def midPointCircle(xc, yc, r, pix, type = 1):
    x = 0
    y = r
    drawCircle(xc, yc, x, y, pix, type)
    d = 1 - r
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * (x - y) + 5
            x += 1
            y -= 1
        drawCircle(xc, yc, x, y, pix, type)



# ================ Solid quard ================

def solidQuad(x1, y1, x2, y2, x3, y3, x4, y4, pix):
    drawLine(x1, y1, x2, y2, pix)
    drawLine(x2, y2, x3, y3, pix)
    drawLine(x3, y3, x4, y4, pix)
    drawLine(x1, y1, x4, y4, pix)

    while x1 < x2:
        drawLine(x1, y1, x2, y2, pix)
        drawLine(x2, y2, x3, y3, pix)
        drawLine(x3, y3, x4, y4, pix)
        drawLine(x1, y1, x4, y4, pix)

        x1 += 1
        x2 -= 1
        x3 -= 1
        x4 += 1
        if y1 < y4:
            y1 += 1
            y2 += 1
            y3 -= 1
            y4 -= 1
def terbine(prop_theta, x, y):
    #turbine
    solidQuad(x, 200, x+5, 200, x+5, y, x, y, 2)
    midPointCircle(x+2, y, 5, 2)

    # propelar
    for i in range(3):
        blade_angle = prop_theta + i * 120  # Calculate the angle of the current blade
        x1 = abs(x+2 + prop_r * math.cos(blade_angle * math.pi / 180.0))  # Calculate the x coordinate of the blade
        y1 = abs(y + prop_r * math.sin(blade_angle * math.pi / 180.0) ) # Calculate the y coordinate of the blade
        x2 = abs(x+2 + (prop_r+50) * math.cos((blade_angle + 180) * math.pi / 180.0))  # Calculate the x coordinate of the blade
        y2 = abs(y + (prop_r+50) * math.sin((blade_angle + 180) * math.pi / 180.0))  # Calculate the y coordinate of the blade

        drawline(x1, y1, x2, y2, 10)

def tree(x, y):
    glColor4f(0, 34, 0, 0.82)
    solidQuad(x, 200, x + 20, 200,  x + 20, y, x, y, 2)

    glColor4f(0, 54, 0, 1)
    midPointCircle(x + 10,  y + 20, 40, 2)
    midPointCircle(x + 40, y + 20, 30, 2)
    midPointCircle(x - 30,  y + 20, 30, 2)
    midPointCircle(x + 10 , y + 60, 40, 2)

    # midPointCircle(240, 360, 30, 2)
    # midPointCircle(195, 360, 30, 2)

    midPointCircle(x + 40, y - 20, 30, 2)
    midPointCircle(x - 30, y - 20, 30, 2)


# quad House with windows
def house(x, y):
    glColor4f(0.00, 0.570, 0.580, 0.5)
    solidQuad(x, 200, x + 100, 200, x + 100, y, x, y, 2)
    # black color
    glColor3f(0.00, 0.00, 0.00)
    x1 = x
    y1 = y - 80
    # windows
    for i in range(5):
        solidQuad(x1 + 10 + i * 10, y1, x1 + 20 + i * 10, y1, x1 + 20 + i * 10, y1+30, x1 + 10 + i * 10, y1+30, 2)

        if x1 + 10 > x + 100:
            y1 = y - 40
            x1 = x
        x1 += 10

def house2(x, y, ys, w = 1):
    glColor4f(0.00, 0.570, 0.580, 0.5)
    solidQuad(x, 200-ys, x + 100, 200, x + 100, y+ys, x, y, 2)
    # black color
    glColor3f(0.00, 0.00, 0.00)
    # windows
    if w == 1:
        x1 = x
        y1 = y - 70
        for i in range(4):
            solidQuad(x1 + 10 + i * 10, y1, x1 + 20 + i * 10, y1, x1 + 20 + i * 10, y1+30, x1 + 10 + i * 10, y1+30, 2)

            if x1 + 10 > x + 100:
                y1 = y - 40
                x1 = x
            x1 += 10

        glColor4f(0, 204, 255, 0.64)
        for i in range(4):
            solidQuad(x1 + 10 + i * 10, y, x1 + 20 + i * 10, y, x1 + 20 + i * 10, y+30, x1 + 10 + i * 10, y+30, 2)

            x1 += 10

def house3(x, y, ys):
    glColor4f(0.00, 0.570, 0.580, 0.5)
    solidQuad(x, 200, x + 100, 200-ys, x + 100, y, x, y+ys, 2)
    solidQuad(x, 200, x + 100, 200, x + 100, y, x, y, 2)
    # black color
    glColor3f(0.00, 0.00, 0.00)
    # windows
    x1 = x
    y1 = y - 70
    for i in range(4):
        solidQuad(x1 + 10 + i * 10, y1, x1 + 20 + i * 10, y1, x1 + 20 + i * 10, y1+30, x1 + 10 + i * 10, y1+30, 2)

        if x1 + 10 > x + 100:
            y1 = y - 40
            x1 = x
        x1 += 10
    glColor4f(0, 204, 255, 0.64)
    for i in range(4):
        solidQuad(x1 + 10 + i * 10, y, x1 + 20 + i * 10, y, x1 + 20 + i * 10, y+30, x1 + 10 + i * 10, y+30, 2)

        x1 += 10

def house4(x, y):
    glColor4f(0.00, 0.570, 0.580, 0.5)
    solidQuad(x, 200, x + 100, 200, x + 100, y, x, y, 2)

    solidQuad(x+20, y, x + 80, y, x + 80, y+20, x+20, y+20, 2)

    solidQuad(x+45, y+20, x + 55, y+20, x + 55, y+60, x+45, y+60, 2)

# wearhouse
def wearhouse(x, y):
    glColor4f(0.00, 0.570, 0.580, 0.5)
    solidQuad(x, 200, x + 100, 200, x + 100, y, x, y, 2)
    # black color


    house2(x, y, 10, 0)
    house2(x+100, y, 10, 0)
    glColor4f(0.00, 0.570, 0.580, 0.5)
    solidQuad(x+200, 200, x + 230, 200, x + 230, y+100, x+200, y+100, 2)

    glColor3f(0.00, 0.00, 0.00)
    # smoke
    glColor4f(0.00, 0.570, 0.580, 0.5)

    midPointCircle(x + 215, y + 130, 13, 2)
    midPointCircle(x + 215, y + 150, 10, 2)
    midPointCircle(x + 215, y + 170, 5, 2)
    midPointCircle(x + 215, y + 175 + sm + 2, 2, 2)
    midPointCircle(x + 215, y + 180+sm + 2, 3, 2)
    midPointCircle(x + 215, y + 190+sm, 2, 2)




def drawCar(x, y):
    # move forward
    x += car_d

    # pink color
    glColor3f(0.00, 0.570, 0.580)
    # solidQuad(self.x, self.y, self.x + 100, self.y, self.x + 100, self.y + 40, self.x, self.y+40, 2)
    # solidQuad(self.x+15, self.y+40, self.x + 85, self.y+40, self.x + 85, self.y + 70, self.x+15, self.y + 70, 2)
    #remove self
    solidQuad(x, y, x + 100, y, x + 100, y + 40, x, y+40, 2)
    solidQuad(x+15, y+40, x + 85, y+40, x + 85, y + 70, x+15, y + 70, 2)

    #car window
    glColor3f(0.00, 0.00, 0.00)
    # solidQuad(self.x+20, self.y+45, self.x + 48, self.y+45, self.x + 48, self.y + 65, self.x+20, self.y + 65, 2)
    # solidQuad(self.x+52, self.y+45, self.x + 80, self.y+45, self.x + 80, self.y + 65, self.x+52, self.y + 65, 2)
    solidQuad(x+20, y+45, x + 48, y+45, x + 48, y + 65, x+20, y + 65, 2)
    solidQuad(x+52, y+45, x + 80, y+45, x + 80, y + 65, x+52, y + 65, 2)


    #car wheels
    glColor3f(0.00, 0.00, 0.00)
    # midPointCircle(self.x+20, self.y+5, 20, 2)
    # midPointCircle(self.x+80, self.y+5, 20, 2)
    midPointCircle(x+20, y+5, 20, 2)
    midPointCircle(x+80, y+5, 20, 2)


    # chrome color
    glColor3f(0.75, 0.75, 0.75)
    # midPointCircle(self.x+20, self.y+5, 10, 2)
    # midPointCircle(self.x+80, self.y+5, 10, 2)
    midPointCircle(x+20, y+5, 10, 2)
    midPointCircle(x+80, y+5, 10, 2)




        # car lights
    glColor3f(1.00, 1.00, 1.00)
    # solidQuad(self.x+10, self.y+40, self.x + 15, self.y+40, self.x + 15, self.y + 70, self.x+10, self.y + 70, 2)
    # solidQuad(self.x+85, self.y+40, self.x + 90, self.y+40, self.x + 90, self.y + 70, self.x+85, self.y + 70, 2)

    solidQuad(x+10, y+40, x + 15, y+40, x + 15, y + 70, x+10, y + 70, 2)
    solidQuad(x+85, y+40, x + 90, y+40, x + 90, y + 70, x+85, y + 70, 2)


def moon(x, y, r, pix, moon_theta):
    # white color
    x1 = x + moon_rad * math.cos(math.radians(moon_theta))
    y1 = y + moon_rad * math.sin(math.radians(moon_theta))

    glColor3f(1.00, 1.00, 1.00)
    midPointCircle(x1, y1, r, pix)


    # moon Glow in circle
    # golden white color
    glColor4f(1.00, 1.00, 0.00, 0.3)
    for i in range(5, 15, 5):
        midPointCircle(x1, y1, r + i, 2, 0)
        # faded white color
        glColor4f(1.00, 1.00, 1.00, 0.3)
        # midPointCircle(x, y, r + 10 + moon_r + i, 1, 0)
        midPointCircle(x1, y1, r + 10 + moon_r + i, 1, 0)



def sunRise(x, y, r, pix, theta):
    x = x + sun_radius * math.cos(math.radians(theta))
    y = y + sun_radius * math.sin(math.radians(theta))
    midPointCircle(x, y, r, pix)
    # sunshine

    for i in range(0, 360, 5):
        glColor3f(1.00, 1.00, 0.00)
        drawline(x, y, x + 50 * math.cos(math.radians(i)), y + 50 * math.sin(math.radians(i)), 2)



# def solarPanel():
#     solidQuad()



def iterate():
    glViewport(0, 0, 1920, 1080)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1920, 0.0, 1080, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()









def showScreen():
    global prop_theta
    global sun_theta
    global car_d
    global sm
    global moon_theta


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(0.00, 0.570, 0.580) #konokichur color set (RGB)
    glColor4f(0.00, 0.570, 0.580, 0.5)
    #call the draw methods here



    # sky

    if clicked:
        # black gradient
        glColor4f(0, 0, 0, 0.64)
        solidQuad(0, 0, 1920, 0, 1920, 1080, 0, 1080, 1)
    else:
        glColor4f(0, 204, 255, 0.64)
        solidQuad(0, 0, 1920, 0, 1920, 1080, 0, 1080, 1)


    # sun
    if not clicked:
        while moon_theta < 180.0:
            moon_theta += 10
        moon_theta = 0.0
        midPointCircle(700, 640,35, 3)
        sunRise(500, 0, 35, 3, sun_theta)

        if sun_theta < 90.0:
            sun_theta += 10

    if clicked:
        while sun_theta < 180.0:
            sun_theta += 10
        sun_theta = 0.0
    # moon
        moon(500, 0, 35, 3, moon_theta)

        if moon_theta < 90.0:
            moon_theta += 10





    # terbine
    # pink color
    glColor3f(1.00, 0.00, 0.00)
    terbine(prop_theta, 100, 300)
    prop_theta += 10
    if prop_theta > 360.0:
        prop_theta = 0.0

    # terbine2
    # pink color
    glColor3f(1.00, 0.00, 0.00)
    terbine(prop_theta, 120, 400)
    # prop_theta += 10
    # if prop_theta > 360.0:
    #     prop_theta = 0.0

    # tree
    tree(200, 300)

    # house
    house(300, 400)

    # house2
    house2(450, 400, 20)

    # house4
    house4(575, 420)

    # house3
    house3(700, 400, 20)


    # wearhouse
    wearhouse(850, 300)
    sm += 5
    if sm > 50:
        sm = 0

    #
    tree(870, 350)


    # Road
    # grey color
    roadcolor = [0.50, 0.50, 0.50]
    glColor3f(*roadcolor)
    solidQuad(0, 0, 1920, 10, 1920, 200, 0, 200, 3)

    # Car

    drawCar(100, 100)

    car_d += 10

    # drawButton()

    midPointCircle()



    glutSwapBuffers()





glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1920, 1080) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Project") #window name
glClearColor(0.0, 0.0, 0.0, 0.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()

# glutMouseFunc(mouse_click)
glutDisplayFunc(showScreen)

glutKeyboardFunc(keyboard_callback)

glutIdleFunc(showScreen)




glutMainLoop()

