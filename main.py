import math

import pygame

from board import boards

pygame.init()

WIDTH, HEIGHT = 900, 950  # W & H of app
FPS = 60

BORDER_COLOR = (199, 36, 177)
GHOST_BORDER_COLOR = (255, 173, 0)
PELLETS_COLOR = (224, 231, 34)
PI = math.pi

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 20)
level = boards[0]

# PLAYER
PLAYER_IMGS = []
for i in range(1, 5):
    PLAYER_IMGS.append(pygame.transform.scale(pygame.image.load(f"assets/guy/{i}.png"), (45, 45)))
player_x = 450
player_y = 663

direction = 0
counter = 0
flicker = True


# Draw level's board
def draw_board(lvl):
    num1 = ((HEIGHT - 50) // 32)
    num2 = ((WIDTH - 50) // 30)

    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            b = level[i][j]
            if b == 1:
                pygame.draw.circle(screen, PELLETS_COLOR, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if b == 2 and not flicker:
                pygame.draw.circle(screen, PELLETS_COLOR, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if b == 3:
                pygame.draw.line(screen, BORDER_COLOR, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if b == 4:
                pygame.draw.line(screen, BORDER_COLOR, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if b == 5:
                pygame.draw.arc(screen, BORDER_COLOR,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if b == 6:
                pygame.draw.arc(screen, BORDER_COLOR,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if b == 7:
                pygame.draw.arc(screen, BORDER_COLOR,
                                [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if b == 8:
                pygame.draw.arc(screen, BORDER_COLOR,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if b == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)


# Draw pacguy
def draw_player():
    if direction == 0:  # RIGHT
        screen.blit(PLAYER_IMGS[counter // 5], (player_x, player_y))
    elif direction == 1:  # LEFT
        screen.blit(pygame.transform.flip(PLAYER_IMGS[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:  # UP
        screen.blit(pygame.transform.rotate(PLAYER_IMGS[counter // 5], 90), (player_x, player_y))
    elif direction == 3:  # DOWN
        screen.blit(pygame.transform.rotate(PLAYER_IMGS[counter // 5], -90), (player_x, player_y))


run = True
while run:
    timer.tick(FPS)
    counter = counter + 1 if counter < 19 else 0
    flicker = True if 3 <= counter <= 5 else False
    screen.fill("black")
    draw_board(level)
    draw_player()

    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            run = False

        # Movement controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3

    pygame.display.flip()

pygame.quit()
