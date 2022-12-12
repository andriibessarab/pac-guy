import pygame
import math

from board import boards

pygame.init()

WIDTH, HEIGHT = 900, 950  # W & H of app
FPS = 60

BORDER_COLOR = (199, 36, 177)
PELLETS_COLOR = (224, 231, 34)
PI = math.pi

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 20)
level = boards[0]


def draw_board(lvl):
    num1 = ((HEIGHT - 50) // 32)
    num2 = ((WIDTH - 50) // 30)

    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            b = level[i][j]
            if b == 1:
                pygame.draw.circle(screen, PELLETS_COLOR, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if b == 2:
                pygame.draw.circle(screen, PELLETS_COLOR, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if b == 3:
                pygame.draw.line(screen, BORDER_COLOR, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if b == 4:
                pygame.draw.line(screen, BORDER_COLOR, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if b == 5:
                pygame.draw.arc(screen, BORDER_COLOR, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if b == 6:
                pygame.draw.arc(screen, BORDER_COLOR,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if b == 7:
                pygame.draw.arc(screen, BORDER_COLOR, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if b == 8:
                pygame.draw.arc(screen, BORDER_COLOR,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if b == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)


run = True
while run:
    timer.tick(FPS)
    screen.fill("black")
    draw_board(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
