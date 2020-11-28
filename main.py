from py_realdino import *
from assistant_info import *
from first_weather import *
from second_weather import *
import requests
from bs4 import BeautifulSoup
import time
import schedule
from auto_updating_naverWeather import *
import threading


def weather_init():
    w_thread = threading.Thread(target=weather_main, args=())
    w_thread.setDaemon(True)
    w_thread.start()
    return
weather_init()


assistant_info()
time.sleep(3)
first_weather()
time.sleep(3)
second_weather()
time.sleep(3)

while True:
    
    #weather_init()

    print("MODE")
    print("1.dino game \n2.weather info \n3.Turn off")
    choice = int(input("Select the Mode : "))
    if choice == 1:
        py_realdino()
        continue
    elif choice == 2:
        time.sleep(3)
        first_weather()
        time.sleep(3)
        second_weather()
        time.sleep(3)
    elif choice == 3:
        break
    else:
        print("잘못된 번호를 입력하셨습니다.")
        continue
