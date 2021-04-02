import pygame
import random

SIZE = WIDTH, HEIGHT = 288, 512
FPS = 60
POS_BIRD_UP = 100
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
GAME_OVER = pygame.image.load("sprites/gameover.png")
GAME_OVER.convert
PIPE_GREEN = pygame.image.load("sprites/pipe-green.png")
PIPE_GREEN.convert
PIPE_RED = pygame.image.load("sprites/pipe-red.png")
PIPE_RED.convert
CLOCK = pygame.time.Clock()


countImageFloor = 0
countImageBird = 0

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_icon(ICON)
pygame.display.set_caption("Flappy Bird")

class Pipe:
    def __init__(self, image):
        self.pipe = image
        self.posX = 288
        self.posY = random.randrange(175, 375)
        self.speedMove = 2

    def getPosX(self):
        return self.posX

    def setPosX(self, posX):
        self.posX = posX

    def getPosY(self):
        return self.posY

    def setPosY(self, posY):
        self.posY = posY

    def getImage(self):
        return self.pipe

    def setSpeed(self, speed):
        self.speedMove = speed
    
    def getSpeed(self):
        return self.speedMove

    def move(self):
        if self.posX > -53:
            self.posX-=self.speedMove

    def drawImage(self, screen):
        screen.blit(self.pipe, (self.posX, self.posY))
        screen.blit(pygame.transform.rotate(self.pipe, 180), (self.posX, self.posY-(150+320)))


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


def animatedFloor():
    global countImageFloor
    countImageFloor-=1
    if countImageFloor < -48:
        countImageFloor = 0
    screen.blit(FLOOR_IMAGE, (countImageFloor, 400))

def animatedBird(posBirdUp):
    global countImageBird
    countImageBird+=1
    if countImageBird>17:
        countImageBird=0
    screen.blit(BIRTH_RED[int(countImageBird/6)], (30,posBirdUp))

def gameOver(statusKeyDown):
    screen.blit(GAME_OVER, (48, 48))
    if statusKeyDown:
        pass

def main():
    if not begin():
        pygame.quit()
        return
    list = [Pipe(PIPE_GREEN)]
    statusRun = True
    statusKeyDown = False
    posBirdUp = 50
    dropBird = 0
    topBirdUp = 0
    while(statusRun): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                statusRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    statusRun = False
                if event.key == pygame.K_SPACE:
                    topBirdUp = posBirdUp - POS_BIRD_UP
                    statusKeyDown = True
                    dropBird = 10 
        if statusKeyDown :
            if posBirdUp>topBirdUp:
                posBirdUp -= dropBird
                if posBirdUp < 0:
                    posBirdUp = 0
                    statusKeyDown = False
                    dropBird = 2
                dropBird = dropBird-0.2
                if dropBird < 1:
                    dropBird = 1
            else:
                statusKeyDown = False
                dropBird = 2 
        else:
            if posBirdUp<375:
                posBirdUp+=dropBird
                dropBird+=0.2
            else:
                dropBird = 10
        screen.blit(BACKGROUND_MAIN, (0,0))
        if list[len(list)-1].getPosX() < 100:
            list.append(Pipe(PIPE_GREEN))
        for pipe  in list:
            pipe.setSpeed(5)
            pipe.move()
            pipe.drawImage(screen)
        if list[0].getPosX() <= -53:
            list.remove(list[0])
        animatedBird(posBirdUp)
        animatedFloor()
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()

main()