from matrix import *
import LED_display as LMD
import threading
import pygame as pg
import sys
import time
import random
import weather_dot as wd
from num_dot import *

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

def get_color(std):
	if std == "좋음" :
		return 4
	elif std == "보통":
		return 2
	elif std == "나쁨":
		return 3
	elif std == "매우나쁨":
		return 1

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

#미세먼지 등급표-파-초-주-빨
tag = [
	[1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1],
	[3, 3, 3, 3, 3, 3, 3, 3],
	[3, 3, 3, 3, 3, 3, 3, 3],
	[3, 3, 3, 3, 3, 3, 3, 3],
	[3, 3, 3, 3, 3, 3, 3, 3],
	[2, 2, 2, 2, 2, 2, 2, 2],
	[2, 2, 2, 2, 2, 2, 2, 2],
	[2, 2, 2, 2, 2, 2, 2, 2],
	[2, 2, 2, 2, 2, 2, 2, 2],
	[4, 4, 4, 4, 4, 4, 4, 4],
	[4, 4, 4, 4, 4, 4, 4, 4],
	[4, 4, 4, 4, 4, 4, 4, 4],
	[4, 4, 4, 4, 4, 4, 4, 4],]

iScreen = Matrix(game_screen)
oScreen = Matrix(iScreen)
LED_init()

top = 0
left = 0
currBlk = Matrix(tag)
tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tmpBlk = tmpBlk + currBlk
oScreen.paste(tmpBlk, top, left)

with open ("weather.txt", "r", encoding="utf8") as text:
	info = text.readlines()


#미세먼지 정보
micro_num1 = info[4][:3]
micro_num2 = info[4][:2]
micro_char1 = info[4][-5:-1]
micro_char2 = info[4][-3:-1]
if micro_char2 == "좋음" or micro_char2 == "보통":
	micro_num = int(micro_num2)
	micro_color = get_color(micro_char1)
elif micro_char1 == "매우나쁨":
	micro_num = int(micro_num1)
	micro_color = get_color(micro_char1)
elif micro_char2 == "나쁨" and micro_num2 > 80:
	micro_num = int(micro_num2)
	micro_color = get_color(micro_char2)
else:
	micro_num = int(micro_num1)
	micro_color = get_color(micro_char2)

top = 1
left = 18
while micro_num > 0 :
	tmp = get_num(micro_num % 10, micro_color)
	currBlk = Matrix(tmp)
	tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
	tmpBlk = tmpBlk + currBlk
	oScreen.paste(tmpBlk, top, left)
	left -= 6
	micro_num = micro_num // 10
	
#초미세먼지 정보
super_micro_num1 = info[5][:-5]
super_micro_num2 = info[5][:-7]
super_micro_char1 = info[5][-3:-1]
super_micro_char2 = info[5][-5:-1]
if super_micro_char2 == "매우나쁨":
	super_micro_num = int(super_micro_num2)
	super_micro_color = get_color(super_micro_char2)
else:
	super_micro_num = int(super_micro_num1)
	super_micro_color = get_color(super_micro_char1)

top = 8
left = 18
while super_micro_num > 0 :
	tmp = get_num(super_micro_num % 10, super_micro_color)
	currBlk = Matrix(tmp)
	tmpBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
	tmpBlk = tmpBlk + currBlk
	oScreen.paste(tmpBlk, top, left)
	left -= 6
	super_micro_num = super_micro_num // 10

draw_matrix(oScreen); print()
time.sleep(8)
