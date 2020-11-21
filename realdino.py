from matrix import *
import pygame as pg
import sys
import time
import random

pg.init()
screen = pg.display.set_mode((1,1))

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□ ", end='')
            elif 1 <= array[y][x] <= 7:
                print("■ ", end='')
            elif array[y][x] < 0:
                print("ㅇ ", end='')
            else:
                print("XX", end='')
        print()

def game_set():
    global iScreenDx, iScreenDy, top, left, i,j,k,l, jump, count, ob_x, cd_x, bs_x, lz_x, lz2_x, it_x, a, o, c, l, speed, boss_die,\
        gameover, boss_hp, t
    iScreenDy = 16
    iScreenDx = 32
    top = 0
    left = 0
    ob_x = 38
    cd_x = 38
    bs_x = 38
    lz_x = 30
    lz2_x = 29
    it_x = 0
    a = 7
    i = 0
    j = 0
    k = 0
    t = 0.5
    speed = 0
    o = random.randint(0,1)
    c = random.randint(0,1)
    l = 1
    count = 0
    boss_hp = 2
    gameover = False
    jump = False
    boss_die = False

def d_warning():
    warning = [[1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
               [1, 0, 1, 0, 1, 0, 3, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 0, 3, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
               [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1],
               [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
               [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1]]

    return warning


def d_dino(num):
    dino = [[[7, 7, 7, 0],
    [7, 0, 7, 7],
    [7, 7, 7, 0],
    [0, 7, 7, 7],
    [7, 7, 7, 0],
    [7, 7, 7, 7],
    [7, 0, 7, 0],
    [7, 0, 0, 7]],
    [[7, 7, 7, 0],
    [7, 0, 7, 7],
    [7, 7, 7, 0],
    [0, 7, 7, 7],
    [7, 7, 7, 0],
    [7, 7, 7, 7],
    [7, 0, 7, 0],
    [0, 7, 7, 0]]]

    return dino[num]

def d_obstacle(num):
    obstacle = [[[0, 2, 2, 2, 0],
        [0, 0, 2, 0, 0]],
        [[0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0]]]

    return obstacle[num]


def d_cloud(num):
    cloud = [[[0, 7, 7, 7],
            [7, 7, 7, 0]],
            [[0, 7, 7, 0],
            [7, 7, 7, 7]]]

    return cloud[num]

def d_boss(num):
    Boss = [[[0, 0, 7, 7, 7, 7, 0, 0],
             [0, 7, 7, 7, 7, 0, 7, 0],
             [0, 0, 0, 0, 7, 7, 7, 0],
             [0, 7, 7, 7, 7, 7, 0, 0],
             [0, 0, 0, 0, 7, 7, 0, 0],
             [7, 0, 7, 7, 7, 7, 7, 0],
             [7, 7, 7, 7, 7, 7, 7, 0],
             [0, 7, 0, 7, 7, 7, 7, 0],
             [7, 7, 0, 7, 7, 7, 7, 7],
             [0, 0, 0, 7, 7, 7, 7, 7],
             [0, 0, 0, 7, 0, 0, 7, 0],
             [0, 0, 7, 7, 0, 7, 7, 0],
             [0, 7, 7, 7, 7, 7, 7, 0],
             [7, 7, 0, 7, 7, 0, 7, 0]],
            [[0, 0, 1, 1, 1, 1, 0, 0],
             [0, 1, 1, 1, 1, 0, 1, 0],
             [0, 0, 0, 0, 1, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 0],
             [1, 0, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 1, 1, 1, 0],
             [1, 1, 0, 1, 1, 1, 1, 1],
             [0, 0, 0, 1, 1, 1, 1, 1],
             [0, 0, 0, 1, 0, 0, 1, 0],
             [0, 0, 1, 1, 0, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 0, 1, 1, 0, 1, 0]]]

    return Boss[num]

def d_lazer(num):
    lazer = [[[1, 1, 1, 0]],
             [[1, 1, 0],
              [1, 1, 0]],
             [[1, 1, 0],
              [1, 1, 0]]]

    return lazer[num]

def d_item():
    item = [[1],
        [1]]

    return item

game_screen = [
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -8, -8, -8, -8, -8, -8, -8, -8],
[-8, -8, -8, -8, -8, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, -8, -8, -8, -8, -8, -8, -8, -8]]

def d_boss_screen(a):

    boss_screen = [
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, 0, a, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, 0, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, 0, a, a, a, a, a, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, a, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, 0, a, a, a, a, a, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, a, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, 0, a, a, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, 0, a, a, 0, a, 0, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, -8, -8, -8, -8, -8, -8, -8, -8],
    [-8, -8, -8, -8, -8, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, -8, -8, -8, -8, -8, -8, -8, -8]]
    return boss_screen

game_set()
score = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                jump = True

    iScreen = Matrix(game_screen)
    oScreen = Matrix(iScreen)

    #공룡
    if jump == True:
        currBlk = Matrix(d_dino(0))
        count += 1
        if count < 6:
            j += 1
        elif count < 11:
            j -= 1
        elif count == 11:
            count = 0
            jump = False
        top = 6 - j
        left = 7
        dino_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
        dino_tempBlk = dino_tempBlk + currBlk
        oScreen.paste(dino_tempBlk, top, left)

    elif jump == False:
        currBlk = Matrix(d_dino(i))
        top = 6
        left = 7
        if i == 0:
            i = 1
        elif i == 1:
            i = 0
        dino_tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        dino_tempBlk = dino_tempBlk + currBlk
        oScreen.paste(dino_tempBlk, top, left)

    #장애물
    currBlk = Matrix(d_obstacle(o))
    if ob_x > 0:
        ob_x -= 1
    elif ob_x == 0:
        o = random.randint(0,1)
        ob_x = 37
    if 5 <= ob_x <= 10:
        if j < 2:
            print(score)
            break
    left = ob_x
    top = 12

    ob_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
    ob_tempBlk = ob_tempBlk + currBlk
    oScreen.paste(ob_tempBlk, top, left)

    ##구름
    currBlk = Matrix(d_cloud(c))
    if speed == 0:
        if cd_x > 0:
            cd_x -= 1
        elif cd_x == 0:
            c = random.randint(0,1)
            cd_x = 37
        speed = 1
    elif speed == 1:
        speed = 0
    top = 1
    left = cd_x

    cd_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
    cd_tempBlk = cd_tempBlk + currBlk
    oScreen.paste(cd_tempBlk, top, left)

    #보스관련
    if score >= 500 and score % 500 == 0:
        #워닝메세지
        currBlk = Matrix(d_warning())
        top = 0
        left = 5
        wn_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
        wn_tempBlk = wn_tempBlk + currBlk
        oScreen.paste(wn_tempBlk, top, left)
        draw_matrix(oScreen); print()
        time.sleep(3)

        # 보스 출현 애니메이션
        oScreen = Matrix(iScreen)
        currBlk = Matrix(d_dino(0))
        top = 6
        left = 7
        dino_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
        dino_tempBlk = dino_tempBlk + currBlk
        oScreen.paste(dino_tempBlk, top, left)
        draw_matrix(oScreen); print()
        currBlk = Matrix(d_boss(k))
        while (bs_x >= 30):
            bs_x -= 1
            left = bs_x
            top = 0
            bs_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
            bs_tempBlk = bs_tempBlk + currBlk
            oScreen.paste(bs_tempBlk, top, left)
            draw_matrix(oScreen); print()
            time.sleep(0.4)

        game_set()

        while(boss_hp > 0):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        jump = True

            if boss_hp == 2:
                a = 7
            elif boss_hp == 1:
                a = -8
            iScreen = Matrix(d_boss_screen(a))
            oScreen = Matrix(iScreen)

            if jump == True:
                currBlk = Matrix(d_dino(0))
                count += 1
                if count < 6:
                    j += 1
                elif count < 11:
                    j -= 1
                elif count == 11:
                    count = 0
                    jump = False
                top = 6 - j
                left = 7
                dino_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
                dino_tempBlk = dino_tempBlk + currBlk
                oScreen.paste(dino_tempBlk, top, left)

            if jump == False:
                currBlk = Matrix(d_dino(i))
                top = 6
                left = 7
                if i == 0:
                    i = 1
                elif i == 1:
                    i = 0
                dino_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
                dino_tempBlk = dino_tempBlk + currBlk
                oScreen.paste(dino_tempBlk, top, left)

            #레이저
            if l != 0 and lz2_x == 15:
                l = random.randint(0,1)
            if l == 0:
                top = 2
                if lz_x > 1:
                    lz_x -= 2
                elif lz_x == 0 or lz_x == 1:
                    lz_x = 29
                if 7 <= lz_x <= 10:
                    if j > 3:
                        print(score)
                        gameover = True
                        break
                left = lz_x

                currBlk = Matrix(d_lazer(l))
                lz_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
                lz_tempBlk = lz_tempBlk + currBlk
                oScreen.paste(lz_tempBlk, top, left)

            top = 11
            if lz2_x > 1:
                lz2_x -= 2
            elif lz2_x == 0 or lz2_x == 1:
                lz2_x = 28
            if 5 <= lz2_x <= 10:
                if j < 3:
                    print(score)
                    gameover = True
                    break
            left = lz2_x

            currBlk = Matrix(d_lazer(1))
            lz_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
            lz_tempBlk = lz_tempBlk + currBlk
            oScreen.paste(lz_tempBlk, top, left)

            #아이템
            if it_x == 0 and 10 == random.randint(1,10):
                it_x = 29
            if it_x > 0:
                it_x -= 1
            elif it_x == 0:
                it_x = 0
            if 6 <= it_x <= 10:
                if j > 0:
                    it_x = 0
                    boss_hp -= 1
                    score += 100
            left = it_x
            top = 4

            currBlk = Matrix(d_item())
            it_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
            it_tempBlk = it_tempBlk + currBlk
            oScreen.paste(it_tempBlk, top, left)

            draw_matrix(oScreen); print()
            score += 0.5
            time.sleep(t)

    boss_hp = 2

    if gameover:
        print(score)
        break

    draw_matrix(oScreen); print()

    score += 1
    if t > 0.3:
        t = t*0.99
    elif t < 0.3:
        t = t*0.999
    time.sleep(t)
