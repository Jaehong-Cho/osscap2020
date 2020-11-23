from matrix import *
import LED_display as LMD
import threading
import pygame as pg
import sys
import time
import random

pg.init()
screen = pg.display.set_mode((1,1))

def LED_init():
    thread = threading.Thread(target = LMD.main, args())
    thread.setDaemon(True)
    thread.start()
    return

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx() - 8):
            if array[y][x] == 0:
                LMD.set_pixel(y, 19-x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, 19-x, 1)
            elif array[y][x] == 2:
                LMD.set_pixel(y, 19-x, 2)
            elif array[y][x] == 3:
                LMD.set_pixel(y, 19-x, 3)
            elif array[y][x] == 4:
                LMD.set_pixel(y, 19-x, 4)
            elif array[y][x] == 4:
                LMD.set_pixel(y, 19-x, 4)
            elif array[y][x] == 5:
                LMD.set_pixel(y, 19-x, 5)
            elif array[y][x] == 6:
                LMD.set_pixel(y, 19-x, 6)
            elif array[y][x] == 7:
                LMD.set_pixel(y, 19-x, 7) 
        print()

def game_set():
    global iScreenDx, iScreenDy, top, left, i,j,k, jump, count, ob_x, cd_x, bs_x, o, c, speed, score, boss_die
    iScreenDy = 16
    iScreenDx = 32
    top = 0
    left = 0
    ob_x = 38
    cd_x = 38
    bs_x = 38
    i = 0
    j = 0
    k = 0
    speed = 0
    o = random.randint(0,1)
    c = random.randint(0,1)
    count = 0
    score = 0
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

game_set()

LED_init()
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
    if 6 <= ob_x <= 9:
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
    if score >= 10 and score % 10 == 0:
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
        while(boss_die == False):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        jump == True

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
                dino_tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
                dino_tempBlk = dino_tempBlk + currBlk
                oScreen.paste(dino_tempBlk, top, left)



    draw_matrix(oScreen); print()

    score += 1

    time.sleep(0.5)
