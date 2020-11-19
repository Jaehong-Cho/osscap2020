import pygame as pg
import sys
import time
import random

image_load_list = [["walk_1", "걷기 1", (80, 80)], ["walk_2", "걷기 2", (80, 80)], ["cloud_image", "구름", (120, 36)],
                   ["dino_image", "dino", (80, 80)], ["obstacle_1", "선인장_2", (120, 100)],
                   ["obstacle_2", "선인장_3", (90, 90)], ["obstacle_3", "선인장_4", (50, 100)],
                   ["obstacle_4", "선인장_5", (130, 86)], ["t_gameover", "게임오버_글자", (480, 30)],
                   ["gameover_image", "게임오버 다시하기", (88, 80)], ["die_image", "dino die", (80, 80)],
                   ["hi_score", "하이스코어", (33, 18)], ["boss", "보스", (200, 150)], ["boss2", "보스2", (200,150)],
                   ["lazer", "레이저", (40,10)], ["warning", "워닝", (500, 100)], ["item", "아이템", (40, 40)]]

for image_load in image_load_list:
    globals()[image_load[0]] = pg.transform.scale(pg.image.load("image/{}.png".format(image_load[1])), image_load[2])

num_image_list = []
for a in range(10):
    num_image_list.append(pg.transform.scale(pg.image.load("image/{}.png".format(a)), (15, 18)))

random_obstacle_list = [(obstacle_1, (120, 100)), (obstacle_2, (90, 90)), (obstacle_3, (50, 100)),
                        (obstacle_4, (130, 86))]
random_item_list = [(item, (40, 40))]
random_lazer_list = [(lazer, (40,10))]

pg.init()
screen = pg.display.set_mode((1000, 500))
pg.display.set_caption("dino game")

pg.key.set_repeat(1, 1)

collision_list = [(57, 53), (11, 75), (83, 14)]
dust_list = []

best_score = 0


def game_set():
    global walk_image, dino_x, dino_y, walk_image2, add_cloud, cloud_list, boss_die, boss_hp, add_dust, add_lazer, lazer_list, dust_list, game_speed, speed_up, jump, jump_speed, add_obstacle, obstacle_list, add_item, item_list, die, score, plus_score
    walk_image = 0
    dino_x = 50
    dino_y = 380
    walk_image2 = 0
    add_cloud = 0
    add_dust = 0
    game_speed = 5
    speed_up = 0
    boss_hp = 2
    jump = False
    jump_speed = 0
    add_obstacle = 0
    add_item = 0
    add_lazer = 0
    obstacle_list = []
    item_list = []
    lazer_list = []
    die = False
    boss_die = False
    cloud_list = [[1000, 100]]
    score = 1
    plus_score = 0

def d_dino():
    global walk_image, walk_image2
    if die:
        screen.blit(die_image, (dino_x, dino_y))
    else:
        if jump:
            screen.blit(dino_image, (dino_x, dino_y))
        else:
            if walk_image % 2 == 1:
                screen.blit(walk_1, (dino_x, dino_y))
            else:
                screen.blit(walk_2, (dino_x, dino_y))
            if walk_image2 % 10 == 0:
                walk_image += 1


def u_dino():
    global walk_image2
    walk_image2 += 1


def d_cloud():
    for cloud in cloud_list:
        screen.blit(cloud_image, cloud)


def u_cloud():
    global add_cloud, cloud_list
    if add_cloud > random.randint(300, 500):
        cloud_list.append([1000, random.randint(20, 300)])
        add_cloud = 0
    for cloud in cloud_list:
        if cloud[0] < -200:
            cloud_list.remove(cloud)
        else:
            cloud[0] -= 1
    add_cloud += 1


def d_background():
    screen.fill((255, 255, 255))
    pg.draw.line(screen, (83, 83, 83), (0, 450), (1000, 450), 1)
    for dust in dust_list:
        pg.draw.line(screen, (83, 83, 83), (dust[0], dust[1]), (dust[0] + dust[2], dust[1]))


def u_background():
    global add_dust
    if add_dust % 3 == 0 or add_dust % 5 == 0:
        dust_list.append([1000, random.randint(455, 465), random.randint(2, 4)])
    for dust in dust_list:
        dust[0] -= game_speed
    add_dust += 1


def u_obstacle():
    global add_obstacle
    if add_obstacle > random.randint(300, 400):  # (obstacle_1, (150, 100))
        random_list = random_obstacle_list[random.randint(0, 3)]
        obstacle_list.append([random_list[0], [1000, random.randint(460, 470) - random_list[1][1]], random_list])
        add_obstacle = 0
    for obstacle in obstacle_list:
        if obstacle[1][0] < -200:
            obstacle_list.remove(obstacle)
        else:
            obstacle[1][0] -= game_speed
    add_obstacle += 1


def d_obstacle():
    for obstacle in obstacle_list:
        screen.blit(obstacle[0], obstacle[1])

