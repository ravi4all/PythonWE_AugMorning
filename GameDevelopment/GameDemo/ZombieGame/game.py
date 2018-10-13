import pygame, random
from pygame.locals import *
import level_2

pygame.init()

width = 1000
height = 500

yellow = 255,255,0
black = 0,0,0
red = 255,0,0

screen = pygame.display.set_mode((width, height))

zombieList = []
for i in range(4):
    image = pygame.image.load("zombie_{}.png".format(i+1))
    zombieList.append(image)
bgImage = pygame.image.load("background.png")
gun_aim = pygame.image.load("aim_pointer.png")
gun = pygame.image.load("gun.png")

shotSound = pygame.mixer.Sound("shot_sound.wav")

def score(counter):
    red = 255,0,0
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score : {}".format(counter), True, red)
    screen.blit(text, (10,10))

def timer(seconds):
    red = 255,255,0
    font = pygame.font.SysFont(None, 40)
    text = font.render("Seconds : {}".format(seconds), True, red)
    screen.blit(text, (width  - 200,10))

def gameOver():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Game Over", True,yellow)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text, ((width/2)-200, 200))
        pygame.display.update()

def homeScreen():
    bg = pygame.image.load("homeBackground.jpg")
    font = pygame.font.SysFont(None, 70)
    text_1 = font.render("Welcome to Zombie Land", True,yellow)
    text_2 = font.render("Press SPACE to Kill Zombies", True, red)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(bg, (0,0))
        screen.blit(text_1, (150, 100))
        screen.blit(text_2, (150, 250))
        pygame.display.update()

def game():
    counter = 0
    gunAimWidth = gun_aim.get_width()
    gunAimHeight = gun_aim.get_height()

    gun_y = height - 200

    pygame.time.set_timer(USEREVENT, 1000)
    seconds = 20
    while True:
        zombieImage = random.choice(zombieList)
        zombieWidth = zombieImage.get_width()
        zombieHeight = zombieImage.get_height()

        random_x = random.randint(0, width - zombieWidth)
        random_y = random.randint(0, height - zombieHeight)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                shotSound.play()
                if rect_1.colliderect(rect_2):
                    counter += 1
                    zombieImage = random.choice(zombieList)
                    zombieWidth = zombieImage.get_width()
                    zombieHeight = zombieImage.get_height()

                    random_x = random.randint(0, width - zombieWidth)
                    random_y = random.randint(0, height - zombieHeight)

        pos_x, pos_y = pygame.mouse.get_pos()

        screen.blit(bgImage, (0,0))
        screen.blit(zombieImage, (random_x, random_y))
        screen.blit(gun_aim, (pos_x - gunAimWidth/2, pos_y - gunAimHeight/2))
        screen.blit(gun, (pos_x, gun_y))

        rect_1 = pygame.Rect(random_x, random_y, zombieWidth, zombieHeight)
        rect_2 = pygame.Rect(pos_x - gunAimWidth/2, pos_y - gunAimHeight/2, gunAimWidth, gunAimHeight)

        score(counter)
        timer(seconds)

        if seconds == 0:
            gameOver()
            break

        if counter == 10:
            level_2.game()

        pygame.display.update()

homeScreen()