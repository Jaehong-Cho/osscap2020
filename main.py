from realdino import *
import requests
from bs4 import BeautifulSoup
import time
import schedule
from auto_updating_naverWeather import *

schedule.every(1).minutes.do(get_info)

while True:
	
	#auto_weather
	schedule.run_pending()
	time.sleep(1)
	
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
