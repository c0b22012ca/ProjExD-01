import pygame as pg
import sys

def main():
    r=0
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 =pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_imgc=pg.transform.rotozoom(kk_img,10,1.0)
    sur=[kk_img,kk_imgc]
    tmr = 0
    count=-1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        tmr += 1
        x=(tmr%3200)
        screen.blit(bg_img,[-x,0])
        screen.blit(bg_img2,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        if tmr%20<=8:
            screen.blit(sur[0],[300,200])
        elif tmr%20>8:
            screen.blit(sur[1],[300,200])
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()