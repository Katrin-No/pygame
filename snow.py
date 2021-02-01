import pygame
import random

pygame.init()

bgColor = (135, 206, 250)  # blue
snowColor = (255, 255, 255)
gravity = 0.5  # speed
width = 1280
height = 980
snowSize = 3
snowNum = 2000

#sizeRails = [900, 980]
#sizelSm = [1280, 980]
#sizeSm = [1200, 980]
rails = pygame.image.load("rails.png")
lSm = pygame.image.load("lSm.png")
sm = pygame.image.load("sm.png")
bg = lSm


# game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('let it snow')

# coordinates for snowflakes
snowFlake = []
for q in range(snowNum):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    snowFlake.append([x, y])

# x-button
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()

    # screen.fill(bgColor)
    screen.blit(bg, [0, 0])

    # move snowflake downwards
    for i in snowFlake:
        i[1] += gravity  # if -= than it moves upwards

        pygame.draw.circle(screen, snowColor, i, snowSize)

        if i[1] > height:
            i[1] = random.randrange(-50, -5)  # sets y-value to random
            i[0] = random.randrange(width)  # sets x-value to random

    pygame.display.flip()

# https://www.youtube.com/watch?v=Quof1cOsaOw
