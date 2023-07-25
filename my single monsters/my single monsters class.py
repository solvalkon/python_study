import pygame
import os
from tkinter import messagebox
import time
import threading

pygame.init()
pygame.mixer.set_num_channels(20)

width = 150
height = 151
channel = 0
stop_music = False
fon_m = pygame.mixer.music
fon_m.load(os.path.join("sounds", "fon_m.mp3"))
fon_m.play()
fon = pygame.image.load(os.path.join("images", "fon.png"))
HEIGHT, WIDTH = fon.get_height(), fon.get_width()

dis = pygame.display.set_mode([WIDTH, HEIGHT])
dis.blit(pygame.transform.scale(pygame.image.load(os.path.join("images", "звук.png")), (WIDTH, HEIGHT)), (0, 0))


class Monster():
    def __init__(self, name, x, y, money, max_money, count):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("images", f"{name}.png")), (width, height))
        self.x = x
        self.y = y
        self.money = money
        self.max_money = max_money
        self.count = count


class Magazine():
    def __init__(self, name, all_seconds):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("images", f"{name}.png")), (width, height))
        self.name = name
        self.all_seconds = all_seconds
        self.all_seconds_pit = all_seconds
        self.image_egg = pygame.transform.scale(pygame.image.load(os.path.join("images", f"{name}_egg.png")), (100, 71))


def draw_image(dict):
    for x in dict:
        dis.blit(x.image, (x.x, x.y))


def monster_draw():
    for elem in all_vorabularu:
        draw_image(elem)


def muzic(dict, muz):
    global channel
    if len(dict) > 0:
        try:
            pygame.mixer.Channel(channel).play(pygame.mixer.Sound(os.path.join("sounds", muz)))
            channel += 1

        except FileNotFoundError:
            pass


def all_music():
    global channel
    global stop_music
    for i in range(channel):
        pygame.mixer.Channel(i).stop()
    channel = 0
    if not stop_music:
        muzic(bas, "ba_m.mp3")
        muzic(tus, "tu_m.mp3")
        muzic(mas, 'ma_m.mp3')
        muzic(pas, 'pa_m.mp3')
        muzic(tis, 'ti_m.mpeg')
        muzic(mars, 'mar_m.mp3')
        muzic(ras, 'ra_m.ogg')
        muzic(sms, 'sm_m.mp3.mpeg')
        muzic(lus, 'la_m.mp3')
        muzic(izs, 'iz_m.mpeg')
        muzic(izs, 'iz_m.mp3')
        threading.Timer(7, all_music).start()


def monster_money_every_minuts():
    global times
    times += 60
    all_draw()
    threading.Timer(60, monster_money_every_minuts).start()