def u_item():
    global add_item
    if add_item > random.randint(300, 400):
        random_list = random_item_list[0]
        item_list.append([random_list[0], [1000, random.randint(300, 310) - random_list[1][1]], random_list])
        add_item = 0
    for item in item_list:
        if item[1][0] < -200 or check_collision2():
            item_list.remove(item)
        else:
            item[1][0] -= game_speed*1.5
    add_item += 1


def d_item():
    for item in item_list:
        screen.blit(item[0], item[1])

def u_lazer():
    global add_lazer
    if add_lazer > random.randint(150, 200):
        random_list = random_lazer_list[0]
        lazer_list.append([random_list[0], [1000, random.randint(400, 410) - random_list[1][1]], random_list])
        add_lazer = 0
    for lazer in lazer_list:
        if lazer[1][0] < -200 or check_collision3():
            lazer_list.remove(lazer)
        else:
            lazer[1][0] -= game_speed*2
    add_lazer += 1

def d_lazer():
    for lazer in lazer_list:
        screen.blit(lazer[0], lazer[1])

def d_gameover():
    screen.blit(t_gameover, (260, 154))
    screen.blit(gameover_image, (446, 240))


def check_collision():
    for collision_xy in collision_list:
        for obstacle in obstacle_list:
            if dino_x + collision_xy[0] > obstacle[1][0] and dino_x + collision_xy[0] < obstacle[1][0] + obstacle[2][1][
                0] and dino_y + collision_xy[1] > obstacle[1][1] and dino_y + collision_xy[1] < obstacle[1][1] + \
                    obstacle[2][1][1]:
                return True

def check_collision2():
    for collision_xy in collision_list:
        for item in item_list:
            if dino_x + collision_xy[0] > item[1][0] and dino_x + collision_xy[0] < item[1][0] + item[2][1][
                0] and dino_y + collision_xy[1] > item[1][1] and dino_y + collision_xy[1] < item[1][1] + \
                    item[2][1][1]:
                return True

def check_collision3():
    for collision_xy in collision_list:
        for lazer in lazer_list:
            if dino_x + collision_xy[0] > lazer[1][0] and dino_x + collision_xy[0] < lazer[1][0] + lazer[2][1][
                0] and dino_y + collision_xy[1] > lazer[1][1] and dino_y + collision_xy[1] < lazer[1][1] + \
                    lazer[2][1][1]:
                return True

def u_score():
    global score, best_score, plus_score
    if score >= best_score:
        best_score = score
    plus_score += 1
    if plus_score % (16 - game_speed) == 0:
        score += 1


def d_score():
    screen.blit(hi_score, (710, 15))
    num = best_score
    for a in range(5):
        screen.blit(num_image_list[num // 10 ** (4 - a)], (770 + a * 19, 15))
        num = num % 10 ** (4 - a)
    num = score
    for a in range(5):
        screen.blit(num_image_list[num // 10 ** (4 - a)], (880 + a * 19, 15))
        num = num % 10 ** (4 - a)

def speed():
    global jump, jump_speed, speed_up, game_speed, dino_y
    if jump:
        dino_y -= jump_speed
        jump_speed -= 0.6
        if dino_y > 380:
            jump = False
    else:
        jump_speed = 0
    if not game_speed > 15:
        if speed_up % 1000 == 0:
            game_speed += 1
    speed_up += 1

def d_warning():
    screen.blit(warning, (250,200))


def u_boss():
    global boss_hp, boss_die, score
    if check_collision2():
        boss_hp -= 1
    if boss_hp == 0:
        boss_die = True
        score += 10

def d_boss():
    screen.blit(boss, (750, 100))

def d_boss2():
    screen.blit(boss2, (750, 100))

game_set()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if not die:
                    if not jump:
                        jump = True
                        jump_speed = 15
                else:
                    die = False
                    game_set()

    u_dino()
    d_background()
    d_cloud()
    d_obstacle()
    d_dino()
    d_score()

    if not die:
        u_score()
        u_background()
        u_cloud()
        u_obstacle()

        if check_collision() or check_collision3():
            die = True

        speed()
    else:
        d_gameover()

    if score >= 50 and score % 50 == 0:
        d_warning()
        pg.display.update()
        time.sleep(2)
        while(boss_die == False):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        if not die:
                            if not jump:
                                jump = True
                                jump_speed = 15
                        else:
                            die = False
                            game_set()

            u_dino()
            u_boss()
            d_background()
            d_cloud()
            d_item()
            d_lazer()
            d_dino()
            d_score()

            if boss_hp == 2:
                d_boss()
            if boss_hp == 1:
                d_boss2()

            if not die:
                u_background()
                u_cloud()
                u_item()
                u_lazer()

                if check_collision3():
                    die = True

                speed()
            else:
                d_gameover()

            pg.display.update()
            time.sleep(0.008)

    boss_die = False
    boss_hp = 2
    pg.display.update()

    time.sleep(0.008)
