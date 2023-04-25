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
    bomb_img = pg.Surface((20, 20))
    pg.draw.circle(bomb_img, color=(255, 0, 0), center=(0, 0), radius=10)
    bomb_img.set_colorkey((0, 0, 0))
    bomb_pos = [random.randint(0, screen.get_width()), random.randint(0, screen.get_height())]
    screen.blit(bomb_img, bomb_pos)
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()