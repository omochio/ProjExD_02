import random
import math
import sys
import pygame as pg

def main():
    pg.display.set_caption("逃げろ！こうかとん")

    screen = pg.display.set_mode((1600, 900))
    screen_rect = screen.get_rect()

    clock = pg.time.Clock()

    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")

    kk_deth_img = pg.image.load("ex02/fig/8.png")
    kk_deth_img = pg.transform.rotozoom(kk_deth_img, 0, 2.0)

    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rot_dict = {
        (0, 0): kk_img,
        (0, -1): pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 90, 1),
        (1, -1): pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), 45, 1),
        (1, 0): pg.transform.flip(kk_img, True, False),
        (1, 1): pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), -45, 1),
        (0, 1): pg.transform.rotozoom(pg.transform.flip(kk_img, True, False), -90, 1),
        (-1, 1): pg.transform.rotozoom(kk_img, 45, 1),
        (-1, 0): kk_img,
        (-1, -1): pg.transform.rotozoom(kk_img, -45, 1)
    }
    kk_rect = kk_img.get_rect()
    kk_rect.center = (900, 400)

    bomb_img = pg.Surface((20, 20))
    pg.draw.circle(bomb_img, color=(255, 0, 0), center=(10, 10), radius=10)
    bomb_img.set_colorkey((0, 0, 0))
    bomb_rect = bomb_img.get_rect()
    bomb_rect.center = [random.randint(0, screen_rect.width), random.randint(0, screen_rect.height)]
    bomb_vel = [1, 1]

    ipt_dict = {
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, 1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (1, 0) 
    }

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        screen.blit(bg_img, [0, 0])

        prev_kk_center = kk_rect.center
        key_list = pg.key.get_pressed()
        kk_vel = [0, 0]
        for k, v in ipt_dict.items():
            if (key_list[k]):
                kk_rect.move_ip(v)
                kk_vel[0] += v[0]
                kk_vel[1] += v[1]
        kk_rot_img = kk_rot_dict[tuple(kk_vel)]
        if (check_in_screen(kk_rect, screen_rect) != (True, True)):
            kk_rect.center = prev_kk_center
        screen.blit(kk_rot_img, kk_rect)

        if (not check_in_screen(bomb_rect, screen_rect)[0]):
            bomb_vel[0] *= -1
        if (not check_in_screen(bomb_rect, screen_rect)[1]):
            bomb_vel[1] *= -1
        bomb_rect.move_ip(bomb_vel)
        
        screen.blit(bomb_img, bomb_rect)

        if (kk_rect.colliderect(bomb_rect)):
            screen.blit(bg_img, [0, 0])
            screen.blit(kk_deth_img, kk_rect)
            screen.blit(bomb_img, bomb_rect)
            pg.display.update()
            clock.tick(0.2)
            return

            

        pg.display.update()
        clock.tick(1000)

def check_in_screen(obj_rect: pg.Rect, screen_rect: pg.Rect):
    """
    オブジェクトが画面内にあるかを表すboolタプルを返す

    obj_rect: オブジェクトのRect
    screen_rect: ScreenのRect

    戻り値: (横方向, 縦方向) 
    """
    hor, ver = True, True
    if (obj_rect.left < screen_rect.left or obj_rect.right > screen_rect.right):
        hor = False
    if (obj_rect.top < screen_rect.top or obj_rect.bottom > screen_rect.bottom):
        ver = False
    return (hor, ver)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()