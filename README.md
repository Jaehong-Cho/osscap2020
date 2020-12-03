# osscap2020
2020 오픈소스 기초설계 프로젝트
==================
(LED 스마트 스피커 / 공룡게임)
-----------------

### 처음 사용하기

미리 설치해야 되는 파이썬 라이브러리 : pygame, GPIO, beautifulsoup4, schedule   

* pygame

    $ python3 -m pip install -U pygame --user
    
* GPIO  
    
    $ sudo apt-get update   
    
    $ sudo apt-get install rpi.gpio 
 
* beautifulsoup4

    $ sudo apt-get update   
    
    $ sudo apt-get install python3-pip  # python3의 pip library update   
    
    $ pip3 install beautifulsoup4   

* schedule

    $ pip3 install schedule

> 준비물 : Raspberry Pi 4, USB 마이크, 3.5파이용 스피커, 16x32 LED matrix, LED matrix에 추가 전력을 공급할 5V/2A power adopter

    $ git clone https://github.com/Jaehong-Cho/osscap2020.git
  
    $ python3 main.py
    
#### 구글 어시스턴트 이용시 주의사항

구글 어시스턴트는 개별 등록이 필요한 서비스 입니다.
    
아래의 Googole API 링크를 통해서 단계에 따라서 수행하신 후에 이용가능합니다.

https://developers.google.com/assistant/sdk/guides/service/python/embed/setup

저희 시연영상과 같이 부팅과 동시에 google-assistant를 작동하시고 싶다면,

해당 repo의 ai_speaker --> make_auto_start.txt를 참고해주시기 바랍니다.

    $ cd                                 # 먼저 home 디렉토리로 이동합니다.
    
    $ nano google_auto_start.sh          # google_auto_start라는 shell파일을 생성합니다.
    
    <파일에 들어갈 내용>
    $ source env/bin/activate   
    $ google-assistant-demo --device-model-id "____"
    <저장 후 나가기>
    $ sudo chmod +x google_auto_start.sh # 해당 파일의 권한을 확장시켜 줍니다.
       
    $ ./google_auto_start.sh             # 위의 링크대로 라즈베리파이 등록이 잘되었다면 정상작동합니다.
    
    <이제 해당 sh파일을 라즈베리파이 루트에 있는 자동실행 명령어에 추가해 줍니다.>
    $ ls -al
    $ cd /etc/xdg/lxsession/LXDE-pi      # 라즈베리파이4용 명령어 입니다. 버전3은 다른 디렉토리입니다.
    $ nano autostart                     # ls를 하면, autostart라는 파일을 확인하실 수 있습니다.
    
    <autostart 파일 가장 맨 아래줄에 추가해줍니다.>
    $ /home/pi/google_auto_start.sh
-----------------------------------------------------------------

### 메인함수 실행시

실행시 처음 보이는 문구는 Google_info.py로 google assistant의 이용안내 문구인 <"헤이 구글"이라고 말하세요.>를 스크롤링 하는 모습을 보실 수 있습니다.

실제로 마이크에 "헤이 구글"을 말한 후, 궁금한 정보나 간단한 대화를 나눠보실 수 있습니다.

ex) 오늘 날씨, 오늘 점심 뭐 먹을까?

이후 LED로 날씨 정보에 대한 이모티콘, 현재 기온, 최고 기온, 최저 기온을 알려주는 first_weather.py가 실행되고,

미세먼지 농도, 초미세먼지 농도를 출력하는 second_weather.py가 자동 실행 됩니다.

------------------

참고로 메인함수에서 threading을 이용하여 날씨에 대한 정보는 1시간 간격으로 자동 업데이트합니다.

시간 간격에 대한 수정을 원하시다면, 
    
    vi auto_updating_naverWeather.py    
    마지막 블록에 있는
    schedule.every(60).minutes.do(get_info)에서 (숫자)를 수정하시면 됩니다.

-----------------------------------------------

### 기능 소개

이후 메뉴에는 1, 2, 3, 4, 5번이 있습니다.

>메뉴 1번은 공룡게임을 진행합니다.
키보드에서 space bar를 누르면 공룡이 점프하며, 장애물을 피할 수 있습니다.
어느 정도 점수에 도달하게 되면 보스 몬스터가 warning 메세지가 출력된 이후 LED화면에 오른쪽에서 천천히 나타납니다. 
공룡이 장애물이나 보스 몬스터의 공격에 맞게 되면, game over 메세지와 점수가 함께 출력되고 게임이 종료됩니다.        

    Q) 다시 1번을 눌렀을때 점프가 작동이 안되요.    
    A)이후 메뉴창이 다시 나타나게 되면 alt키 + tab키를 누른 후에 다시 공룡게임을 실행할지 날씨 정보를 출력할 지 선택할 수 있습니다.
    공룡게임을 재실행하면, alt키 + tab키 한번 더 눌러주어야 공룡이 점프할 수 있습니다.     
    즉, 공룡게임이 실행되면 pygame 실행 창이 뜨면서 게임이 실행 되는데 키보드 입력을 받는 게임 진행시 pygame활성창을 클릭하여야만 키보드 입력이 이뤄집니다.    
    키보드 입력을 pygame모듈을 사용하면서 생긴 문제점입니다.

>메뉴 2번은 날씨 정보를 1회 재출력합니다.   
출력되는 처음 출력되었던 형식과 동일합니다.

    first_weather.py
    second_weather.py
    날씨 정보는 main함수가 실행되고나서 부터 1시간마다 새롭게 업데이트 됩니다.

>메뉴 3번은 날씨 정보를 100회 재출력합니다.     
출력되는 정보는 처음 출력되었던 날씨 정보와 동일합니다.

>메뉴 4번은 텍스트 스크롤링으로 가장 처음에 보여준 어시스턴트 안내 문구를 보여줍니다.

    google_assistant_info.py

>메뉴 5번은 프로그램을 종료해 줍니다.

#### 더 자세한 기능 소개는 issue에 기재된 '결과 ppt 및 영상링크'를 참고해 주세요.

![all](https://user-images.githubusercontent.com/70634938/100569833-9492ab00-3312-11eb-9484-67228aa0d84f.jpg)

----------------------
> 공룡게임 오픈소스 https://github.com/byunkyunho/chrome-dino-game

> 웹 스크래핑 오픈소스 https://github.com/norangLemon/naverWeather

> 구글 API(assistant) https://developers.google.com/assistant/sdk/guides/service/python/embed/setup
