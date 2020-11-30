from matrix import *
import LED_display as LMD
import threading
import pygame as pg
import sys
import time
import random
import weather_dot as wd
from num_dot import *


def first_weather():

    def LED_init():
        thread = threading.Thread(target = LMD.main, args=())
        thread.setDaemon(True)
        thread.start()
        return

    def draw_matrix(m):
        array = m.get_array()
        for y in range(16):
            for x in range (32):
                if array[y][x] == 0:
                    LMD.set_pixel(x, y, 0)
                elif array[y][x] == 1:
                    LMD.set_pixel(x, y, 1)
                elif array[y][x] == 2:
                    LMD.set_pixel(x, y, 2)
                elif array[y][x] == 3:
                    LMD.set_pixel(x, y, 3)
                elif array[y][x] == 4:
                    LMD.set_pixel(x, y, 4)
                elif array[y][x] == 5:
                    LMD.set_pixel(x, y, 5)
                elif array[y][x] == 6:
                    LMD.set_pixel(x, y, 6)
                elif array[y][x] == 7:
                    LMD.set_pixel(x, y, 7)
            print()

    game_screen = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    ###prepare the initial screen output
    iScreen = Matrix(game_screen)
    oScreen = Matrix(iScreen)
    LED_init()


    # weather.txt 파일에 접근하여 정보 가져오기
    # 사용할 정보 : 날씨 상태, 현재 기온, 최고 기온, 최저 기온
    # 각 인덱스 정보 : 1,         0,         3          2
    with open ("weather.txt", "r", encoding="utf8") as text:
        info = text.readlines()

    #날씨 상태 아이콘 불러오기
    #10x10 array
    icon = wd.weather_icon(info[1][:-14])
    #좌표
    top = 0
    left = 0
    currBlk = Matrix(icon)
    tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tmpBlk = tmpBlk + currBlk
    oScreen.paste(tmpBlk, top, left)

    #현재 온도 표시 글자색-흰색
    curr_tmp = int(info[0][:-1])
    if curr_tmp < 0 :
        curr_tmp = -curr_tmp
        option_blk = get_minus(7)
        #좌표
        top = 12
        left = 1

        currBlk = Matrix(option_blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)

    if 0 <= curr_tmp and curr_tmp < 10 :
        fir_Blk = get_num(curr_tmp, 7)
        #좌표
        top = 9
        left = 4

        currBlk = Matrix(fir_Blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)
    else :
        fir_Blk = get_num(curr_tmp // 10, 7)
        #좌표
        top = 9
        left = 4

        currBlk = Matrix(fir_Blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)

        sec_Blk = get_num(curr_tmp % 10, 7)
        #좌표
        top = 9
        left = 10

        currBlk = Matrix(sec_Blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)


    # 최고기온 표시
    # 글자색 - 빨간색
    max_tmp = int(info[3][:-2])
    if max_tmp < 0 :
        max_tmp = -max_tmp
        option_blk = get_minus(1)
        #좌표
        top = 3
        left = 16

        currBlk = Matrix(option_blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)

    if 0 <= max_tmp and max_tmp < 10 :
        fir_Blk = get_num(max_tmp, 1)
        #좌표
        top = 1
        left = 19

        currBlk = Matrix(fir_Blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)
    else :
        fir_Blk = get_num(max_tmp // 10, 1)
        #좌표
        top = 1
        left = 19

        currBlk = Matrix(fir_Blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)

        sec_Blk = get_num(max_tmp % 10, 1)
        #좌표
        top = 1
        left = 25

        currBlk = Matrix(sec_Blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)


    # 최저기온 표시
    # 글자색 - 파랑색
    min_tmp = int(info[2][:-2])
    if min_tmp < 0 :
        min_tmp = -min_tmp
        option_blk = get_minus(4)
        #좌표
        top = 12
        left = 16

        currBlk = Matrix(option_blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)


    if 0 <= min_tmp and min_tmp < 10 :
        fir_Blk = get_num(min_tmp, 4)
        #좌표
        top = 8
        left = 19

        currBlk = Matrix(fir_Blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)
    else :
        fir_Blk = get_num(min_tmp // 10, 4)
        #좌표
        top = 8
        left = 19

        currBlk = Matrix(fir_Blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)

        sec_Blk = get_num(min_tmp % 10, 4)
        #좌표
        top = 8
        left = 25

        currBlk = Matrix(sec_Blk)
        tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tmpBlk = tmpBlk + currBlk
        oScreen.paste(tmpBlk, top, left)
    draw_matrix(oScreen); print()
    time.sleep(5)
