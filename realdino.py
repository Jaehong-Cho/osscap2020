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
    global iScreenDx, iScreenDy, top, left, i,j, jump, count, ob_x
    iScreenDy = 16
    iScreenDx = 32
    top = 0
    left = 0
    ob_x = 33
    i = 0
    j = 0
    count = 0
    jump = False


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
    obstacle = [[[0, 0, 2, 0, 0],
        [2, 0, 2, 0, 0],
        [2, 0, 2, 0, 2],
        [2, 2, 2, 0, 2],
        [0, 0, 2, 2, 2],
        [0, 0, 2, 0, 0]],
        [[0, 2, 0, 2, 0],
        [2, 2, 0, 2, 2],
        [2, 2, 0, 2, 2],
        [0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0]]]

    return obstacle[num]


def d_cloud(num):
    cloud = [[[0, 7, 7, 7],
            [7, 7, 7, 0]],
            [[0, 7, 7, 0],
            [7, 7, 7, 7]]]

    return cloud(num)

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
        tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print(5)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()


    if jump == False:
        currBlk = Matrix(d_dino(i))
        top = 6
        left = 7
        if i == 0:
            i = 1
        elif i == 1:
            i = 0
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print(5)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()

    currBlk = Matrix(d_obstacle(0))
    if ob_x > 0:
        ob_x -= 1
    elif ob_x == 0:
        ob_x = 37
    left = ob_x
    top = 8
    tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()



    """
    currBlk = Matrix(d_boss(j))
    left = 24
    top = 0
    tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()
    """

    time.sleep(0.1    )
