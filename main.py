from realdino import *

while True:
    print("MODE")
    print("1. dino game \n2.Turn off")
    choice = int(input("Select the Mode : "))
    if choice == 1:
        realdino()
        break

    elif choice == 2:
        break

    else:
        print("잘못된 번호를 입력하셨습니다.")
        continue
