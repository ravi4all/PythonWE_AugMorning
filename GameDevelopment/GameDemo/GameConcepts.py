import pygame

pygame.init()

width = 1000
height = 500

# rgb - 0-255
black = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode((width, height))

image_1 = pygame.image.load("image_1.png")
image_2 = pygame.image.load("image_1.png")

charImage_1 = pygame.image.load("m1.png")
charImage_2 = pygame.image.load("m2.png")

currentImage = charImage_1

bg_x = 0
bg_y = 0

bg_2x = width

moveX = 0
moveY = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = -1

    screen.fill(white)
    screen.blit(image_1, (bg_x,bg_y))
    screen.blit(image_2, (bg_2x, 0))

    bg_x += moveX
    bg_2x += moveX

    if currentImage == charImage_2:
        screen.blit(charImage_1, (200,365))
        currentImage = charImage_1
    elif currentImage == charImage_1:
        screen.blit(charImage_2, (200, 365))
        currentImage = charImage_2

    if bg_x < -width:
        bg_x = width
    elif bg_2x < -width:
        bg_2x = width

    pygame.display.update()