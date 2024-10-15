import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Define the vertices, edges and surfaces of a cube
vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Back edges
    (4, 5), (5, 6), (6, 7), (7, 4),  # Front edges
    (0, 4), (1, 5), (2, 6), (3, 7)   # Side edges
]

surfaces = [
    (0, 1, 2, 3),  # Back
    (4, 5, 6, 7),  # Front
    (0, 4, 5, 1),  # Right
    (2, 6, 7, 3),  # Left
    (0, 4, 7, 3),  # Top
    (1, 5, 6, 2)   # Bottom
]

colors = [
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 1, 0),  # Yellow
    (1, 0, 1),  # Purple
    (0, 1, 1)   # Cyan
]

def draw_cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        color_index = surfaces.index(surface)
        glColor3fv(colors[color_index])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))  # Black for edges
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def rotate_cube(cube_rotation):
    glRotatef(cube_rotation[0], 1, 0, 0)  # Rotate around x-axis
    glRotatef(cube_rotation[1], 0, 1, 0)  # Rotate around y-axis
    glRotatef(cube_rotation[2], 0, 0, 1)  # Rotate around z-axis

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()
    cube_rotation = np.array([0.0, 0.0, 0.0])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            cube_rotation[1] -= 1
        if keys[K_RIGHT]:
            cube_rotation[1] += 1
        if keys[K_UP]:
            cube_rotation[0] -= 1
        if keys[K_DOWN]:
            cube_rotation[0] += 1
        if keys[K_q]:
            cube_rotation[2] -= 1
        if keys[K_e]:
            cube_rotation[2] += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        rotate_cube(cube_rotation)
        draw_cube()
        glPopMatrix()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
