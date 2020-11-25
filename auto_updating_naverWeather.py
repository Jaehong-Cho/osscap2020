import requests
from bs4 import BeautifulSoup
import time
import schedule

def get_info():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = BeautifulSoup(html.text, 'html.parser')

    data1 = soup.find('div', {'class':'weather_box'})
    find_address = data1.find('span', {'class':'btn_select'}).text
    print('현재 위치: '+find_address)

    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
    print('현재 온도: '+find_currenttemp+'℃')

    find_cast = data1.find('p', {"class":"cast_txt"}).text
    print(find_cast)

    find_mintmp = data1.find('span', {'class':'min'}).text
    print('최저기온:'+find_mintmp)

    find_maxtmp = data1.find('span', {'class':'max'}).text
    print('최고기온:'+find_maxtmp)

    dust = soup.find("dl", attrs={"class":"indicator"})

    find_dust = dust.find_all("dd")[0].get_text()
    find_ultra_dust = dust.find_all("dd")[1].get_text()
    print('현재 미세먼지: '+find_dust)
    print('현재 초미세먼지: '+find_ultra_dust)

    with open("weather.txt", "w") as file:
        file.write(find_address)
        file.write("\n")
        file.write(find_currenttemp)
        file.write("\n")
        file.write(find_cast)
        file.write("\n")
        file.write(find_mintmp)
        file.write("\n")
        file.write(find_maxtmp)
        file.write("\n")
        file.write(find_dust)
        file.write("\n")
        file.write(find_ultra_dust)

def weather_main():
# 매시간마다 새로운 날씨 정보를 스크랩
    schedule.every(1).minutes.do(get_info)

    while True:
        schedule.run_pending()
    #time.sleep(1)

