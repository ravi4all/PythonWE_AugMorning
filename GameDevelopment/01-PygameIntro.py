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

while True:
    screen.fill(color_1)
    pygame.display.update()