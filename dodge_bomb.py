import random
import sys
import pygame as pg

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()

    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")

    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    kk_rect.center = (900, 400)

    bomb_img = pg.Surface((20, 20))
    pg.draw.circle(bomb_img, color=(255, 0, 0), center=(10, 10), radius=10)
    bomb_img.set_colorkey((0, 0, 0))
    bomb_rect = bomb_img.get_rect()
    bomb_rect.center = [random.randint(0, screen.get_width()), random.randint(0, screen.get_height())]
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

        key_list = pg.key.get_pressed()
        for k, v in ipt_dict.items():
            if (key_list[k]):
                kk_rect.move_ip(v)

        screen.blit(kk_img, kk_rect)
        
        bomb_rect.move_ip(bomb_vel)
        screen.blit(bomb_img, bomb_rect)
        

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()