def staving(vocabulary, name, money, max_money, count):
    global file
    global vrem_name
    vocabulary.append(Monster(stav, mouse[0] - width // 2, mouse[1] - height // 2, money, max_money, count))
    file.write(str(vocabulary[-1].x) + '  '+ str(vocabulary[-1].y) + '  ' + str(name) + '\n')
    vrem_name = ''
    all_draw()
    pygame.display.update()


def staving_(vocabulary, name, x, y, money, max_money, count):
    vocabulary.append(Monster(name, x, y, money, max_money, count))


def draw_money():
    x, y = 0, 0
    text = font.render(str(my_money), True, YELLOW, BLACK)
    dis.blit(text, (x, y))
    y += text.get_height()
    text = font.render(str(almaz), True, BLUE, BLACK)
    dis.blit(text, (x, y))


def close_coor():
    for i in range(mouse[0] - width//2, mouse[0] + width//2):
        for j in range(mouse[1] - height//2, mouse[1] + height//2):
            close.append((i, j))


def forx(voraluary: list, elem : str):
    global ans
    global count
    for x in voraluary:
        for i in range(x.x, x.x + width):
            for j in range(x.y, x.y + height):
                if mouse == (i, j):
                    ans += elem
                    monsters_in_pit.append(x.count)
                    count += 1



def clik_monster(voraluary):
    for x in voraluary:
        for i in range(x.x, x.x + width):
            for j in range(x.y, x.y + height):
                if mouse == (i, j):
                    return True

def magazin_clik(int,  image_x):
    global stav
    global game
    global eggs
    global vrem_name
    global all_seconds
    global my_money
    global monster_in_p
    mouse = pygame.mouse.get_pos()
    if mouse[0] in range(image_x[0], image_x[1]) and mouse[1] in range(HEIGHT // 3 - height // 2, HEIGHT // 3 + height):
        if my_money - 300 >= 0 and vrem_name == ''  and all_seconds <= 0:
            my_money -= 300
            game = True
            all_draw()
            dis.blit(magazine[int].image_egg, (WIDTH - 500 + width//2, height//2 + 27))
            pygame.display.update()

            vrem_name = magazine[int].name


            all_seconds = magazine[int].all_seconds
            monster_in_p = int
            timer()
        elif my_money <= 300:
            messagebox.showinfo("", "У вас не хватает денег")
            game = True
            all_draw()
            pygame.display.update()
        else:
            messagebox.showinfo("", "Питомник уже занят")
            game = True
            all_draw()
            pygame.display.update()


def monster_money(vocabulary):
    for x in vocabulary:
        if x.money*(times//60) < x.max_money:
            text = str(x.money*(times//60))
        else:
            text = str(x.max_money)

        text = font.render((text), True, YELLOW)
        dis.blit(text, (x.x + width // 4, x.y + height))


def sbor_money(vocabulary):
    global my_money
    global times
    for x in vocabulary:
        if x.money * (times // 60) <= x.max_money:
            my_money += x.money * (times // 60)
        else:
            my_money += x.max_money


def all_draw():
    global monster_in_p
    global monster_in_pit
    global monsters_in_pit



    dis.blit(fon, (0, 0))
    pygame.draw.rect(dis, YELLOW, (WIDTH - 100, HEIGHT - 100, 100, 100))
    draw_money()
    dis.blit(pit, (300, 0))
    dis.blit(ppp, (WIDTH - 500, 0))
    pygame.draw.rect(dis, BLACK, (0, HEIGHT - 100, 100, 100))


    pygame.draw.rect(dis, BLACK, (200, 0, 100, 100))

    text = font.render("-2", True, BLUE, BLACK)
    dis.blit(text, (0, 150))
    dis.blit(pygame.transform.scale(pygame.image.load(os.path.join("images", "звук.png")), (100, 100)),(100, HEIGHT - 100))
    monster_draw()

    if monster_in_p != -1:
        dis.blit(magazine[monster_in_p].image_egg, (WIDTH - 500 + width//2, height//2 + 27))
        stroka = str(all_seconds - seconds)
        dis.blit(font.render(str(all_seconds - seconds), True, WHITE), ((WIDTH - (400 + 10 *len(stroka)-1)) , 240))

    if monster_in_pit != -1:

        # dis.blit(magazine[monsters_in_pit[0]].image_egg, (300, 15))
        # dis.blit(magazine[monsters_in_pit[1]].image_egg, (450, 15))

        stroka = str(all_seconds_pit - seconds_pit)
        dis.blit(font.render(stroka, True, WHITE), (300 - (10 * len(stroka)-1), 240))

    for elem in all_vorabularu:
        monster_money(elem)


def timer_pit():
    global monster_in_p
    global all_seconds_pit
    global vrem_name
    global seconds_pit
    global all_seconds
    global monster_in_pit
    global all_seconds_pit
    global monsters_in_pit
    global vrem_name_pit
    global stav

    if game:
        all_draw()
        pygame.display.update()

    if seconds_pit < all_seconds_pit:
        seconds_pit += 1

        threading.Timer(1, timer_pit).start()

    else:
        if all_seconds == -1 and vrem_name == '' and monster_in_pit != -1:
            all_draw()
            dis.blit(magazine[monster_in_pit].image_egg, (300, 20))
            all_seconds = magazine[monster_in_pit].all_seconds
            monster_in_p = monster_in_pit
            monster_in_pit = -1
            seconds_pit = 0
            monsters_in_pit = []
            vrem_name_pit = ''

            # vrem_name = magazine[monster_in_pit].name
            vrem_name = stav

            pygame.display.update()
            timer()

        else:
            threading.Timer(1, timer_pit).start()


def timer():
    global eggs
    global stav
    global seconds
    global vrem_name
    global seall_seconds
    global monster_in_p
    global all_seconds

    if game:
        all_draw()
        pygame.display.update()

    if seconds < all_seconds:
        seconds += 1
        threading.Timer(1, timer).start()

    else:
        stav = vrem_name
        eggs = True
        monster_in_p = -1
        seconds = 0
        all_seconds = -1


def all_sbor_money():
    for elem in all_vorabularu:
        sbor_money(elem)


bas = []
tus = []
mas = []
pas = []
lus = []
osms = []
zes = []
uts = []
uds = []
kus = []
tis = []
ras = []
mars = []
sms = []
izs = []
magazine = []


WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
my_money = 1000
almaz = 100

all_vorabularu = [bas, tus, mas, pas, lus, zes, uts, uds, kus, osms, tis, sms, mars, ras, izs]
font = pygame.font.Font('freesansbold.ttf', 70)
count = 0
# fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))

close = []
stav = ''

times = 0

seconds = 0
seconds_pit = 0

monsters_in_pit = []


vrem_name = ''
vrem_name_pit = ''

monster_in_p = -1
monster_in_pit = -1



ba = pygame.transform.scale(pygame.image.load(os.path.join("images", "ba.png")), (width, height))
tu = pygame.transform.scale(pygame.image.load(os.path.join("images", "tu.png")), (width, height))
ma = pygame.transform.scale(pygame.image.load(os.path.join("images", "ma.png")), (width, height))
pa = pygame.transform.scale(pygame.image.load(os.path.join("images", "pa.png")), (width, height))

lu = pygame.transform.scale(pygame.image.load(os.path.join("images", "lu.png")), (width, height))
ku = pygame.transform.scale(pygame.image.load(os.path.join("images", "ku.png")), (width, height))
ze = pygame.transform.scale(pygame.image.load(os.path.join("images", "ze.png")), (width, height))
osm =pygame.transform.scale( pygame.image.load(os.path.join("images", "osm.png")), (width, height))
ud = pygame.transform.scale(pygame.image.load(os.path.join("images", "ud.png")), (width, height))
ut = pygame.transform.scale(pygame.image.load(os.path.join("images", "ut.png")), (width, height))

mar =pygame.transform.scale( pygame.image.load(os.path.join("images", "mar.png")), (width, height))
ti = pygame.transform.scale(pygame.image.load(os.path.join("images", "ti.png")), (width, height))
ra = pygame.transform.scale(pygame.image.load(os.path.join("images", "ra.png")), (width, height))
sm = pygame.transform.scale(pygame.image.load(os.path.join("images", "sm.png")), (width, height))

iz = pygame.image.load(os.path.join("images", f"iz.png"))

file = open('my single monsters.txt','r+')


pit = pygame.image.load(os.path.join("images", "питомник.png"))
ppp = pygame.image.load(os.path.join("images", "ppp.png"))

pit_width = 220
pit_height = 300
pit = pygame.transform.scale(pit, (pit_width, pit_height))
ppp = pygame.transform.scale(ppp, (pit_width + 50, pit_height))
dis.blit(fon, (0, 0))
dis.blit(pit, (300, 0))
dis.blit(ppp, (WIDTH - 500, 0))

pygame.draw.rect(dis, YELLOW, (WIDTH - 100, HEIGHT - 100, 100, 100))
draw_money()
ee = ''
monster_money_every_minuts()
pygame.draw.rect(dis, BLACK, (0, HEIGHT - 100, 100, 100))
pygame.display.update()


all_seconds = -1
all_seconds_pit = -1

game = True


for line in file:
    try:
        x, y, name = line.split('  ')
        x = int(x)
        y = int(y)
        if len(name) == 3:
            ee += name[-3]
            ee += name[-2]
            if ee == 'ba':
                staving_(bas, 'ba', x, y, 4, 18, 0)
                ee = ''
            elif ee == 'tu':
                staving_(tus, 'tu', x, y, 2,  30, 1)
                ee = ''
            elif ee == 'ma':
                staving_(mas, 'ma', x, y, 3, 30, 2)
                ee = ''
            elif ee == 'pa':
                staving_(pas, 'pa', x, y, 3, 18, 3)
                ee = ''

            elif ee == 'ze':
                staving_(zes, 'ze', x, y, 5, 225, 5)
                ee = ''
            elif ee == 'ud':
                staving_(uds, 'ud', x, y, 6, 180, 7)
                ee = ''
            elif ee == 'ut':
                staving_(uts, 'ut', x, y, 4, 300, 6)
                ee = ''
            elif ee == 'ku':
                staving_(kus, 'ku', x, y, 6, 120, 8)
                ee = ''
            elif ee == 'lu':
                staving_(lus, 'lu', x, y, 5, 225, 4)
                ee = ''
            elif ee == 'osm':
                staving_(osms, 'osm', x, y, 5, 300, 9)
                ee = ''
            elif ee == 'ti':
                staving_(tis, 'ti', x, y, 8, 2160, 10)
                ee = ''
            elif ee == 'sm':
                staving_(sms, 'sm', x, y, 7, 1890, 11)
                ee = ''
            elif ee == 'mar':
                staving_(mars, 'mar', x, y, 8, 1872, 12)
                ee = ''
            elif ee == 'ra':
                staving_(ras, 'ra', x, y, 9, 1872, 13)
                ee = ''

            elif ee == 'iz':
                staving_(izs, 'iz', x, y, 12, 11232, 14)
                ee = ''

        elif len(name) == 4:
            ee += name[-4]
            ee += name[-3]
            ee += name[-2]

            if name == 'osm':
                staving_(osms, 'osm', x, y, 5, 300, 9)
                ee = ''
        pygame.display.update()
    except:
        try:
            my_money, almaz = map(int, (line.split('  ')))
            monster_draw()
            pygame.display.update()

        except:
            try:
                all_seconds_pit, vrem_name_pit, monster_in_pit = line.split('    ')

                if int(all_seconds_pit) - times >= 0:
                    all_seconds_pit = int(all_seconds_pit) - times
                else:
                    all_seconds_pit = 0
                monster_in_pit = int(monster_in_pit)
            except:
                try:
                    all_seconds, vrem_name, monster_in_p = line.split('   ')
                    if int(all_seconds) - times >= 0:
                        all_seconds = int(all_seconds) - times
                    else:
                        all_seconds = -1
                    monster_in_p = int(monster_in_p)

                except:
                    try:
                        a, b, c, d, e = line.split('  ')
                        times = int(time.time()) - int(a) + int(b)
                    except:
                        pass


for elem in all_vorabularu:
    draw_image(elem)



for i in range(300, 300 + pit_width):
    for j in range(pit_height):
        close.append((i, j))
pygame.display.update()


cloak = time.time()



pit_ak = False

ans = ''

run = True

for elem in all_vorabularu:
    monster_money(elem)

pygame.display.update()

eggs = False

magazine.append(Magazine('ba', 5))
magazine.append(Magazine('tu', 60))
magazine.append(Magazine('ma', 2 * 60))
magazine.append(Magazine('pa', 2 * 60 * 60))
magazine.append(Magazine('lu', 30 * 60))
magazine.append(Magazine('ze', 8 * 60 * 60))
magazine.append(Magazine('ut', 8 * 60 * 60))
magazine.append(Magazine('ud', 8 * 60 * 60))
magazine.append(Magazine('ku', 8 * 60 * 60))
magazine.append(Magazine('osm', 8 * 60 * 60))
magazine.append(Magazine('ti', 8 * 60 * 60))
magazine.append(Magazine('sm', 12 * 60 * 60))
magazine.append(Magazine('mar',12 * 60 * 60))
magazine.append(Magazine('ra', 12 * 60 * 60))
magazine.append(Magazine('iz', 24 * 60 * 60))


if all_seconds >= 0:
    timer()

if all_seconds_pit >= 0:
    timer_pit()



# all_music()
fon_m.stop()






while run:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            file.write(str(my_money) + '  ' + str(almaz) + '\n')
            file.write(str(int(time.time())) + '  ' + str(times) + '  ' + '2  ' +'3  ' + '\n')


            try:
                file.write((str(all_seconds - seconds)) + '   ' + str(vrem_name) + '   ' + str(monster_in_p) + '\n')

            except:
                pass

            try:
                if all_seconds_pit > -1:

                    file.write(str(all_seconds_pit - seconds_pit) + '    ' + str(vrem_name_pit) + '    ' + str(monster_in_pit) + '\n')

            except:
                pass

            file.close()

            run = False
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse = pygame.mouse.get_pos()
            if game:
                if eggs == True and stav!= '' and game:
                    if 1100 > mouse[0] > 200 and 600 > mouse[1] > 150:
                        if mouse not in close:
                            eggs = False
                            seconds = 0
                            if stav == 'ba':
                                staving(bas, 'ba', 4, 18, 0)
                            elif stav == 'tu':
                                staving(tus, 'tu', 2, 30, 1)
                            elif stav == 'ma':
                                staving(mas, 'ma', 3, 30, 2)
                            elif stav == 'pa':
                                staving(pas, 'pa', 3, 18, 3)
                            elif stav == 'lu':
                                staving(lus, 'lu', 5, 225, 4)
                            elif stav == 'ze':
                                staving(zes, 'ze', 5, 225, 5)
                            elif stav == 'ku':
                                staving(kus, 'ku', 6, 120, 8)
                            elif stav == 'ut':
                                staving(uts, 'ut', 4, 300, 6)
                            elif stav == 'ud':
                                staving(uds, 'ud', 6, 180, 7)
                            elif stav == 'osm':
                                staving(osms, 'osm', 5, 300, 9)
                            elif stav == 'ti':
                                staving(tis, 'ti', 8, 2160, 10)
                            elif stav == 'mar':
                                staving(mars, 'mar', 8, 1872, 12)
                            elif stav == 'sm':
                                staving(sms, 'sm', 7, 1890, 11)
                            elif stav == 'ra':
                                staving(ras, 'ra', 9, 1872, 13)
                            elif stav == 'iz':
                                staving(izs, 'iz', 12, 11232, 14)
                            close_coor()


                            # song_f = False
                            stav = ''
                            all_draw()
                            pygame.display.update()



                elif pit_ak == True:
                        forx(bas, 'ba')
                        forx(tus, 'tu')
                        forx(mas, 'ma')
                        forx(pas, 'pa')
                        forx(lus, 'batu')
                        forx(uds, 'bama')

                        forx(uts, 'tuma')
                        forx(osms, 'tupa')
                        forx(zes, 'pama')
                        forx(osms, 'tupa')
                        forx(kus, 'tupa')



                        if count == 2:
                            seconds_pit = 0
                            if 'ba' in ans and 'tu' in ans and 'ma' in ans and 'pa' in ans:
                                all_seconds_pit = 24 * 60 * 60
                                monster_in_pit = 14
                                vrem_name_pit = 'iz'
                                timer_pit()
                                stav = 'iz'

                            elif 'ba' in ans and 'tu' in ans and 'ma' in ans:
                                all_seconds_pit = 8 * 60 * 60
                                monster_in_pit = 10
                                vrem_name_pit = 'ti'

                                timer_pit()

                                stav = 'ti'

                            elif 'ba' in ans and 'tu' in ans and 'pa' in ans:
                                all_seconds_pit = 12 * 60 * 60
                                monster_in_pit = 12
                                vrem_name_pit = 'mar'

                                timer_pit()
                                stav = 'mar'

                            elif 'ba' in ans and 'pa' in ans and 'ma' in ans:
                                all_seconds_pit = 12 * 60 * 60
                                monster_in_pit = 13
                                timer_pit()
                                vrem_name_pit = 'ra'
                                stav = 'ra'

                            elif 'pa' in ans and 'tu' in ans and 'ma' in ans:
                                all_seconds_pit = 12 * 60 * 60
                                monster_in_pit = 11
                                vrem_name_pit = 'sm'
                                timer_pit()
                                stav = 'sm'


                            elif 'tu' in ans and 'ba' in ans:
                                all_seconds_pit = 30 * 60
                                monster_in_pit = 4

                                vrem_name_pit = 'lu'

                                timer_pit()
                                stav = 'lu'


                            elif 'ma' in ans and 'tu' in ans:
                                all_seconds_pit = 8 * 60 * 60
                                monster_in_pit = 6
                                vrem_name_pit = 'ut'
                                timer_pit()

                                stav = 'ut'

                            elif 'ba' in ans and 'ma' in ans:
                                all_seconds_pit = 8 * 60 * 60
                                monster_in_pit = 7
                                vrem_name_pit = 'ud'
                                timer_pit()
                                stav = 'ud'

                            elif 'tu' in ans and 'pa' in ans:
                                all_seconds_pit = 8 * 60 * 60
                                monster_in_pit = 9
                                vrem_name_pit = 'osm'
                                timer_pit()
                                stav = 'osm'

                            elif 'ba' in ans and 'pa' in ans:
                                all_seconds_pit = 8 * 60 * 60
                                monster_in_pit = 8
                                vrem_name_pit = 'ku'
                                timer_pit()
                                stav = 'ku'

                            elif 'ma' in ans and 'pa' in ans:
                                all_seconds_pit = 8 * 60 * 60
                                monster_in_pit = 5
                                vrem_name_pit = 'ze'
                                timer_pit()
                                stav = 'ze'
                            all_draw()
                            pygame.display.update()
                            ans = ''
                            pit_ak = False
                            count = 0



                elif mouse[0] in range(WIDTH - 100, WIDTH) and mouse[1] in range(HEIGHT - 100, HEIGHT):

                    all_sbor_money()
                    times = 0
                    dis.fill(WHITE)
                    pygame.draw.rect(dis, BLACK, (WIDTH - 100, HEIGHT - 100, 100, 100))
                    game = False
                    draw_money()


                    for x in range(0, 4):
                        a = 0
                        if x == 1:
                            a = WIDTH // 4
                        elif x == 2:
                            a = WIDTH // 2
                        elif x == 3:
                            a = WIDTH - WIDTH // 4

                        dis.blit(magazine[x].image, (a, HEIGHT // 3))
                        text = font.render('300', True, YELLOW, WHITE)
                        dis.blit(text, (a, HEIGHT // 3 + height))



                elif mouse[0] in range(0, 100) and mouse[1] in range(HEIGHT - 100, HEIGHT):
                    all_sbor_money()
                    times = 0
                    all_draw()
                    pygame.display.update()



                elif mouse[0] in range(300, 300 + pit_width) and mouse[1] in range(pit_height):
                    if pit_ak == False:
                        pit_ak = True


                elif mouse[0] in range(0, 100) and mouse[1] in range(150, 250):
                    almaz -= 2
                    if seconds_pit + 3600 <= all_seconds_pit:
                        seconds_pit += 3600
                    else:
                        seconds_pit = all_seconds_pit


                    if seconds + 3600 <= all_seconds:
                        seconds += 3600
                    else:
                        seconds = all_seconds



                elif mouse[0] in range(200, 300) and mouse[1] in range(0, 100):


                    bas = []
                    tus = []
                    mas = []
                    pas = []
                    lus = []
                    osms = []
                    zes = []
                    uts = []
                    uds = []
                    kus = []
                    tis = []
                    ras = []
                    mars = []
                    sms = []
                    izs = []

                    all_vorabularu = [bas, tus, mas, pas, lus, zes, uts, uds, kus, osms, tis, sms, mars, ras, izs]




                    my_money = 1000
                    almaz = 1000
                    close = []

                    vrem_name = ''
                    vrem_name_pit = ''

                    seconds = 0
                    seconds_pit = 0

                    all_seconds = -1
                    all_seconds_pit = -1

                    monster_in_p = -1
                    monster_in_pit = -1

                    monsters_in_pit = []

                    channel = 0

                    count = 0

                    stav = ''

                    times = 0

                    file.truncate(0)

                    all_draw()
                    pygame.display.update()


                elif mouse[0] in range(WIDTH - 300, WIDTH) and mouse[1] in range (0, 300):
                    my_money += 10000
                    almaz += 100
                    seconds = all_seconds
                    seconds_pit = all_seconds_pit
                    all_draw()
                    pygame.display.update()

                elif mouse[0] in range(100, 200) and mouse[1] in range(HEIGHT - 100, HEIGHT):
                    if not stop_music:
                        stop_music = True
                    else:
                        stop_music = False
                        all_music()

                pygame.display.update()


            else:
                magazin_clik(0, (0, 0 + width))
                magazin_clik(1, (WIDTH // 4, WIDTH // 4 + width))
                magazin_clik(2, (WIDTH // 2, WIDTH // 2 + width))
                magazin_clik(3,  (WIDTH - WIDTH // 4, WIDTH - WIDTH // 4 + width))


                if mouse[0] in range(WIDTH - 100, WIDTH) and mouse[1] in range(HEIGHT - 100, HEIGHT):
                    game = True
                    all_draw()
                    pygame.display.update()