import pygame
import random
import os
import time
from tkinter import messagebox
pygame.init()

BLOCK_SIZE = 160
PADDING_SIZE = 5
MARGIN_SIZE = 10
BLOCK_COUNT_X = 4
BLOCK_COUNT_Y = 4
FINISH_POWER = 11
IMAGE_FOLDER = 'numbers' #fish

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if random.randint(1, 10) == 1:
            self.pow = 2
        else:
            self.pow = 1

    def power_up(self):
        self.pow += 1
        update_record(self.pow)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def located(self, x, y):
        return self.x == x and self.y == y

    def draw(self):
        x = MARGIN_SIZE + self.x * (BLOCK_SIZE + PADDING_SIZE)
        y = MARGIN_SIZE + self.y * (BLOCK_SIZE + PADDING_SIZE)
        im = pygame.image.load(os.path.join(IMAGE_FOLDER, f"" + str(2 ** self.pow) + ".png"))
        im = pygame.transform.scale(im, (BLOCK_SIZE, BLOCK_SIZE))
        dis.blit(im, (x, y))

    def mark(self):
        x = MARGIN_SIZE + self.x * (BLOCK_SIZE + PADDING_SIZE)
        y = MARGIN_SIZE + self.y * (BLOCK_SIZE + PADDING_SIZE)
        pygame.draw.rect(dis, GREEN, [x, y, BLOCK_SIZE/4, BLOCK_SIZE/4])

record = FINISH_POWER

def update_record(pow):
    global record
    if pow == record:
        messagebox.showinfo('Поздравляем!', 'Вы достигли: ' + str(2 ** record) + ', следующая цель: ' + str(2 ** (record + 1)))
        record += 1
        show_caption()


def show_caption():
    global record
    pygame.display.set_caption(str(2 ** record))
    programIcon = pygame.image.load(os.path.join(IMAGE_FOLDER, f"" + str(2 ** record) + ".png"))
    pygame.display.set_icon(programIcon)

total_width = BLOCK_SIZE * BLOCK_COUNT_X + (BLOCK_COUNT_X - 1) * PADDING_SIZE + MARGIN_SIZE * 2
total_height = BLOCK_SIZE * BLOCK_COUNT_Y + (BLOCK_COUNT_Y - 1) * PADDING_SIZE + MARGIN_SIZE * 2
dis = pygame.display.set_mode([total_width, total_height])

show_caption()

WHITE = (250, 250, 250)
GREEN = (0, 250, 0)
RED = (250, 0, 0)
BLACK = (0, 0, 0)
dis.fill(WHITE)
blocks = []

def proverka(x, y):
        for i in range(len(blocks)):
            if blocks[i].located(x, y):
                return i
        return -1

def dvigenie(dx, dy):
    dvigenie_ = False
    moved = True
    while moved:
        remove = []
        moved = False
        for i in range(0, len(blocks)):
            block = blocks[i]
            if (block.x + dx >= 0) and (block.x + dx < BLOCK_COUNT_X) and (block.y + dy >= 0) and (block.y + dy < BLOCK_COUNT_Y):
                j = proverka(block.x + dx, block.y + dy)
                if j == -1:
                    block.move(dx, dy)
                    dvigenie_ = True
                    moved = True
                else:
                     if blocks[i].pow == blocks[j].pow:
                         remove.append(i)
                         blocks[j].power_up()
                         dvigenie_ = True
                         moved = True

        for i in reversed(remove):
            blocks.pop(i)

    return dvigenie_

x = random.randint(0, BLOCK_COUNT_X - 1)
y = random.randint(0, BLOCK_COUNT_Y - 1)
blocks.append(Block(x, y))

blocks[0].draw()
pygame.display.update()

game = True
quit_press = False
while game or not quit_press:
    xod = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_press = True
        if event.type == pygame.KEYDOWN:
            newplit = False
            split = []
            if event.key == pygame.K_LEFT:
                xod = xod or dvigenie(-1, 0)
            elif event.key == pygame.K_RIGHT:
                xod = xod or dvigenie(1, 0)
            elif event.key == pygame.K_UP:
                xod = xod or dvigenie(0, -1)
            elif event.key == pygame.K_DOWN:
                xod = xod or dvigenie(0, 1)
            elif event.key == pygame.K_F2:
                for i in range(0, len(blocks)):
                    blocks[i].power_up()

            free = []
            for x in range(0, BLOCK_COUNT_X):
                for y in range(0, BLOCK_COUNT_Y):
                    if proverka(x, y) == -1:
                        free.append((x, y))

            if len(free) == 0:
                game = False
            else:
                newplit = random.choice(free)
                if xod:
                    blocks.append(Block(newplit[0], newplit[1]))

            dis.fill(WHITE)
            for i in range(0, len(blocks)):
                blocks[i].draw()
            blocks[len(blocks) - 1].mark()
            pygame.display.update()
#final_images = [f"win.png", f"win1.png"]

if quit_press:
    print ('До свидания')
else:
    final_images = [f"pro.png", f"pro1.png"]

dis.fill(WHITE)
for i in range(0,len(final_images)):
    image = pygame.image.load(os.path.join("Images", final_images[i]))
    kx = total_width / max(image.get_width(), total_width)
    image = pygame.transform.scale(image,(kx*image.get_width(),kx*image.get_height()))
    dis.blit(image, ((total_width - image.get_width())//2, total_height//(len(final_images)+1) * i))
    pygame.display.update()
    time.sleep(2)

pygame.quit()
