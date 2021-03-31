import pygame

SIZE = WIDTH, HEIGHT = 500, 600
FPS = 30
ICON = pygame.image.load("sprites/bird.png")
BACKGROUND_MAIN = (32, 176, 186)
CLOCK = pygame.time.Clock()

X = 50
Y = 400

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_icon(ICON)
pygame.display.set_caption("Flappy Bird")

statusRun = True
while(statusRun):
    screen.fill(BACKGROUND_MAIN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            statusRun = False

    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()