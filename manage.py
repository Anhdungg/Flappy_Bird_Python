import pygame
import time
from pynput import keyboard

SIZE = WIDTH, HEIGHT = 288, 512
FPS = 60
POS_Y_BIRD_UP = 150
ICON = pygame.image.load("sprites/bird.png")
ICON.convert
BACKGROUND_MAIN = pygame.image.load("sprites/background-day.png")
BACKGROUND_MAIN.convert
BACKGROUND_BEGIN = pygame.image.load("sprites/message.png")
BACKGROUND_BEGIN.convert
BIRTH_RED = [pygame.image.load("sprites/bluebird-upflap.png"), pygame.image.load("sprites/bluebird-midflap.png"), 
pygame.image.load("sprites/bluebird-downflap.png")]
FLOOR_IMAGE = pygame.image.load("sprites/base.png")
FLOOR_IMAGE.convert
CLOCK = pygame.time.Clock()

X = 30
Y = 50

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_icon(ICON)
pygame.display.set_caption("Flappy Bird")

def begin():
    statusRun = True
    rect = BACKGROUND_BEGIN.get_rect()
    rect.center = WIDTH//2, HEIGHT//2
    while statusRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        screen.blit(BACKGROUND_BEGIN, rect)
        pygame.display.update()
        CLOCK.tick(FPS)

def main():
    if not begin():
        pygame.quit()
        return
    statusRun = True
    statusKeyDown = False
    countImageBird = 0
    posYBird = 50
    countPosXFloor = 0
    count=2
    while(statusRun):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                statusRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Y = posYBird - POS_Y_BIRD_UP
                    statusKeyDown = True
                    count = 10 
                if event.key == pygame.K_ESCAPE:
                    statusRun = False
        if statusKeyDown :
            if posYBird>Y:
                posYBird = posYBird - count
                if posYBird < 0:
                    posYBird = 0
                    statusKeyDown = False
                    count = 2
                count = abs(count-0.32)
            else:
                statusKeyDown = False
                count = 2 
        else:
            if posYBird<375:
                posYBird+=count
                count+=0.5
            else:
                count = 10

        countPosXFloor-=1
        countImageBird+=1
        if countImageBird>17:
            countImageBird=0
        if countPosXFloor < -48:
            countPosXFloor = 0
        screen.blit(BACKGROUND_MAIN, (0,0))
        screen.blit(BIRTH_RED[int(countImageBird/6)], (X,posYBird))
        screen.blit(FLOOR_IMAGE, (countPosXFloor, 400))
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()

main()