import pygame
import random

SIZE = WIDTH, HEIGHT = 288, 512
FPS = 60
ICON = pygame.image.load("sprites/bird.png")
ICON.convert
BACKGROUND_MAIN_DAY = pygame.image.load("sprites/background-day.png")
BACKGROUND_MAIN_DAY.convert
BACKGROUND_MAIN_NIGHT = pygame.image.load("sprites/background-night.png")
BACKGROUND_MAIN_NIGHT.convert
BACKGROUND_BEGIN = pygame.image.load("sprites/message.png")
BACKGROUND_BEGIN.convert
BIRD_BLUE = [pygame.image.load("sprites/bluebird-upflap.png"), pygame.image.load("sprites/bluebird-midflap.png"), 
    pygame.image.load("sprites/bluebird-downflap.png")]
BIRD_RED = [pygame.image.load("sprites/redbird-upflap.png"), pygame.image.load("sprites/redbird-midflap.png"), 
    pygame.image.load("sprites/redbird-downflap.png")]
BIRD_YELLOW = [pygame.image.load("sprites/yellowbird-upflap.png"), pygame.image.load("sprites/yellowbird-midflap.png"), 
    pygame.image.load("sprites/yellowbird-downflap.png")]
BIRD = [BIRD_BLUE, BIRD_RED, BIRD_YELLOW]
SCORE_IMAGE = [pygame.image.load("sprites/0.png"), pygame.image.load("sprites/1.png"), pygame.image.load("sprites/2.png"), 
    pygame.image.load("sprites/3.png"), pygame.image.load("sprites/4.png"), pygame.image.load("sprites/5.png"), 
    pygame.image.load("sprites/6.png"), pygame.image.load("sprites/7.png"), pygame.image.load("sprites/8.png"), 
    pygame.image.load("sprites/9.png")]
FLOOR_IMAGE = pygame.image.load("sprites/base.png")
FLOOR_IMAGE.convert
GAME_OVER = pygame.image.load("sprites/gameover.png")
GAME_OVER.convert
PIPE_GREEN = pygame.image.load("sprites/pipe-green.png")
PIPE_GREEN.convert
PIPE_RED = pygame.image.load("sprites/pipe-red.png")
PIPE_RED.convert
PIPE = [PIPE_RED, PIPE_GREEN]
CLOCK = pygame.time.Clock()

pygame.mixer.init()
SOUND_POINT = pygame.mixer.Sound("sound/sfx_point.wav")
SOUND_DIED = pygame.mixer.Sound("sound/sfx_die.wav")
SOUND_HIT = pygame.mixer.Sound("sound/sfx_hit.wav")


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
        screen.blit(pygame.transform.rotate(self.pipe, 180), (self.posX, self.posY-(170+320)))

class Bird:
    def __init__(self, birdColor):
        self.bird = birdColor
        self.flightDistance = 100
        self.posX = 30
        self.posY = 100
        self.flapping = 0
        self.speed = 5
        self.statusFly = False
        self.topPosY = 0
        self.botPosY = 375

    def getPosY(self):
        return self.posY

    def setPosY(self, posY):
        self.posY = posY

    def getTopPosY(self):
        return self.topPosY 

    def setSpeed(self, speed):
        self.speed = speed

    def flyUp(self):
        self.topPosY = self.posY - self.flightDistance
        if self.topPosY < 0:
            self.topPosY = 0
        self.speed = 8
        self.botPosY = 375
        self.statusFly = True

    def fly(self):
        if self.statusFly:
            self.posY -= self.speed
            self.speed = self.speed-0.2
            if self.posY<0:
                self.posY = 0
            if self.speed<1:
                self.speed = 1
            if self.posY < self.topPosY or self.posY==0:
                self.speed = 4
                self.statusFly = False
        else:
            self.posY += self.speed
            self.speed = self.speed+0.2
            if self.posY>self.botPosY:
                self.posY = self.botPosY
        self.draw(self.animation())

    def animation(self):
        self.flapping +=1
        if self.flapping>17:
            self.flapping=0
        global newBird
        if self.statusFly:
            newBird = pygame.transform.rotate(self.bird[int(self.flapping/6)], 10)
        else:
            newBird = pygame.transform.rotate(self.bird[int(self.flapping/6)], -20)
        return newBird

    def draw(self, bird):
        screen.blit(bird, (self.posX,self.posY))
    
    def died(self):
        self.topPosY = self.posY - 150 
        if self.topPosY < 0:
            self.topPosY = 0
        self.speed = 8
        self.botPosY = 544
        self.statusFly = True

