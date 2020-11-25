from py_realdino import *
import requests
from bs4 import BeautifulSoup
import time
import schedule
from auto_updating_naverWeather import *
import threading

def weather_init ():
    w_thread = threading.Thread(target=weather_main, args=())
    w_thread.setDaemon(True)
    w_thread.start()
    return

weather_init()

while True:  
	
    print("MODE")
    print("1. dino game \n2.Turn off")
    choice = int(input("Select the Mode : "))
    if choice == 1:
        realdino()
        continue

    elif choice == 2:
        continue
        
    else:
        print("잘못된 번호를 입력하셨습니다.")
        continue
