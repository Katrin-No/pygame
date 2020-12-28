import pygame
import sys
pygame.init()

size = [650, 650] # razmer okna
screen = pygame.display.set_mode(size) # vysyvaem metod set_mode i peredae:m emy spisok 4isel size
pygame.display.set_caption('kleto4ki') # s pom. etogo metoda mozhem zadat' zagolovok
width = heigth = 16
BLACK = (1, 1, 1)
FRAME_COLOR = (115, 179, 228)
WHITE = (250, 228, 228)
MARGIN = 1
mas = [[0]*38 for i in range(38)] #generator spiskov

while True:
    for event in pygame.event.get(): #zikl dlja obrabotki sobytij
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: #esli nazhali myshkoy
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print (f'x={x_mouse}, y={y_mouse}')

            column = x_mouse//(MARGIN + width)
            row = y_mouse//(MARGIN + heigth)
            mas[row][column] ^= 1 #1 eto prisnak togo, 4to zvet bydet drugoj

    screen.fill(FRAME_COLOR) #raskrasim ekram

    for row in range(38):
        for col in range(38): #risuem kleto4ki
            if mas[row][col] == 1:
                color = BLACK
            else:
                color = WHITE

            x = col * width + (col + 1) * MARGIN
            y = row * heigth + (row + 1) * MARGIN
            pygame.draw.rect(screen, color, (x, y, width, heigth))

    pygame.display.update() # primenjaet vse: 4to mnarisovali na ekrane
