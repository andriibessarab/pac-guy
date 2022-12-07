import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 1024  # W & H of app
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 20)

run = True
while run:
    timer.tick(FPS)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()