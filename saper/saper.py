import pygame
import os
from tkinter import messagebox
import time
import random
pygame.init()

# level = 'easy'

def image(name):
    return pygame.image.load(os.path.join("images", name + ".png"))
names = {}
names[0] = image("пусто")
names[1] = image("1")
names[2] = image("2")
names[3] = image("3")
names[4] = image("4")
names[5] = image("5")
names[6] = image("6")
names[7] = image("7")
names[8] = image("8")
names[9] = image("9")
names[-1] = image("бомба")
names[-2] = image("флажок")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SIZE = 50
MARGIN = 10
PADDING = 10
EMPTY = 0
BOMB = -1
MARK_BOMB = -2


def random_COUNT():
    x = SIZE_X
    y = SIZE_Y
    A = []
    for i in range(x+2):
        a_y=[]
        for j in range(y+2):
            a_y.append(0)
        A.append(a_y)
    an = 0
    while an != COUNT_BOMB:
        i = random.randint(1, x)
        j = random.randint(1, y)
        if A[i][j] == 0:
            A[i][j] = -1
            an += 1
    for i in range(1, x+1):
        for j in range(1, y+1):
            count = 0
            if A[i][j] != -1:
                if A[i - 1][j] == -1:
                    count+=1
                if A[i][j - 1] == -1:
                    count+=1
                if A[i + 1][j] == -1:
                    count+=1
                if A[i][j + 1] == -1:
                    count+=1
                if A[i - 1][j - 1] == -1:
                    count+=1
                if A[i + 1][j + 1] == -1:
                    count+=1
                if A[i - 1][j + 1] == -1:
                    count+=1
                if A[i + 1][j - 1] == -1:
                    count+=1
                A[i][j] = count
    global COUNT
    COUNT = []
    for i in range(1, SIZE_X +1):
        COUNT.append(A[i][1: -1])

dis = pygame.display.set_mode([550, 650])

flags = 0
class Button:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.show = False
        self.mark_bomba = False

        self.cur_x = MARGIN + self.x * SIZE + self.x  * PADDING
        self.cur_y = MARGIN + self.y * SIZE + self.y  * PADDING
        self.draw_voc = [self.cur_x, self.cur_y, SIZE, SIZE]

    def draw(self):
        if self.show:
            im = pygame.transform.scale(names[self.value], (SIZE, SIZE))
            dis.blit(im, (self.cur_x, self.cur_y))
        elif self.mark_bomba:
            im = pygame.transform.scale(names[MARK_BOMB], (SIZE, SIZE))
            dis.blit(im, (self.cur_x, self.cur_y))
        else:
            pygame.draw.rect(dis, BLACK, self.draw_voc)

    def showing(self):
        global ans
        if not self.mark_bomba:
            self.show = True
            if self.value == EMPTY:
                for elem in buttons:
                    if elem.check_neighbour(self.x, self.y) and not elem.show:
                        elem.showing()
        ans+=1

    def marking_bomba(self):
        global flags
        if not self.show:
            if self.mark_bomba == True:
                self.mark_bomba = False
                flags -= 1
            elif flags < COUNT_BOMB:
                self.mark_bomba = True
                flags += 1

    def check_click(self, mouse):
        return self.cur_x <= mouse[0] <= self.cur_x + SIZE and self.cur_y <=  mouse[1] <= self.cur_y + SIZE

    def check_neighbour(self, x, y):
        return abs(x - self.x) <= 1 and abs(y - self.y) <= 1


