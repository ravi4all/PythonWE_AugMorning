import pygame

pygame.init()

width = 1000
height = 500

# rgb - 0-255
black = 0,0,0
white = 255,255,255
red = 255,0,0
blue = 0,0,255
color_1 = 100,150,99

screen = pygame.display.set_mode((width, height))

x = 0
y = 0

moveX = 1
moveY = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(color_1)

    pygame.draw.circle(screen, red, [x,y], 50)
    x += moveX
    y += moveY

    if x > width - 50:
        moveX = -1
    elif y > height - 50:
        moveY = -1
    elif x < 50:
        moveX = 1
    elif y < 50:
        moveY = 1

    pygame.display.update()