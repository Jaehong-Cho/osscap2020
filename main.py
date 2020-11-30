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
first_weather()
second_weather()

while True:
    
    #weather_init()
    print("<MODE>")
    print("-------------")
    print("1.Dino Game \n2.Weather Info \n3.Weather Info (100 times)\n4.Text Scrolling\n5.Turn off")
    print("-------------")
    choice = int(input("\nSelect the Mode : "))
    if choice == 1:
        py_realdino()
        assistant_info()
    elif choice == 2:
        first_weather()
        second_weather()
        assistant_info()
    elif choice == 3:
        for i in range(100):
            first_weather()
            second_weather()
            assistant_info()
    elif choice == 4:
        assistant_info()
    elif choice == 5:
        break
    else:
        print("잘못된 번호를 입력하셨습니다.")
        continue