class Score:
    def __init__(self, image, sound):
        self.scoreImage = image
        self.sound = sound
        self.userScore = 0
        self.midWidth = 144
        self.posY = 50

    def setUserScore(self, userScore):
        self.userScore = userScore

    def getScore(self):
        return self.userScore

    def setPosY(self, posY):
        self.posY = posY

    def countScore(self):
        self.userScore += 1
        self.sound.play()

    def drawScore(self):
        temp =  str(self.userScore)
        arrScore = list(temp)
        temp = 0
        for score in arrScore:
            if score == "1":
                temp+=16
            else:
                temp+=24
        posX = temp/2
        for score in arrScore:
            screen.blit(self.scoreImage[int(score)], (self.midWidth - posX, self.posY))
            if score == "1":
                posX-=16
            else:
                posX-=24
           
class Floor:
    def __init__(self, image):
        self.image = image
        self.speed = 1
        self.posX = 0
        self.posY = 400

    def setSpeed(self, speed):
        self.speed = speed

    def animation(self):
        self.posX-=self.speed
        if self.posX < -48:
            self.posX = 0

    def stop(self):
        self.setSpeed(0)

    def draw(self):
        self.animation()
        screen.blit(self.image, (self.posX, self.posY))

def begin(score, statusBackgound):
    tempScore = str(score)
    statusRun = True
    rect = BACKGROUND_BEGIN.get_rect()
    rect.center = WIDTH//2, HEIGHT//2
    score = Score(SCORE_IMAGE, SOUND_POINT)
    score.setPosY(180)
    score.setUserScore(int(tempScore))
    while statusRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False
        if statusBackgound:
            screen.blit(BACKGROUND_MAIN_DAY, (0,0))
        else:
            screen.blit(BACKGROUND_MAIN_NIGHT, (0,0))
        screen.blit(BACKGROUND_BEGIN, rect)
        score.drawScore()
        pygame.display.update()
        CLOCK.tick(FPS)

def gameOver():
    screen.blit(GAME_OVER, (48, 166))

def main():
    if not begin(0, True):
        pygame.quit()
        return
    randomPipe = random.randrange(0,2)
    listPipe = [Pipe(PIPE[randomPipe])]
    bird = Bird(BIRD[random.randrange(0,3)])
    score = Score(SCORE_IMAGE, SOUND_POINT)
    floor = Floor(FLOOR_IMAGE)
    statusRun = True
    birdDead = False
    statusBackgound = True
    while(statusRun): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                statusRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    statusRun = False
                if event.key == pygame.K_SPACE:
                    if not birdDead:
                        bird.flyUp()
        if statusBackgound:
            screen.blit(BACKGROUND_MAIN_DAY, (0,0))
        else:
            screen.blit(BACKGROUND_MAIN_NIGHT, (0,0))
        if not birdDead:
            if listPipe[len(listPipe)-1].getPosX() < 100:
                listPipe.append(Pipe(PIPE[randomPipe]))
            for pipe  in listPipe:
                pipe.move()
                pipe.drawImage(screen)
            if listPipe[0].getPosX() <= -53:
                score.countScore() 
                if score.getScore() % 3 == 0:
                    statusBackgound = not statusBackgound
                listPipe.remove(listPipe[0])

            if listPipe[0].getPosX() <= 60 and listPipe[0].getPosX() >= -20:
                if bird.getPosY() + 32 > listPipe[0].getPosY() or bird.getPosY() < listPipe[0].getPosY()-170:
                    SOUND_HIT.play()
                    bird.died()
                    birdDead = True
        else:
            if bird.getPosY() < bird.getTopPosY() or bird.getPosY() == 0:
                SOUND_DIED.play()
            for pipe in listPipe:
                pipe.setSpeed(0)
                pipe.drawImage(screen)
            floor.setSpeed(0)
            gameOver()
            if bird.getPosY() >= 544:
                status = begin(score.getScore(), statusBackgound)
                if status:
                    randomPipe = random.randrange(0,2)
                    listPipe.clear()
                    listPipe = [Pipe(PIPE[randomPipe])]
                    bird = Bird(BIRD[random.randrange(0,3)])
                    score.setUserScore(0)
                    floor.setSpeed(1)
                    birdDead = False
                else:
                    return 
        score.drawScore()
        floor.draw()
        bird.fly()
        pygame.display.update()
        CLOCK.tick(FPS)
        
    pygame.quit()

main()