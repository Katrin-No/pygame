import pygame
import sys
import random
pygame.init() #bez nego byla oshibka so shriftom

SIZE_BLOCK = 30 # razmer kwadrata
FRAME_COLOR = (52,66,56) #(1, 255, 204)
BLUE = (84, 148, 101)#(63, 202, 125)#(204, 255, 255)
WHITE = (52,66,66) #(255, 255, 255)
SNAKE_COLOR = (103, 58, 183) #(1, 102, 1)
RED = (244,67,54)

size = [690, 750] # razmer okna
COUNT_BLOCKS = 20
MARGIN = 1

#sozdae:m okno i sohranjaem ego v peremennuju
screen = pygame.display.set_mode(size) # vysyvaem metod set_mode i peredae:m emy spisok 4isel size
pygame.display.set_caption('zmejka') # s pom. etogo metoda mozhem zadat' zagolovok
timer = pygame.time.Clock()

class SnakeBlock:
    def __init__(self, x, y): #pri sozdanii objekta etogo klassa budem sohranjat' x i y
        self.x = x
        self.y = y

    def is_inside(self):
         return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

def get_random_empty_block():
    x = random.randint(0, COUNT_BLOCKS -1)
    y = random.randint(0, COUNT_BLOCKS -1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCKS -1)
        empty_block.y = random.randint(0, COUNT_BLOCKS -1)
    return empty_block

def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [30 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     80 + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK, SIZE_BLOCK]) #risuem kwadratiki polja, levaja verhnjaja to4ka (x,y) i rasmer kwadratika

snake_blocks = [SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)]
apple = get_random_empty_block()
d_row = 0
d_col = 1
total = 0 #podc4e: o4kov
courier = pygame.font.SysFont('courier', 36) #ssylka na shrift

# 4toby okno ne zakryvalos' cozdae:m beskone4ny zikl
while True:
    for event in pygame.event.get(): # zikl dlja obrabotki sobytij
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
        elif event.type == pygame.KEYDOWN: # peremeshhenie zmejki
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR) #raskrasim ekram

    text_total = courier.render(f"Total: {total}", 0, SNAKE_COLOR) #sozdae:m tekst, shrift, obtekanie, razmer, zvet
    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK)) #raspolagaem tekst na ekrane

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0: #proverka 4e:tnosti
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, column)

    head = snake_blocks[-1]
    if not head.is_inside():
        print('crush')
        pygame.quit()
        sys.exit () #zakroetsja programma
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    draw_block(RED, apple.x, apple.y)
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    if apple == head:
        total += 1
        snake_blocks.append(apple)
        apple = get_random_empty_block()

    new_head = SnakeBlock (head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head) #dobavljaem novuju golowu v spisok
    snake_blocks.pop(0) #ubiraem poslednij blok zmejki, a konez zmeiki u nas na index 0

    pygame.display.flip() # primenjaet vse: 4to mnarisovali na ekrane
    timer.tick(7)
