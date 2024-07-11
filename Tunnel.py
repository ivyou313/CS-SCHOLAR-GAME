
import math

import pygame.mouse
from pgzrun import *

WIDTH = 600
HEIGHT = 600

X0 = WIDTH // 2
Y0 = HEIGHT // 2

COUNT_CIRCLES = 100                     # Total number of circles in the tunnel
STEP_RADIUS = 10                         # Space between circles
STEP_COLOR = (255-50) / COUNT_CIRCLES    # Brightness of the circles? 

# a list containing ellipses, each element of this list is also
# list of numbers representing center coordinates, radius and tint:
# [X, Y, RADIUS, COLOR]
сircles = []

for i in range(0, COUNT_CIRCLES):
    сircles.append([WIDTH // 2, HEIGHT // 2, 100, 50])

def draw_circle(circle):
    angle = 0                   # Angle of movement along the ellipse to draw the next point.
    step = math.pi / 100    # Step with which the points of the ellipse are drawn.

    circle_x = circle[0]
    circle_y = circle[1]
    circle_r = circle[2]
    circle_color = circle[3]

    while angle < math.pi * 2:
        x = round(circle_x + math.sin(angle) * circle_r)
        y = round(circle_y + math.cos(angle) * circle_r // 1.5)

        if 0 < x < WIDTH and 0 < y < HEIGHT:
            screen.draw.filled_circle((x, y), 2, (0, circle_color, circle_color))

        angle += step

def update():
    pass

rotation_angle = 0

def draw():
    global rotation_angle

    screen.fill((74, 170, 100))

    for i in range(len(сircles) - 2, -1, -1):
        circle = сircles[i]

        circle[2] += STEP_RADIUS
        circle[3] += STEP_COLOR
        сircles[i + 1] = circle

        draw_circle(circle)

    # Calculating X, Y coordinates for a new circle (Changes how much the tunnel rorates)
    rotation_angle += 0.05
    x = X0 + math.sin(rotation_angle) * 10.0
    y = Y0 + math.cos(rotation_angle) * 1.0

    # Add a new circle to the beginning of the list
    сircles[0] = [x, y, 100, 50]

go()