game = True
dis.fill(WHITE)
pygame.display.update()
def quest():
    global SIZE_X
    global SIZE_Y
    global COUNT_BOMB
    not_clik = True

    levels=[
        ('лёгкий','easy',80),
        ('средний', 'sred',180),
        ('тяжёлый', 'hard',280),
        ('кошмарный', 'very_hard',380)
        # ,('свой уровень', 'your', 480)
    ]

    while not_clik:
        font = pygame.font.Font('freesansbold.ttf', 70)
        textRects = {}
        for l in range(0,len(levels)):
            text = font.render(levels[l][0], True, WHITE, BLACK)
            textRects[l] = text.get_rect()
            textRects[l].center = (dis.get_width() // 2, levels[l][2])
            dis.blit(text, (textRects[l]))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                for l in range(0, len(levels)):
                    if textRects[l].left <= mouse[0] <= textRects[l].right and textRects[l].top <= mouse[1] <= textRects[l].bottom:
                        level = levels[l][1]
                        not_clik = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    level = 'volya'
                    not_clik = False
        pygame.display.update()
    if level == 'easy':
        SIZE_X = 8
        SIZE_Y = 9
        COUNT_BOMB = 1
    elif level == 'sred':
        SIZE_X = 10
        SIZE_Y = 12
        COUNT_BOMB = 20
    elif level == 'hard':
        SIZE_X = 12
        SIZE_Y = 13
        COUNT_BOMB = 30
    elif level == 'very_hard':
        SIZE_X = 13
        SIZE_Y = 15
        COUNT_BOMB = 40
    elif level == 'volya':
        SIZE_X = 19
        SIZE_Y = 3
        COUNT_BOMB = 19
    random_COUNT()

quest()
dis = pygame.display.set_mode([MARGIN * 2 + SIZE_X * SIZE + (SIZE_X - 1) * PADDING, MARGIN * 2 + SIZE_Y * SIZE + (SIZE_Y - 1) * PADDING])
ans = 0
while True:
    if game:
        dis.fill(WHITE)
        buttons = []
        for i in range(0, SIZE_X):
            for j in range(0, SIZE_Y):
                buttons.append(Button(i, j, COUNT[i][j]))  # COUNT[i][j]
        for i in range(0, len(buttons)):
            buttons[i].draw()
        pygame.display.update()
        proigrish = False
    else:
        x = 200
        y = 400
        x1 = 400
        y1 = 400
        dis.fill(WHITE)
        pygame.draw.rect(dis, BLACK, [x, y, SIZE, SIZE])
        pygame.draw.rect(dis, BLACK, [x1, y1, SIZE, SIZE])
        pygame.display.update()
    while game:

        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == 1:
                    for i in range(0, len(buttons)):
                        if buttons[i].check_click(mouse):
                            buttons[i].showing()
                elif event.button == 3:
                    for i in range(0, len(buttons)):
                        if buttons[i].check_click(mouse):
                            buttons[i].marking_bomba()
                for i in range(0, len(buttons)):
                    if buttons[i].value == BOMB and buttons[i].show and game == True:
                        proigrish = True
                        game = False
                        flags = 0
                        time.sleep(0.5)

                for i in range(0, len(buttons)):
                    if proigrish:
                        buttons[i].showing()
                    buttons[i].draw()
                pygame.display.update()

                if ans == SIZE_X * SIZE_Y - COUNT_BOMB and flags == COUNT_BOMB:  #?

                    messagebox.showinfo('Поздравляем!',
                                        "Вы победили. Продолжайте в этом духе!")
                    game = False
                    ans = 0
                    flags = 0
                if proigrish == True:
                    messagebox.showinfo('Сочувствуем!',
                                    "Вы проиграли. Желаем удачи в дальнейшем прохождении сапёра")
                    game = False
                    proigrish = False

    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 200 <= mouse[0] <= 200+ SIZE and 400 <= mouse[1] <= 400 + SIZE:
                game = True
                random_COUNT()
            elif 400 <= mouse[0] <= 400+ SIZE and 400 <= mouse[1] <= 400 + SIZE:
                dis.fill(WHITE)
                pygame.display.update()
                quest()
                dis = pygame.display.set_mode([MARGIN * 2 + SIZE_X * SIZE + (SIZE_X - 1) * PADDING,
                                               MARGIN * 2 + SIZE_Y * SIZE + (SIZE_Y - 1) * PADDING])
                game = True
    pygame.display.update()



    pygame.display.update()
# pygame.quit()
